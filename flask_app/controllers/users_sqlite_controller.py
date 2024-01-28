# Controller users.py is the primary controller for the Users App

# import app variable from flask_app package
from flask_app import app
# import render_template, request, redirect, session from flask
from flask import render_template, request, redirect, session
# import the Users class from the user_sqlite.py file in the models folder to interact with the database
from flask_app.models.user_sqlite_model import Users

# since sqlite3 uses UTC time for the TimeStamp, we need to import the datetime module from the python standard library
# import the datetime module from the python standard library
import datetime

# for passing the date time as a variable, get the current datetime and store it in a variable
# modules cannot be called and passed as a variable
currentDateTime = datetime.datetime.now()

# Display all users from the database on the Read (All) page
@app.route('/projects/users-crud')
def users():
    users = Users.get_all()
    print("View Page for All Users")
    return render_template('/projects/users_crud/show_users.html', users = users)

# Display form to create new users on the Create page
@app.route('/projects/users-crud/new')
def users_new():
    print("Create Page for New User")
    return render_template('/projects/users_crud/create_user.html')

# After successful creation of a new User, redirect to Read (One) page
@app.route('/users-crud/process', methods = ['post'])
def users_process():
    data = {}
    data['first_name'] = request.form['first_name']
    data['last_name'] = request.form['last_name']
    data['email'] = request.form['email']
    data['created_at'] = currentDateTime
    data['updated_at'] = currentDateTime
    user_id = Users.save(data)
    session['user_id'] = user_id
    print(f"User with id {user_id} created.")
    return redirect('/projects/users-crud/show')

# Read (One) page will display the User's information After Successful Creation
@app.route('/projects/users-crud/show')
def users_show():
    data = {}
    data['user_id'] = session['user_id']
    session.clear()
    user = Users.get_one(data)
    print(f"Showing View Page for User with id {data['user_id']}")
    return render_template('/projects/users_crud/show_user.html', user = user)

# Read (One) page will display the User's information by ID
@app.route('/projects/users-crud/show/<user_id>')
def users_show_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    print(f"Showing View Page for User with id {data['user_id']}")
    return render_template('/projects/users_crud/show_user.html', user = user)

# Edit link will render the Users Edit page
@app.route('/projects/users-crud/edit/<user_id>')
def users_edit_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    print(f"Showing Edit Page for User with id {data['user_id']}")
    return render_template('/projects/users_crud/edit_user.html', user = user)

# After successful update of user, redirect to the Read (One) page and display the updated information
@app.route('/users-crud/edit/process/<user_id>', methods = ['post'])
def users_edit_process_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    data['first_name'] = request.form['first_name']
    data['last_name'] = request.form['last_name']
    data['email'] = request.form['email']
    data['updated_at'] = currentDateTime
    session['user_id'] = user_id
    Users.update(data)
    print(f"Update made on User with id {data['user_id']}")
    return redirect('/projects/users-crud/show')

# Delete link will delete the User from the database, and redirect to the Read (All) page
@app.route('/projects/users-crud/delete/<user_id>')
def users_delete_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    print(f"Show User with id {user_id} for Delete Confirmation")
    return render_template('/projects/users_crud/delete_user.html', user = user)

# Delete link will delete the User from the database, and redirect to the Read (All) page
@app.route('/users-crud/delete/process/<user_id>')
def users_delete_process_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    Users.delete(data)
    print(f"Deleted User with id {user_id}")
    return redirect('/projects/users-crud')

