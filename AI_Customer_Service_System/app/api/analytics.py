from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..db.session import get_db
from ..db.models import ChatSession, Message, Escalation

router = APIRouter()

@router.get("/dashboard")
def get_analytics(db: Session = Depends(get_db)):
    total_sessions = db.query(ChatSession).count()
    total_messages = db.query(Message).count()
    total_escalations = db.query(Escalation).count()
    
    # Top Intents
    top_intents = db.query(Message.intent, func.count(Message.intent))\
        .filter(Message.sender == 'bot')\
        .group_by(Message.intent)\
        .order_by(func.count(Message.intent).desc())\
        .limit(5).all()
    
    return {
        "metrics": {
            "total_sessions": total_sessions,
            "total_messages": total_messages,
            "escalation_rate": f"{(total_escalations/total_sessions)*100:.2f}%" if total_sessions > 0 else "0%",
        },
        "top_intents": [{"intent": i[0], "count": i[1]} for i in top_intents]
    }
