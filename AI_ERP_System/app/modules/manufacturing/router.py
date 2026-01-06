from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
import shutil
import os
import uuid

from app.modules.manufacturing.predictive_maintenance.model import PredictiveMaintenanceModel
from app.modules.manufacturing.quality_control.model import QualityControlModel
from app.modules.manufacturing.supply_chain.optimizer import SupplyChainOptimizer

router = APIRouter()

# Models
class SensorData(BaseModel):
    temperature: float
    vibration: float
    pressure: float
    rpm: float
    usage_hours: float

class SupplyParams(BaseModel):
    daily_usage: List[float]
    lead_time_days: int

# Instances (Lazy loading handled in classes or init here)
maintenance_model = PredictiveMaintenanceModel()
qc_model = QualityControlModel()
supply_optimizer = SupplyChainOptimizer()

@router.post("/predict-failure")
def predict_failure(data: SensorData):
    try:
        result = maintenance_model.predict(data.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/quality-check")
def quality_check(file: UploadFile = File(...)):
    temp_file = f"temp_{uuid.uuid4()}.jpg"
    try:
        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        result = qc_model.predict(temp_file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

@router.post("/optimize-supply")
def optimize_supply(params: SupplyParams):
    try:
        result = supply_optimizer.optimize_reorder_point(
            params.daily_usage, 
            params.lead_time_days
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
