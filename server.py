"""Simple Flask server to serve the landing page."""
import os

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    """Serve the landing page."""
    return send_from_directory("static", "landing.html")


if __name__ == "__main__":
    # Start the server on port 8000
    print("Starting server on http://localhost:8000")
    app.run(host="0.0.0.0", port=8000, debug=True)
