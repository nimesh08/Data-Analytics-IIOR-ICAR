"""Optional Flask server for the Oilseed Atlas static portfolio demo."""
from pathlib import Path
from flask import Flask, send_from_directory

ROOT = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)

@app.get('/')
def index():
    return send_from_directory(ROOT, 'index.html')

@app.get('/<path:filename>')
def asset(filename):
    if filename not in {'style.css', 'app.js'}:
        return 'Not found', 404
    return send_from_directory(ROOT, filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
