import numpy as np

def main():
    print("=== Aljabar Linear dengan NumPy ===\n")

    # 1. Vectors (1D Array)
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    print(f"Vector v1: {v1}")
    print(f"Vector v2: {v2}")

    # Operasi Vector
    print(f"Penjumlahan (v1 + v2): {v1 + v2}")
    print(f"Dot Product (v1 . v2): {np.dot(v1, v2)}") # 1*4 + 2*5 + 3*6 = 32

    # 2. Matrix (2D Array)
    print("\n--- Matrix ---")
    A = np.array([
        [1, 2],
        [3, 4]
    ])
    B = np.array([
        [5, 6],
        [7, 8]
    ])
    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")

    # Operasi Matrix
    print(f"Perkalian Matrix (A @ B):\n{A @ B}")
    print(f"Transpose A:\n{A.T}")

    # 3. Broadcasting
    print("\n--- Broadcasting ---")
    # Menambahkan scalar ke seluruh elemen matrix
    print(f"A + 10:\n{A + 10}")

    # 4. Shape & Reshape
    print("\n--- Shape Manipulation ---")
    C = np.arange(9) # [0, 1, ..., 8]
    print(f"Original C: {C}")
    C_reshaped = C.reshape(3, 3)
    print(f"Reshaped C (3x3):\n{C_reshaped}")

if __name__ == "__main__":
    main()
