from flask_app.config.env import KEY
from flask import Flask

app = Flask(__name__)
app.secret_key = KEY