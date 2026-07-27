from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "app": "k8s-assignment",
        "env": os.getenv("APP_ENV")
    }

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
