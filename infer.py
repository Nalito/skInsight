# !pip install -r reqiurements.txt

import warnings
warnings.filterwarnings('ignore')
import tensorflow
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Load the TensorFlow model
model = tensorflow.keras.models.load_model('model.h5') 

# Define class names (adjust based on your model's classes)
class_names = ['Eczema', 'Folliculitis', 'Insect Bite', 'Tinea', 'Urticaria']  

# Function to preprocess the input image
def preprocess_image(image, target_size=(224, 224)):
    image = image.resize(target_size)
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    image_array /= 255.0  # Normalize to [0, 1]
    return image_array


def predict(image_path):
    # Simulate a prediction for demonstration
    class_names = ['Eczema', 'Folliculitis', 'Insect Bite', 'Tinea', 'Urticaria']
    processed_image = preprocess_image(image)
        
    # Make prediction
    prediction = model.predict(processed_image)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)
    return predicted_class, confidence

print("")
print("--------------------")
print("Welcome to skInsight.")

is_quit = 0
while is_quit!=1:
    print("--------------------")
    print(" ")
    im_path = input("Enter in the image path: ")
    image = Image.open(im_path)

        
    # Make prediction
    predicted_class, confidence = predict(image)
    print("--------------------")
    print(" ")
    print(f'Model detected {predicted_class} with probability of {confidence*100:.2f}%')
    print("")
    print("--------------------")
    print(" ")
    is_quit = int(input("Enter 1 to quit, press 2 to make another prediction: "))

print("Done")