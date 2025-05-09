# Controller index_controller.py is the primary controller for the Flask App.

# Serving each page by its respective route.

from flask_app import app

from flask import redirect, render_template

@app.route('/')
def root():
    return render_template('/index.html')

@app.route('/resume')
def resume():
    return render_template('/resume.html')

@app.route('/projects')
def projects():
    return render_template('/projects.html')

@app.route('/home')
def home():
    return redirect('/')
