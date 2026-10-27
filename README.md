# Image Recognition with Ollama (LLaVA)

A Flask upload form that asks Ollama's `llava` model to describe an image. [app.py](app.py) saves the upload temporarily, sends its base64-encoded bytes to Ollama and renders the returned text. The page displays the filename and description, not an image preview.

## Prerequisites

- Python and a virtual environment compatible with the installed Flask, Ollama Python client and Werkzeug versions. [requirements.txt](requirements.txt) is unpinned; a Python 3.7 compatibility claim is not validated.
- [Ollama](https://ollama.com/) installed and its service available.
- The `llava` model available to that service. If needed, download it with `ollama pull llava`; this is a model download, not part of installing the Python requirements.

The code calls `ollama.chat(model='llava', ...)`. Using another model requires a code change. Verify that the client's configured Ollama endpoint is the intended local service before uploading an image.

## Setup

```bash
git clone https://github.com/Zinga18018/ollama-image-recognition-tool.git
cd ollama-image-recognition-tool
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For Windows PowerShell, replace the activation line with `.\.venv\Scripts\Activate.ps1`.

If Ollama is not already running, start `ollama serve` in another terminal. Then use the [Flask development CLI](https://flask.palletsprojects.com/en/stable/cli/) on loopback, with the debugger and reloader disabled:

```bash
python -m flask --app app run --host 127.0.0.1 --port 5000 --no-debugger --no-reload
```

Open `http://127.0.0.1:5000/`, choose a PNG, JPG/JPEG or GIF and click **Get Description**. If the service or model is unavailable, the app displays an error. Setup, service/model calls and browser flows were not rerun for this documentation update.

## Storage, safety and limits

- `python app.py` instead starts debug mode on `0.0.0.0`. Do not expose that entry point to a network. The application has no authentication; even the loopback development command is not a production deployment.
- Uploads are limited to 16 MiB. File checks use the filename extension, not decoded-image validation.
- The app creates `uploads/` in its working directory. It attempts deletion after success or a caught error, but a process crash can leave files behind. Repeated/concurrent uploads with the same sanitized filename can collide.
- [templates/index.html](templates/index.html) loads frontend assets from external CDNs. Local model inference does not make the whole browser session offline.
- Descriptions can be inaccurate or omit details. No caption-quality evaluation, performance benchmark or automated test suite is committed.

Use non-sensitive images with appropriate permissions. Public deployment, stronger file handling and resource limits require separate code work.

