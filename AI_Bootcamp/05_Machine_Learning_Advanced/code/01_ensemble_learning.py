from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    print("=== Ensemble Learning Demo (Random Forest & GBM) ===\n")
    
    # 1. Load Data
    data = load_wine()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    print(f"Dataset: Wine Quality ({len(X)} samples)")

    # 2. Random Forest
    print("\nTraining Random Forest...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_pred)
    print(f"Random Forest Accuracy: {rf_acc:.4f}")

    # 3. Gradient Boosting
    print("\nTraining Gradient Boosting...")
    gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
    gb_model.fit(X_train, y_train)
    gb_pred = gb_model.predict(X_test)
    gb_acc = accuracy_score(y_test, gb_pred)
    print(f"Gradient Boosting Accuracy: {gb_acc:.4f}")

    # 4. Feature Importance (RF)
    print("\nTop 3 Important Features (RF):")
    importances = rf_model.feature_importances_
    indices = importances.argsort()[::-1]
    for i in range(3):
        print(f"{i+1}. {data.feature_names[indices[i]]} ({importances[indices[i]]:.4f})")

if __name__ == "__main__":
    main()
