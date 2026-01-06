import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

class HousePricePredictor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = None
        self.X_test = None
        self.y_test = None
        self.y_pred = None

    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError("Dataset not found")
        
        df = pd.read_csv(self.data_path)
        print("Data Loaded:")
        print(df.head())
        
        # Features (X) & Target (y)
        X = df[['Area', 'Bedrooms', 'Age', 'Location_Score']]
        y = df['Price']
        return X, y

    def train(self):
        X, y = self.load_data()
        
        # Split Data
        X_train, self.X_test, y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Init & Train Model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        print("\nModel Trained Successfully.")
        print(f"Intercept: {self.model.intercept_}")
        print(f"Coefficients: {self.model.coef_}")

    def evaluate(self):
        if not self.model:
            print("Model not trained yet.")
            return

        self.y_pred = self.model.predict(self.X_test)
        
        mae = mean_absolute_error(self.y_test, self.y_pred)
        rmse = np.sqrt(mean_squared_error(self.y_test, self.y_pred))
        r2 = r2_score(self.y_test, self.y_pred)
        
        print("\n=== Model Evaluation ===")
        print(f"MAE (Mean Absolute Error): {mae:.2f}")
        print(f"RMSE (Root Mean Squared Error): {rmse:.2f}")
        print(f"R2 Score: {r2:.2f}")

    def predict_new(self, area, bedrooms, age, loc_score):
        if not self.model:
            print("Model not trained.")
            return
        
        input_data = pd.DataFrame([[area, bedrooms, age, loc_score]], 
                                columns=['Area', 'Bedrooms', 'Age', 'Location_Score'])
        price = self.model.predict(input_data)[0]
        print(f"\nPrediction for House [Area={area}, Bed={bedrooms}, Age={age}, Loc={loc_score}]:")
        print(f"Estimated Price: {price:.2f} Million IDR")

    def save_plot(self):
        if self.y_pred is None: return
        
        plt.figure(figsize=(8, 6))
        plt.scatter(self.y_test, self.y_pred, color='blue')
        plt.plot([self.y_test.min(), self.y_test.max()], [self.y_test.min(), self.y_test.max()], 'k--', lw=2)
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.title('Actual vs Predicted Prices')
        plt.savefig('prediction_plot.png')
        print("Saved plot to prediction_plot.png")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'housing.csv')
    
    predictor = HousePricePredictor(data_path)
    predictor.train()
    predictor.evaluate()
    predictor.save_plot()
    
    # Test Prediction
    predictor.predict_new(160, 3, 5, 8)

if __name__ == "__main__":
    main()
