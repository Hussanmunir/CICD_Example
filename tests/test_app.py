# test_app.py - This file contains unit tests for the Flask app.

import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the app instance from the app module
from app.app import app

# Test the home route of the Flask app
def test_home():
    # Enable testing mode
    app.testing = True
    client = app.test_client()

    # Send a GET request to the root URL
    response = client.get("/")
    
    # Check if the response status is 200 (OK)
    assert response.status_code == 200
    # Check if the response data is correct
    assert response.data == b"Hello, Heroku CI/CD!"

# pytest -v -p no:warnings