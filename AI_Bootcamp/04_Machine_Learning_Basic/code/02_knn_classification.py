import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    print("=== KNN Classification Demo (Iris Dataset) ===\n")

    # 1. Load Dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    print(f"Features: {iris.feature_names}")
    print(f"Target Classes: {iris.target_names}")
    print(f"Data Shape: {X.shape}")

    # 2. Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 3. Train Model (K-Nearest Neighbors)
    k = 3
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    print(f"\nTraining KNN with k={k}...")

    # 4. Predict & Evaluate
    y_pred = knn.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {acc:.2f} ({acc*100}%)")

    print("\n--- Classification Report ---")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    print("\n--- Confusion Matrix ---")
    print(confusion_matrix(y_test, y_pred))

    # 5. Predict New Data
    new_data = np.array([[5.1, 3.5, 1.4, 0.2]]) # Sepal Length, Sepal Width, Petal Length, Petal Width
    prediction = knn.predict(new_data)
    print(f"\nNew Flower Prediction {new_data}: {iris.target_names[prediction][0]}")

if __name__ == "__main__":
    main()
