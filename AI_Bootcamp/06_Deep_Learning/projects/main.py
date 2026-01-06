import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
import os

class FashionClassifier:
    def __init__(self):
        self.model = None
        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                            'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def load_data(self):
        print("Loading Fashion MNIST dataset...")
        # Download dataset (otomatis disimpan di ~/.keras/datasets)
        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
        
        # Normalisasi pixel value (0-255 -> 0-1)
        train_images = train_images / 255.0
        test_images = test_images / 255.0
        
        # Reshape agar sesuai input CNN (28, 28, 1)
        self.train_images = train_images.reshape((-1, 28, 28, 1))
        self.test_images = test_images.reshape((-1, 28, 28, 1))
        self.train_labels = train_labels
        self.test_labels = test_labels
        
        print(f"Training Data: {self.train_images.shape}")
        print(f"Test Data: {self.test_images.shape}")

    def build_model(self):
        print("\nBuilding CNN Model...")
        self.model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.3), # Mencegah overfitting
            layers.Dense(10, activation='softmax')
        ])
        
        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])
        self.model.summary()

    def train(self, epochs=5):
        print(f"\nTraining for {epochs} epochs...")
        self.history = self.model.fit(self.train_images, self.train_labels, epochs=epochs, 
                                      validation_data=(self.test_images, self.test_labels))

    def evaluate(self):
        print("\nEvaluating Model...")
        test_loss, test_acc = self.model.evaluate(self.test_images, self.test_labels, verbose=2)
        print(f"Test accuracy: {test_acc:.4f}")

    def predict_sample(self):
        print("\nPredicting sample images...")
        predictions = self.model.predict(self.test_images[:5])
        
        for i in range(5):
            pred_label = np.argmax(predictions[i])
            true_label = self.test_labels[i]
            print(f"Image {i+1}: Pred={self.class_names[pred_label]} ({np.max(predictions[i]):.2f}), True={self.class_names[true_label]}")

    def save_model(self):
        self.model.save('fashion_model.h5')
        print("\nModel saved to fashion_model.h5")

def main():
    classifier = FashionClassifier()
    classifier.load_data()
    classifier.build_model()
    classifier.train(epochs=3) # Menggunakan 3 epoch agar cepat demo-nya
    classifier.evaluate()
    classifier.predict_sample()
    classifier.save_model()

if __name__ == "__main__":
    main()
