import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image

# Load the TensorFlow model
model = tf.keras.models.load_model('model.h5') 

# Define class names (adjust based on your model's classes)
class_names = ['Eczema', 'Folliculitis', 'Insect Bite', 'Tinea', 'Urticaria']  

# Function to preprocess the input image
def preprocess_image(image, target_size=(224, 224)):
    image = image.resize(target_size)
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    image_array /= 255.0  # Normalize to [0, 1]
    return image_array

# Streamlit app
st.title("Skin Defect Detection")
logo = Image.open("logo.png")
st.image(logo)

# File uploader for user to input an image
uploaded_file = st.file_uploader("Upload an image of the skin defect", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess the image
    processed_image = preprocess_image(image)
    
    # Make prediction
    prediction = model.predict(processed_image)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)
    
    # Display the result
    st.write(f"### Prediction: {predicted_class}")
    st.write(f"### Confidence: {confidence:.2f}")


if __name__ == '__main__':     
    st.set_option('server.enableCORS', True) 
