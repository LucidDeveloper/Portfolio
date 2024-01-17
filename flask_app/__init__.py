from flask import Flask
from flask_app.config.env import KEY


app = Flask(__name__)
app.secret_key = KEY