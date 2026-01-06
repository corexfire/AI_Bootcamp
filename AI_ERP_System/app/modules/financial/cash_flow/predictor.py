from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import joblib
import os

class CashFlowPredictor:
    def __init__(self, model_path="models/cashflow_model.joblib"):
        self.model_path = model_path
        self.model = None

    def train(self, data: pd.DataFrame):
        """
        Data should have 'date' and 'net_cash_flow'.
        We will feature engineer: day of month, month, lagged values.
        """
        df = data.copy()
        df['date'] = pd.to_datetime(df['date'])
        df['day'] = df['date'].dt.day
        df['month'] = df['date'].dt.month
        df['day_of_week'] = df['date'].dt.dayofweek
        
        # Create lag features (previous day cash flow)
        df['lag_1'] = df['net_cash_flow'].shift(1)
        df['lag_7'] = df['net_cash_flow'].shift(7)
        
        df = df.dropna()
        
        features = ['day', 'month', 'day_of_week', 'lag_1', 'lag_7']
        X = df[features]
        y = df['net_cash_flow']
        
        self.model = LinearRegression()
        self.model.fit(X, y)
        
        self.save_model()
        return {"score": self.model.score(X, y)}

    def predict_next_day(self, last_day_data: dict):
        """
        Predict next day cash flow.
        Requires: last_day_cash_flow, cash_flow_7_days_ago, date_to_predict
        """
        if not self.model:
            self.load_model()
            
        date = pd.to_datetime(last_day_data['date'])
        
        features = pd.DataFrame([{
            'day': date.day,
            'month': date.month,
            'day_of_week': date.dayofweek,
            'lag_1': last_day_data['lag_1'],
            'lag_7': last_day_data['lag_7']
        }])
        
        prediction = self.model.predict(features)[0]
        
        return {
            "predicted_cash_flow": float(prediction),
            "date": str(date.date())
        }

    def save_model(self):
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)

    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            raise FileNotFoundError("Model not found")
