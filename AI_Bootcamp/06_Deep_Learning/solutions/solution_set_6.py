import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

def solve_theory():
    print("--- Theory Answers ---")
    print("1. ReLU: Untuk hidden layer (cepat, mengatasi vanishing gradient). Sigmoid: Output layer binary classification (0-1). Softmax: Output layer multi-class classification (probabilitas total 1).")
    print("2. Mengatasi Overfitting: Dropout, L1/L2 Regularization, Early Stopping, Data Augmentation.")
    print("3. Kernel: Matriks bobot untuk ekstraksi fitur. Stride: Langkah pergeseran filter. Output size: (Input - Filter + 1) / Stride. (5-3+1)/1 = 3x3.")
    print("5. Epoch: Satu putaran penuh seluruh dataset. Batch Size: Jumlah data yang diproses sebelum update bobot. Steps: 1000 / 100 = 10 steps per epoch.")

def solve_coding_challenge():
    print("\n--- Soal 4: MLP Regression ---")
    # 1. Generate Dummy Data
    X = np.random.rand(100, 5)
    y = np.random.rand(100, 1) # Target kontinu
    
    # 2. Build Model
    model = Sequential([
        Dense(16, activation='relu', input_shape=(5,)),
        Dense(8, activation='relu'),
        Dense(1) # Linear activation (default) for regression
    ])
    
    model.compile(optimizer='adam', loss='mse')
    
    # 3. Train
    print("Training Regression Model...")
    history = model.fit(X, y, epochs=5, verbose=0)
    print(f"Final Loss (MSE): {history.history['loss'][-1]:.4f}")

if __name__ == "__main__":
    solve_theory()
    solve_coding_challenge()
