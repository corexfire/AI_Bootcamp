from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from app.modules.financial.anomaly_detection.detector import AnomalyDetector
from app.modules.financial.cash_flow.predictor import CashFlowPredictor

router = APIRouter()

# Schemas
class Transaction(BaseModel):
    amount: float
    hour: int
    category_encoded: int
    is_weekend: int

class CashFlowData(BaseModel):
    date: str
    net_cash_flow: float # Previous day actual
    lag_1: float
    lag_7: float

# Instances
anomaly_detector = AnomalyDetector()
cashflow_predictor = CashFlowPredictor()

@router.post("/detect-anomaly")
def detect_anomaly(transaction: Transaction):
    try:
        return anomaly_detector.detect(transaction.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict-cashflow")
def predict_cashflow(data: CashFlowData):
    try:
        # We pass the input data which represents "yesterday" or known features
        # to predict "today/tomorrow"
        return cashflow_predictor.predict_next_day(data.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
