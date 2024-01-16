# Controllers act as servers for each distinct model and respective templates within the app
from flask_app.__init__ import app
from flask import redirect, render_template

@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/linked_in')
def linked_in():
    return redirect('linkedin.com')

@app.route('/git_hub')
def git_hub():
    return redirect('github.com')

@app.route('/email')
def email():
    return redirect()