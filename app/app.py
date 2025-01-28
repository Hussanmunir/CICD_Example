# app.py - This file contains the main Flask application code.

# Import the Flask class from the flask module
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define the root route of the app
@app.route("/")
def home():
    # This is the response when accessing the root URL
    return "Hello, Welcome to my CI/CD Pipeline!"

# Check if the script is run directly
if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True)
