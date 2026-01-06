from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib
import os

class AnomalyDetector:
    def __init__(self, model_path="models/financial_anomaly_model.joblib"):
        self.model_path = model_path
        self.model = None
        self.features = ['amount', 'hour', 'category_encoded', 'is_weekend']

    def train(self, transactions: pd.DataFrame):
        """
        Train Isolation Forest on normal transactions.
        """
        X = transactions[self.features]
        
        # Contamination is the proportion of outliers in the data set
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.model.fit(X)
        
        self.save_model()
        return {"status": "Model trained successfully"}

    def detect(self, transaction: dict):
        if not self.model:
            self.load_model()
            
        df = pd.DataFrame([transaction])
        df = df[self.features]
        
        # Predict returns -1 for outlier, 1 for inlier
        prediction = self.model.predict(df)[0]
        score = self.model.decision_function(df)[0]
        
        return {
            "is_anomaly": bool(prediction == -1),
            "anomaly_score": float(score),
            "risk_level": "High" if score < -0.2 else ("Medium" if score < 0 else "Low")
        }

    def save_model(self):
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)

    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            raise FileNotFoundError("Model not found")
