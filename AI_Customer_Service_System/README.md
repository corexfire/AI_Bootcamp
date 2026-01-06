# AI Customer Service System

A production-ready, AI-powered Customer Service Chatbot built with Python, FastAPI, and Scikit-learn.

## Features
- **Intelligent Intent Classification**: Uses TF-IDF and Logistic Regression to understand user queries.
- **Context Awareness**: Handles multi-turn conversations (e.g., Order Tracking).
- **Escalation System**: Automatically detects when to hand off to human agents.
- **CRM Integration**: Mock integration for checking order status.
- **Analytics Dashboard**: Tracks session metrics and top intents.
- **REST API**: Fully documented API with Swagger UI.

## Project Structure
```
AI_Customer_Service_System/
├── app/
│   ├── api/            # Endpoints (Chat, Analytics)
│   ├── core/           # NLP Engine & Conversation Logic
│   ├── db/             # Database Models (SQLite)
│   ├── services/       # External Integrations (CRM)
│   └── main.py         # Entry Point
├── data/               # Intents & Models
├── tests/              # Simulation Scripts
```

## Setup & Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server**:
   ```bash
   uvicorn app.main:app --reload --app-dir .
   ```

3. **Access Documentation**:
   Open `http://localhost:8000/docs` to see the interactive API documentation.

## Testing
Run the simulation script to verify the chat flow:
```bash
python tests/simulation.py
```

## Use Cases Covered
1. **FAQ**: Hours, Location.
2. **Order Tracking**: "Where is my order?" -> User provides ID -> System checks CRM.
3. **Complaints**: Handling product issues.
4. **Escalation**: "I want to talk to a human".
