# Controller portfolio.py is the primary controller for the Flask App

from flask_app import app

from flask import redirect, render_template

@app.route('/')
def root():
    return render_template('/portfolio/index.html')

@app.route('/resume')
def resume():
    return render_template('/portfolio/resume.html')

@app.route('/projects')
def projects():
    return render_template('/portfolio/projects.html')

@app.route('/home')
def home():
    return redirect('/')
