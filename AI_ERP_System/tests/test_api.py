from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
import sys
import os

# Add app to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "active"

@patch('app.modules.manufacturing.router.maintenance_model')
def test_predict_failure(mock_model):
    mock_model.predict.return_value = {
        "prediction": 0,
        "failure_probability": 0.1,
        "status": "Healthy"
    }
    
    payload = {
        "temperature": 80.0,
        "vibration": 0.5,
        "pressure": 100.0,
        "rpm": 1500.0,
        "usage_hours": 500.0
    }
    
    response = client.post("/api/v1/manufacturing/predict-failure", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "Healthy"

@patch('app.modules.distribution.router.route_optimizer')
def test_optimize_route(mock_optimizer):
    mock_optimizer.solve_tsp_nearest_neighbor.return_value = {
        "optimized_route": ["depot", "A"],
        "total_distance": 10.0
    }
    
    payload = {
        "locations": [
            {"id": "depot", "coords": [0, 0]},
            {"id": "A", "coords": [10, 0]}
        ]
    }
    
    response = client.post("/api/v1/distribution/optimize-route", json=payload)
    assert response.status_code == 200
    assert "optimized_route" in response.json()

@patch('app.modules.financial.router.anomaly_detector')
def test_detect_anomaly(mock_detector):
    mock_detector.detect.return_value = {
        "is_anomaly": False,
        "anomaly_score": 0.1,
        "risk_level": "Low"
    }
    
    payload = {
        "amount": 100.0,
        "hour": 10,
        "category_encoded": 1,
        "is_weekend": 0
    }
    
    response = client.post("/api/v1/financial/detect-anomaly", json=payload)
    assert response.status_code == 200
    assert response.json()["is_anomaly"] is False
