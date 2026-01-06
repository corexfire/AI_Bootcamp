import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

def main():
    print("=== Artificial Neural Network (ANN) Demo ===\n")

    # 1. Generate Non-Linear Data (Circles)
    # Data ini sulit dipisahkan oleh Linear Regression/Logistic Regression biasa
    X, y = make_circles(n_samples=1000, noise=0.03, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 2. Build Model
    # Input Layer -> Hidden Layer (10 neurons, ReLU) -> Output Layer (1 neuron, Sigmoid)
    model = Sequential([
        Dense(10, activation='relu', input_shape=(2,)), # Hidden Layer 1
        Dense(10, activation='relu'),                   # Hidden Layer 2
        Dense(1, activation='sigmoid')                  # Output Layer (Binary Classification)
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    print("Model Architecture:")
    model.summary()

    # 3. Train Model
    print("\nTraining Model...")
    history = model.fit(X_train, y_train, epochs=20, verbose=1, validation_split=0.2)

    # 4. Evaluate
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"\nTest Accuracy: {accuracy:.4f}")

    # 5. Visualize Training History
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.title('Training Loss')
    plt.legend()
    # plt.show()
    print("Loss plot generated.")

if __name__ == "__main__":
    main()
