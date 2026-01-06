from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class ChatSession(Base):
    __tablename__ = "sessions"
    
    id = Column(String, primary_key=True, index=True) # UUID
    user_id = Column(String, index=True, nullable=True) # Optional if anonymous
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    platform = Column(String, default="web") # whatsapp, web, telegram
    language = Column(String, default="en") # en, id
    
    messages = relationship("Message", back_populates="session")

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, ForeignKey("sessions.id"))
    sender = Column(String) # "user" or "bot"
    content = Column(Text)
    intent = Column(String, nullable=True) # Detected intent
    confidence = Column(Integer, nullable=True) # Confidence score
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    session = relationship("ChatSession", back_populates="messages")

class Escalation(Base):
    __tablename__ = "escalations"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, ForeignKey("sessions.id"))
    reason = Column(String)
    status = Column(String, default="pending") # pending, resolved
    created_at = Column(DateTime, default=datetime.utcnow)

# Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./customer_service.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
