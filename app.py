from flask import Flask, request, jsonify
from prediction import FruitPredictor
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from PIL import Image

# Initialize Flask app and FruitPredictor
app = Flask(__name__)
CORS(app)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize the predictor with your model and training data
predictor = FruitPredictor(model_path='models/best_model.keras', train_dir='fruit_dataset/Train')

# Helper function to check allowed file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Now, we pass the file path directly to FruitPredictor.predict()
            predicted_class = predictor.predict(filepath)
            print(predicted_class)

            # Return the result as JSON
            return jsonify({"predicted_class": predicted_class})

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
