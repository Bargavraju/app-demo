import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Application CI/CD!"


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    app.run(host=host, port=port)
