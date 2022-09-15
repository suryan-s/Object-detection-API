"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import json,jsonify
from flask import Response,request,abort,render_template
from flask_cors import CORS
from flask_api import FlaskAPI

app = FlaskAPI(__name__)
CORS(app)
@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
