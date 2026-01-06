from ..db.models import ChatSession, Message, Escalation
from .nlp_engine import nlp_engine
from ..services.crm_integration import CRMService
import uuid

class ConversationManager:
    def __init__(self, db_session):
        self.db = db_session
        self.crm = CRMService()

    def process_message(self, session_id, user_message, platform="web", language="en"):
        # 1. Retrieve or Create Session
        session = self.db.query(ChatSession).filter(ChatSession.id == session_id).first()
        if not session:
            session = ChatSession(id=session_id, platform=platform, language=language)
            self.db.add(session)
            self.db.commit()
        else:
            # Update language if provided and different
            if language and session.language != language:
                session.language = language
                self.db.commit()
            
            # Use session language if request language is not explicit (or handled by caller)
            language = session.language

        # 2. Log User Message
        self.log_message(session_id, "user", user_message)

        # 3. Context Handling (Simple State Machine)
        last_bot_msg = self.db.query(Message).filter(Message.session_id == session_id, Message.sender == "bot").order_by(Message.timestamp.desc()).first()
        
        response_text = ""
        intent_tag = ""
        confidence = 0.0

        # --- SPECIAL LOGIC FOR CONTEXT ---
        # Detect order ID pattern (simplified) - Context: awaiting_order_id
        # We need to know if the last message from bot was asking for Order ID. 
        # Since we don't store "context" state explicitly in DB (only intent), we check last intent or content.
        # Ideally, we should store `current_context` in Session table. For now, heuristics:
        
        is_order_flow = False
        if last_bot_msg and ("provide your Order ID" in last_bot_msg.content or "berikan Order ID" in last_bot_msg.content):
             is_order_flow = True

        if is_order_flow:
            # Assume user is providing Order ID
            order_id = user_message.strip()
            status, desc = self.crm.get_order_status(order_id)
            
            # Multilingual response for CRM
            if language == 'id':
                status_map = {"Shipped": "Dikirim", "Cancelled": "Dibatalkan", "Processing": "Diproses"}
                desc_map = {
                    "Your order is on the way and will arrive tomorrow.": "Pesanan Anda sedang dalam perjalanan dan akan tiba besok.",
                    "Your order was cancelled due to payment failure.": "Pesanan dibatalkan karena pembayaran gagal.",
                    "We are currently packing your order.": "Kami sedang mengemas pesanan Anda."
                }
                status = status_map.get(status, status)
                desc = desc_map.get(desc, desc)
                response_text = f"Order {order_id}: {status}. {desc}"
            else:
                response_text = f"Order {order_id}: {status}. {desc}"
                
            intent_tag = "check_order_status_fulfillment"
            confidence = 1.0
        
        else:
            # 4. NLP Prediction
            intent_tag, confidence = nlp_engine.predict(user_message)
            
            # Confidence Threshold
            if confidence < 0.4:
                intent_tag = "fallback"
                response_text = "Maaf, saya kurang mengerti." if language == 'id' else "I'm sorry, I didn't quite catch that. Could you rephrase?"
            else:
                # Pass language to get_response
                response_text, context_set = nlp_engine.get_response(intent_tag, lang=language)

                # --- SPECIAL ACTIONS BASED ON INTENT ---
                if intent_tag == "human_agent":
                    reason = "User requested agent"
                    self.escalate_to_human(session_id, reason)
                    if language == 'id':
                        response_text += " (Tiket #Human-Request dibuat)"
                    else:
                        response_text += " (Ticket #Human-Request created)"
                
        # 5. Log Bot Response
        self.log_message(session_id, "bot", response_text, intent_tag, confidence)

        return {
            "response": response_text,
            "intent": intent_tag,
            "confidence": float(confidence)
        }

    def log_message(self, session_id, sender, content, intent=None, confidence=None):
        msg = Message(
            session_id=session_id, 
            sender=sender, 
            content=content,
            intent=intent,
            confidence=confidence
        )
        self.db.add(msg)
        self.db.commit()

    def escalate_to_human(self, session_id, reason):
        escalation = Escalation(session_id=session_id, reason=reason)
        self.db.add(escalation)
        self.db.commit()
