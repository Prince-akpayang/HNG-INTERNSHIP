# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L9F-IT0H-2v-IlXStiFo8CkmwoCY40MO
"""

!pip install flask flask-cors

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define the API endpoint
@app.route('/', methods=['GET'])
def get_info():
    # Get the current datetime in ISO 8601 format (UTC)
    current_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Return the JSON response
    return jsonify({
        "email": "princeakpayang@gmail.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/Prince-akpayang/HNG-INTERNSHIP"
    })

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
