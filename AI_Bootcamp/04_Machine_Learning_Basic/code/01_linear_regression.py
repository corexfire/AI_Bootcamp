import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def main():
    print("=== Linear Regression Demo ===\n")

    # 1. Generate Dummy Data
    # X: Ukuran rumah (m2), y: Harga rumah (juta)
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1) * 100 # 0 - 200 m2
    y = 4 + 3 * X + np.random.randn(100, 1) * 20 # Linear relation with noise

    # 2. Split Data (Train 80% - Test 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training Data: {len(X_train)} samples")
    print(f"Testing Data: {len(X_test)} samples")

    # 3. Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    print("\nTraining complete.")
    print(f"Coefficient (Slope): {model.coef_[0][0]:.2f}")
    print(f"Intercept: {model.intercept_[0]:.2f}")
    # Persamaan: y = 3x + 4

    # 4. Evaluate Model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n--- Evaluation ---")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R2 Score: {r2:.2f}")

    # 5. Visualization
    plt.scatter(X_test, y_test, color='black', label='Actual Data')
    plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Prediction')
    plt.xlabel("Ukuran Rumah (m2)")
    plt.ylabel("Harga (Juta)")
    plt.title("Linear Regression: House Price Prediction")
    plt.legend()
    # plt.show()
    print("\nVisualization code executed (plot not shown in terminal).")

if __name__ == "__main__":
    main()
