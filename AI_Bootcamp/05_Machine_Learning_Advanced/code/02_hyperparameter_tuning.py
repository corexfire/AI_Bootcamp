from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def main():
    print("=== Hyperparameter Tuning with Grid Search ===\n")

    # Load Data
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

    # Define Model
    rf = RandomForestClassifier(random_state=42)

    # Define Parameter Grid
    param_grid = {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }
    print(f"Tuning Parameters: {param_grid}")

    # Setup Grid Search
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1)
    
    # Run Search
    print("\nStarting Grid Search...")
    grid_search.fit(X_train, y_train)

    # Results
    print("\n--- Results ---")
    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Best CV Score: {grid_search.best_score_:.4f}")
    
    # Evaluate Best Model
    best_model = grid_search.best_estimator_
    test_acc = best_model.score(X_test, y_test)
    print(f"Test Set Accuracy: {test_acc:.4f}")

if __name__ == "__main__":
    main()
