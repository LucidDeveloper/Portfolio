from flask_app.__init__ import app
from flask_app.controllers import controller
# Controllers act as servers for each distinct model within the app
# Models are classes which interact with the MySQL Database in order to Create an Object Oriented Relational Database System

if __name__ == "__main__":
    app.run(debug=True)