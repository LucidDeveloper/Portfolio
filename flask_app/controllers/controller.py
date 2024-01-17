# Controllers act as servers for each distinct model and respective templates within the app
from flask_app import app
from flask import redirect, render_template

@app.route('/')
def root():
    return render_template('index.html')
    

@app.route('/home')
def home():
    return redirect('/')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/linked_in')
def linked_in():
    return redirect('https://www.linkedin.com/in/lucid-developer/')

@app.route('/git_hub')
def git_hub():
    return redirect('https://www.github.com/LucidDeveloper/')

@app.route('/email')
def email():
    return redirect('mailto:lucid_developer@proton.me')