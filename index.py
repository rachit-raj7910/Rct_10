from flask import Flask, render_template_string, request, jsonify
import random
from collections import OrderedDict
import pandas as pd

# --- Flask App Initialization ---
app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# --- IMPORTANT ---
# Vercel expects a handler function.
def handler(request, *args, **kwargs):
    return app(request.environ, request.start_response)
