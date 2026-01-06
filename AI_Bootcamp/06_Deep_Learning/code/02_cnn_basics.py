import tensorflow as tf
from tensorflow.keras import layers, models

def main():
    print("=== Convolutional Neural Network (CNN) Architecture Demo ===\n")
    
    # Membuat arsitektur CNN sederhana untuk klasifikasi gambar (misal ukuran 28x28)
    model = models.Sequential()
    
    # 1. Feature Extraction (Convolution + Pooling)
    # Conv2D: Mendeteksi fitur (tepi, tekstur, pola)
    # MaxPooling2D: Mengurangi dimensi spatial (downsampling)
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    
    # 2. Classification (Flatten + Dense)
    model.add(layers.Flatten()) # Mengubah 2D/3D array menjadi 1D vector
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax')) # Output layer (misal 10 kelas digit)
    
    print("CNN Architecture Summary:")
    model.summary()
    
    print("\nPenjelasan Layer:")
    print("1. Conv2D: Melakukan filter konvolusi untuk mengekstrak fitur visual.")
    print("2. MaxPooling2D: Mengambil nilai maksimal dari area tertentu, mengurangi ukuran gambar.")
    print("3. Flatten: Meratakan hasil ekstraksi fitur menjadi satu vektor panjang.")
    print("4. Dense: Fully Connected Layer untuk klasifikasi akhir.")

if __name__ == "__main__":
    main()
