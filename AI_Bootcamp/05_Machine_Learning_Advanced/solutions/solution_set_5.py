from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def solve_theory():
    print("--- Theory Answers ---")
    print("1. Bagging (Parallel): Melatih banyak model secara independen lalu voting (mengurangi variance). Boosting (Sequential): Melatih model secara berurutan untuk memperbaiki kesalahan model sebelumnya (mengurangi bias). Boosting lebih rentan overfitting.")
    print("2. K-Fold CV membagi data menjadi K bagian dan melatih model K kali. Ini memberikan estimasi performa yang lebih stabil dan tidak bias pada potongan data tertentu.")
    print("3. Artinya 'Umur' adalah fitur yang paling banyak mengurangi ketidakmurnian (impurity) saat membuat pohon keputusan. Ini korelasi kuat, belum tentu kausalitas.")
    print("5. Untuk mengurangi overfitting XGBoost: Kurangi `max_depth`, kurangi `n_estimators` (atau early stopping), naikkan `min_child_weight`, naikkan `gamma` atau `lambda` (regularization).")

def solve_coding_challenge():
    print("\n--- Soal 4: Model Comparison ---")
    # 1. Load & Split
    digits = load_digits()
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
    
    # 2. Decision Tree
    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, y_train)
    dt_acc = accuracy_score(y_test, dt.predict(X_test))
    
    # 3. Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    rf_acc = accuracy_score(y_test, rf.predict(X_test))
    
    print(f"Decision Tree Accuracy: {dt_acc:.4f}")
    print(f"Random Forest Accuracy: {rf_acc:.4f}")
    
    if rf_acc > dt_acc:
        print("Conclusion: Random Forest performs better (Ensemble effect).")
    else:
        print("Conclusion: Performance is similar.")

if __name__ == "__main__":
    solve_theory()
    solve_coding_challenge()
