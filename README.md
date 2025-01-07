# Fruit Classification and Health Benefits App

## Overview

This project is an AI-based application designed to classify fruit images and provide detailed health benefits of various fruits. The model has been trained using **MobileNetV2**, a lightweight deep learning architecture, on a dataset containing **58 classes of fruits**. The application allows users to either upload an image of a fruit or input its name directly. In both cases, the system will identify the fruit and present detailed health benefits associated with it.

The goal of this project is to create an interactive tool that helps users not only identify fruits but also understand their nutritional and health benefits.

## Features

- **Image Classification**: Upload a photo of a fruit, and the AI model identifies it.
- **Text-Based Search**: Type the name of a fruit to retrieve its health benefits instantly.
- **Health Benefits Information**: Each identified fruit displays a list of benefits, promoting better health awareness.
- **Show More**: Users can view additional health benefits if available for the identified fruit.

## Technical Flow

### Input
1. **Image Input**:
   - Users can upload fruit images in formats like **JPEG**, **PNG**, etc.
   - The image is resized to **224x224 pixels** and normalized (scaled to a range from 0 to 1) to be processed by the AI model.

2. **Text Input**:
   - Users can manually type the name of a fruit into a text box.
   - The application checks the typed fruit name against a predefined list to match the benefits.

### Processing

1. **For Image Input**:
   - **Preprocessing**: The image is resized and normalized to be compatible with the model input requirements.
   - **AI Model Prediction**:
     - The image is passed through the **MobileNetV2** model.
     - The model classifies the fruit and outputs a probability distribution across 58 fruit classes.
     - The fruit with the highest probability is selected as the prediction.

2. **For Text Input**:
   - The entered fruit name is checked against a predefined list of fruits.
   - If the name matches, the application retrieves and displays the health benefits.

### Output
1. **For Image Input**:
   - The fruit identified by the model is displayed.
   - Health benefits associated with the identified fruit are shown to the user.

2. **For Text Input**:
   - The health benefits of the fruit corresponding to the entered name are displayed.

3. **Show More**:
   - If more detailed benefits are available, users can click the "Show More" button to get additional health information.

## AI Model: MobileNetV2

The fruit classification is powered by **MobileNetV2**, a deep learning model designed for mobile and edge applications. It is lightweight and efficient, making it ideal for fruit image classification while maintaining accuracy. The model has been trained on a dataset of **58 fruit classes**, which allows the application to recognize a wide variety of fruits with high accuracy.

### Model Training Details:
- **Dataset**: A custom dataset of 58 different fruits.
- **Model**: MobileNetV2, chosen for its efficiency and suitability for mobile applications.
- **Preprocessing**: Images are resized to 224x224 pixels and normalized before feeding into the model.
- **Output**: The model outputs the fruit class with the highest probability.

## Technologies Used

- **AI Model**: MobileNetV2 (Pre-trained)
- **Programming Languages**: Python
- **Libraries**: TensorFlow, Keras, NumPy, OpenCV
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask or Django (depending on implementation choice)

## How to Use

1. **Upload an Image**: Click the "Upload" button and choose an image of a fruit. The model will classify the fruit and show you its benefits.
2. **Enter a Fruit Name**: Type the name of a fruit in the provided text box. The application will provide health benefits for that fruit.
