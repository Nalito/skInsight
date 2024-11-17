from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import os

# Load the TensorFlow model
model = tf.keras.models.load_model('model.h5')  # Replace with your .h5 file
class_names = ['Eczema', 'Folliculitis', 'Insect Bite', 'Tinea', 'Urticaria']  # Replace with your actual class names

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to preprocess the input image
def preprocess_image(image, target_size=(224, 224)):
    image = image.resize(target_size)
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    image_array /= 255.0  # Normalize to [0, 1]
    return image_array

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']
        if file:
            # Save the uploaded image
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            # Preprocess the image
            image = Image.open(image_path)
            processed_image = preprocess_image(image)

            # Make prediction
            prediction = model.predict(processed_image)
            predicted_class = class_names[np.argmax(prediction)]
            confidence = np.max(prediction)

            # Render the result
            return render_template('index.html', image_path=image_path, prediction=predicted_class, confidence=f"{confidence:.2f}")

    return render_template('index.html', image_path=None)

if __name__ == '__main__':
    # Create upload folder if not exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
