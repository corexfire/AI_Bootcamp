import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

class PredictiveMaintenanceModel:
    def __init__(self, model_path="models/maintenance_model.joblib"):
        self.model_path = model_path
        self.model = None
        self.features = ['temperature', 'vibration', 'pressure', 'rpm', 'usage_hours']

    def train(self, data: pd.DataFrame):
        """
        Train the model using sensor data.
        Target column should be 'failure' (0 or 1).
        """
        X = data[self.features]
        y = data['failure']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        self.save_model()
        return report

    def predict(self, sensor_data: dict):
        """
        Predict failure probability.
        """
        if not self.model:
            self.load_model()
        
        df = pd.DataFrame([sensor_data])
        # Ensure correct order of columns
        df = df[self.features]
        
        prediction = self.model.predict(df)[0]
        probability = self.model.predict_proba(df)[0][1]
        
        return {
            "prediction": int(prediction),
            "failure_probability": float(probability),
            "status": "Maintenance Required" if prediction == 1 else "Healthy"
        }

    def save_model(self):
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)

    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            raise FileNotFoundError("Model not found. Please train the model first.")
