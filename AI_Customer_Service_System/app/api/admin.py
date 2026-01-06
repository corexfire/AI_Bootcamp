from fastapi import APIRouter, Depends
from ..core.nlp_engine import nlp_engine

router = APIRouter()

@router.post("/train")
def train_model():
    """
    Trigger manual retraining of the NLP model.
    Use this endpoint after updating data/intents.json.
    """
    try:
        nlp_engine.load_data() # Reload data from JSON
        nlp_engine.train()     # Retrain Pipeline
        return {
            "message": "Model retrained successfully",
            "total_intents": len(nlp_engine.intents)
        }
    except Exception as e:
        return {"error": str(e)}
