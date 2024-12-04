import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class FruitPredictor:
    def __init__(self, model_path, train_dir):
        self.model = load_model(model_path)
        self.class_labels = self._load_class_labels(train_dir)

    def _load_class_labels(self, train_dir):
        train_datagen = ImageDataGenerator(rescale=1.0 / 255.0)
        train_generator = train_datagen.flow_from_directory(
            train_dir, target_size=(224, 224), batch_size=32, class_mode='categorical'
        )
        return {v: k for k, v in train_generator.class_indices.items()}

    def predict(self, image_file):
        # Preprocess the image
        img = load_img(image_file, target_size=(224, 224))  # Replace with your input size
        img_array = img_to_array(img) / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction
        predictions = self.model.predict(img_array)
        predicted_class_index = np.argmax(predictions[0])
        return self.class_labels[predicted_class_index]
