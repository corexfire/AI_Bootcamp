import sys
import os
import pandas as pd
import numpy as np
import cv2

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.modules.manufacturing.predictive_maintenance.model import PredictiveMaintenanceModel
from app.modules.manufacturing.quality_control.model import QualityControlModel
from app.modules.financial.anomaly_detection.detector import AnomalyDetector
from app.modules.financial.cash_flow.predictor import CashFlowPredictor

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def generate_maintenance_data(n_samples=1000):
    print("Generating Maintenance Data...")
    np.random.seed(42)
    data = {
        'temperature': np.random.normal(70, 10, n_samples),
        'vibration': np.random.normal(0.5, 0.1, n_samples),
        'pressure': np.random.normal(100, 15, n_samples),
        'rpm': np.random.normal(1500, 100, n_samples),
        'usage_hours': np.random.uniform(0, 10000, n_samples),
        'failure': np.zeros(n_samples)
    }
    df = pd.DataFrame(data)
    
    # Introduce failures for high temp/vibration
    df.loc[(df['temperature'] > 90) | (df['vibration'] > 0.8), 'failure'] = 1
    
    df.to_csv(f"{DATA_DIR}/maintenance.csv", index=False)
    return df

def generate_qc_data(n_samples=100):
    print("Generating QC Mock Images...")
    images = []
    labels = []
    
    for i in range(n_samples):
        # Generate random noise image
        img = np.random.rand(128, 128, 3)
        label = 0
        
        # Add "defect" (bright spot)
        if np.random.rand() > 0.5:
            img[50:60, 50:60, :] = 1.0
            label = 1
            
        images.append(img)
        labels.append(label)
        
    return np.array(images), np.array(labels)

def generate_financial_data(n_samples=1000):
    print("Generating Financial Data...")
    data = {
        'amount': np.random.exponential(100, n_samples),
        'hour': np.random.randint(0, 24, n_samples),
        'category_encoded': np.random.randint(0, 5, n_samples),
        'is_weekend': np.random.choice([0, 1], n_samples)
    }
    df = pd.DataFrame(data)
    
    # Introduce anomalies
    anomalies = pd.DataFrame({
        'amount': np.random.uniform(1000, 5000, 20),
        'hour': np.random.randint(0, 4, 20), # Late night
        'category_encoded': np.random.randint(0, 5, 20),
        'is_weekend': 1
    })
    
    df = pd.concat([df, anomalies])
    df.to_csv(f"{DATA_DIR}/transactions.csv", index=False)
    return df

def generate_cashflow_data(n_days=365):
    print("Generating Cash Flow Data...")
    dates = pd.date_range(start='2023-01-01', periods=n_days)
    
    # Trend + Seasonality + Noise
    trend = np.linspace(1000, 2000, n_days)
    seasonality = 500 * np.sin(np.linspace(0, 3.14 * 10, n_days))
    noise = np.random.normal(0, 200, n_days)
    
    net_cash_flow = trend + seasonality + noise
    
    df = pd.DataFrame({'date': dates, 'net_cash_flow': net_cash_flow})
    df.to_csv(f"{DATA_DIR}/cashflow.csv", index=False)
    return df

def main():
    # 1. Train Maintenance Model
    m_data = generate_maintenance_data()
    m_model = PredictiveMaintenanceModel()
    print("Training Maintenance Model...")
    print(m_model.train(m_data))
    
    # 2. Train QC Model
    qc_images, qc_labels = generate_qc_data()
    qc_model = QualityControlModel()
    print("Training QC Model...")
    qc_model.train(qc_images, qc_labels, epochs=2)
    
    # 3. Train Anomaly Detector
    f_data = generate_financial_data()
    ad_model = AnomalyDetector()
    print("Training Anomaly Detector...")
    print(ad_model.train(f_data))
    
    # 4. Train Cash Flow Predictor
    cf_data = generate_cashflow_data()
    cf_model = CashFlowPredictor()
    print("Training Cash Flow Predictor...")
    print(cf_model.train(cf_data))
    
    print("\nAll models trained and saved to 'models/' directory.")

if __name__ == "__main__":
    main()
