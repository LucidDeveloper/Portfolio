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

@app.route('/payments')
def payments():
    return render_template('/payments.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/home')
def home():
    return redirect('/')
