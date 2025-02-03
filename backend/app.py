from flask import Flask
from flask_cors import CORS
import flask
import json
from pathlib import Path

# Notes
# Activate venv with: source ./venv/bin/activate
# Run with: python3 app.py

#Variables
serverName = "hsBackend"
dataFolder = Path("data")

# Define Server
app = Flask(serverName)
CORS(app)

# Routes
@app.route("/")
def index():
    return "<h1>Home Server Backend</h1>"

@app.route('/recipes', methods=["GET"])
def recipes():
    print("recipes endpoint reached...")
    with open(dataFolder / "data-recipes.json", "r") as f:
        data = json.load(f)
        return flask.jsonify(data)

# Start Server
if serverName == "hsBackend":
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    app.run("localhost", 5000)
