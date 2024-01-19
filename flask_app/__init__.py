# Initializes the Flask app
# Import the Flask class from the flask module
from flask import Flask

# KEY is the secret key for the Flask app
from flask_app.config.env import KEY

# App is the Flask app object
app = Flask(__name__)
app.secret_key = KEY