import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import os

class QualityControlModel:
    def __init__(self, model_path="models/qc_model.h5"):
        self.model_path = model_path
        self.model = None
        self.img_size = (128, 128)

    def build_model(self):
        model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(1, activation='sigmoid') # Binary classification: Defect (1) vs Good (0)
        ])
        
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        self.model = model

    def train(self, train_images, train_labels, epochs=5):
        if self.model is None:
            self.build_model()
            
        history = self.model.fit(train_images, train_labels, epochs=epochs, validation_split=0.2)
        self.save_model()
        return history.history

    def predict(self, image_path: str):
        if self.model is None:
            self.load_model()
            
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image could not be read")
            
        img = cv2.resize(img, self.img_size)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        
        prediction = self.model.predict(img)[0][0]
        
        return {
            "defect_probability": float(prediction),
            "is_defective": bool(prediction > 0.5),
            "status": "Defective" if prediction > 0.5 else "Passed"
        }

    def save_model(self):
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        self.model.save(self.model_path)

    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = tf.keras.models.load_model(self.model_path)
        else:
            # If no model exists, build a new one (for demonstration purposes if loading fails)
            self.build_model()
