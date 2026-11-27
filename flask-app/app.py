import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "service": "Python Flask Service",
        "status": "running",
        "port": 5000,
        "db_host": os.getenv("DB_HOST", "db"),
        "db_name": os.getenv("DB_NAME", "laravel_db")
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)