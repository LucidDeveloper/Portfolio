# Controller great_number_game.py is the primary controller for the Great Number Game

from flask_app import app
from flask import render_template, redirect, request, session
import random

@app.route('/projects/great_number_game')
def great_number_game():
    if 'random_int' not in session:
        session['random_int'] = random.randint(1,100)
    if 'guess' not in session:
        session['guess'] = 0
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template('/projects/great_number_game.html', random_int = session['random_int'], guess = session['guess'], attempts = session['attempts'] )

@app.route('/process/guess', methods = ['post'])
def guess():
    session['guess'] = int(request.form['guess'])
    
    if 'attempts' not in session:
        session['attempts'] = 1
    else:
        session['attempts'] += 1
    return redirect('/projects/great_number_game')

@app.route('/process/reset')
def reset():
    session.clear()
    return redirect('/projects/great_number_game')

@app.route('/process/leader_board', methods = ['post'])
def process_leader_board():
    session['name'] = request.form['name']
    return redirect('/projects/leader_board')

@app.route('/projects/leader_board')
def leader_board():
    return render_template('/projects/leader_board.html', name = session['name'], attempts = session['attempts'])
