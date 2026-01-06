from fastapi import FastAPI
from .api import chat, analytics, admin
from .db.models import init_db

app = FastAPI(
    title="AI Customer Service System",
    description="Enterprise-grade AI Chatbot for Customer Support",
    version="1.0.0"
)

# Initialize Database
init_db()

# Include Routers
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])
app.include_router(analytics.router, prefix="/api/v1", tags=["Analytics"])
app.include_router(admin.router, prefix="/api/v1", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "Welcome to AI Customer Service API. Visit /docs for Swagger UI."}
