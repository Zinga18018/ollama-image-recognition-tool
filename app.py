import os
import ollama
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # Encode image to base64
                with open(filepath, "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')

                # Interact with Ollama
                # Ensure you have a multimodal model like 'llava' pulled in Ollama
                # You can pull it using: `ollama pull llava`
                response = ollama.chat(
                    model='llava', # Or another multimodal model you have
                    messages=[
                        {
                            'role': 'user',
                            'content': 'Describe this image in detail:',
                            'images': [b64_string]
                        },
                    ]
                )
                description = response['message']['content']
                # Clean up the uploaded file after processing
                os.remove(filepath)
                return render_template('index.html', filename=filename, description=description)
            except Exception as e:
                # Clean up the uploaded file in case of error
                if os.path.exists(filepath):
                    os.remove(filepath)
                return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    # Make sure Ollama server is running.
    # You can start it by typing `ollama serve` in your terminal if it's not already running.
    print("Please ensure the Ollama server is running. You can start it with 'ollama serve'.")
    print("Also, ensure you have a multimodal model like 'llava' pulled: 'ollama pull llava'")
    app.run(debug=True, host='0.0.0.0', port=5000)