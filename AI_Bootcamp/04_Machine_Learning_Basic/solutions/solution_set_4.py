from sklearn.datasets import load_breast_cancer, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import numpy as np

def solve_theory():
    print("--- Soal 1 & 2 & 5 (Theory) ---")
    print("1. Supervised: Data berlabel (Contoh: Spam Filter). Unsupervised: Data tanpa label (Contoh: Customer Segmentation).")
    print("2. Train-Test Split penting untuk mengevaluasi performa model pada data yang belum pernah dilihat (Generalisasi). Jika diuji dengan data train, terjadi Overfitting.")
    print("5. Recall lebih penting pada Fraud Detection. Kita ingin meminimalkan False Negative (transaksi curang yang dianggap aman).")

def solve_logistic_regression():
    print("\n--- Soal 3: Logistic Regression ---")
    # 1. Load Data
    data = load_breast_cancer()
    X = data.data
    y = data.target
    
    # 2. Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Train
    model = LogisticRegression(max_iter=3000) # Increased max_iter for convergence
    model.fit(X_train, y_train)
    
    # 4. Accuracy
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Breast Cancer Model Accuracy: {acc:.4f}")

def solve_kmeans():
    print("\n--- Soal 4: K-Means ---")
    # 1. Generate Data
    X, _ = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)
    
    # 2. Clustering
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans.fit(X)
    
    # 3. Centroids
    centroids = kmeans.cluster_centers_
    print("Cluster Centroids Found:")
    print(centroids)

if __name__ == "__main__":
    solve_theory()
    solve_logistic_regression()
    solve_kmeans()
