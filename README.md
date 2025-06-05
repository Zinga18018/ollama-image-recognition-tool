# Image Recognition with Ollama (LLaVA)

This is a simple Flask web application that allows users to upload an image and get a description of it using a locally running Ollama instance with a multimodal model like LLaVA.

## Prerequisites

1.  **Python 3.7+**
2.  **Ollama Installed:** Download and install Ollama from [https://ollama.com/](https://ollama.com/).
3.  **Multimodal Model Pulled:** You need a multimodal model compatible with Ollama. This application is configured to use `llava` by default.
    *   Open your terminal and run: `ollama pull llava`
    *   If you wish to use a different model, update the `model` parameter in the `ollama.chat` call within `app.py`.

## Setup

1.  **Clone the repository (or download the files):**
    ```bash
    # If this were a git repo, you'd clone it.
    # For now, ensure you have app.py, requirements.txt, and the templates/index.html file.
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    Activate it:
    *   Windows: `venv\Scripts\activate`
    *   macOS/Linux: `source venv/bin/activate`

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ensure Ollama Server is Running:**
    Open a new terminal window/tab and start the Ollama server if it's not already running:
    ```bash
    ollama serve
    ```
    Keep this terminal window open while the application is running.

## Running the Application

1.  **Navigate to the project directory** in your terminal (where `app.py` is located).

2.  **Run the Flask application:**
    ```bash
    python app.py
    ```

3.  **Open your web browser** and go to: `http://127.0.0.1:5000/` or `http://localhost:5000/`

## How to Use

1.  Click on "Choose File" or "Browse" to select an image from your computer (supports .png, .jpg, .jpeg, .gif).
2.  Click the "Get Description" button.
3.  The application will upload the image, send it to your local Ollama instance, and display the description provided by the LLaVA model.

## Project Structure

```
Image_Recognition/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # HTML template for the web page
├── uploads/            # Directory for temporary image uploads (created automatically)
└── README.md           # This file
```

## Notes

*   The `uploads` directory is created automatically by `app.py` to temporarily store uploaded images. These images are deleted after processing.
*   The application uses base64 encoding to send the image data to Ollama. This is a common way to handle image data in API requests.
*   Error handling is basic. If Ollama is not running or the model is not available, an error message will be displayed.
*   The maximum upload size is set to 16MB in `app.py`.