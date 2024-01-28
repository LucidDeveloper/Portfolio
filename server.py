# server.py is the entry point for the application.
# Run this file to start the server.

from flask_app import app

# Controllers act as servers for each distinct model and respective templates within the app
from flask_app.controllers import great_number_game, portfolio, users_sqlite_controller

if __name__ == '__main__':
    app.run(debug=True)