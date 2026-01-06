from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..db.session import get_db
from ..core.conversation import ConversationManager
from ..core.nlp_engine import nlp_engine
import uuid

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str = None
    message: str
    platform: str = "web"
    language: str = "en" # Added language parameter, default 'en'

class ChatResponse(BaseModel):
    session_id: str
    response: str
    intent: str
    confidence: float
    language: str

@router.on_event("startup")
async def startup_event():
    # Force retrain to ensure new intents are loaded
    nlp_engine.train()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest, db: Session = Depends(get_db)):
    # Generate session ID if not provided
    if not request.session_id:
        request.session_id = str(uuid.uuid4())
    
    manager = ConversationManager(db)
    
    # Process message with language
    result = manager.process_message(
        request.session_id, 
        request.message, 
        request.platform, 
        request.language
    )
    
    return ChatResponse(
        session_id=request.session_id,
        response=result["response"],
        intent=result["intent"],
        confidence=result["confidence"],
        language=request.language
    )

@router.get("/health")
def health_check():
    return {"status": "ok", "nlp_model": "loaded"}
