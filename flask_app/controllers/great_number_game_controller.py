# Controller file great_number_game_controller.py is the primary controller for the Great Number Game.

# The controller interacts with the website, receiving data from the client and saving it in session.

# As the user enters new information into the website, the controller requests the information entered into
# the form and updates the session data, with the new information, and then the flask app reroutes and renders
# the html page with the updated information which sends it back to the website,
# which then displays the updated information, with the users current guess, number of attempts, and proximity
# to the random number.

from flask_app import app
from flask import render_template, redirect, request, session
import random

@app.route('/projects/great-number-game')
def great_number_game():
    if 'random_int' not in session:
        session['random_int'] = random.randint(1,100)
    if 'guess' not in session:
        session['guess'] = 0
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template('/projects/great_number_game/index.html', random_int = session['random_int'], guess = session['guess'], attempts = session['attempts'] )

@app.route('/process/guess', methods = ['post'])
def process_guess():
    session['guess'] = int(request.form['guess'])
    
    if 'attempts' not in session:
        session['attempts'] = 1
    else:
        session['attempts'] += 1
    return redirect('/projects/great-number-game')

@app.route('/process/reset')
def process_reset():
    session.clear()
    return redirect('/projects/great-number-game')

@app.route('/process/leader_board', methods = ['post'])
def process_leader_board():
    session['name'] = request.form['name']
    return redirect('/projects/leader_board')

@app.route('/projects/leader_board')
def leader_board():
    return render_template('/projects/great_number_game/leader_board.html', name = session['name'], attempts = session['attempts'])
