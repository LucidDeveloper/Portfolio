# Controller file users_crud_controller.py is the primary controller for the Users App.

# The controller interacts with the website, receiving data from the forms on the website
# which is sent to the model file,users_crud_sqlite_model.py, which interacts with the 
# database, receiving data from the model to send back to the website, to then 
# view on the website.

# import app variable from flask_app package
from flask_app import app
# import render_template, request, redirect, session from flask
from flask import render_template, request, redirect, session
# import the Users class from the user_sqlite.py file in the models folder to interact with the database
from flask_app.models.users_crud_sqlite_model import Users

# since sqlite3 uses UTC time for the TimeStamp, we need to import the datetime module from the python standard library
# import the datetime module from the python standard library
import datetime

# needed for passing the date time as a variable, get the current datetime and store it in a variable
# sqlite timestamp is in UTC time, so we need to convert it to local time
currentDateTime = datetime.datetime.now()

# Display all users from the database on the Read (All) page
@app.route('/projects/users-crud')
def users_crud():
    users = Users.get_all()
    # check
    print("Now on View Page for All Users")
    return render_template('/projects/users_crud/index.html', users = users)

# Display form to create new users on the Create page
@app.route('/projects/users-crud/new')
def users_crud_new():
    # check
    print("Now on Create Page for New User")
    return render_template('/projects/users_crud/create_user.html')

# After successful creation of a new User, redirect to Read (One) page
@app.route('/users-crud/process', methods = ['post'])
def users_crud_process():
    data = {}
    data['first_name'] = request.form['first_name']
    data['last_name'] = request.form['last_name']
    data['email'] = request.form['email']
    data['created_at'] = currentDateTime
    data['updated_at'] = currentDateTime
    Users.save(data)
    # check
    print(f"User created at {data['created_at']}, (Controller.Users.users_process)")
    return redirect('/projects/users-crud/process/get_last_id')

# get id and redirect to show new user page
@app.route('/projects/users-crud/process/get_last_id')
def users_crud_process_get_last_id():
    user_id = Users.get_last_id()
    session['user_id'] = user_id[0]
    print(f"User with id {user_id[0]} created. (Controller.Users.users_process_get_last_id)")
    return redirect('/projects/users-crud/show')

# Read (One) page will display the User's information After Successful Creation
@app.route('/projects/users-crud/show')
def users_crud_show():
    data = {}
    # make sure to pass value at index and not a tuple. 
    # Confirm values in session and data are the same
    data['user_id'] = session['user_id'][0]
    print(f"User with data id {data['user_id']} and session id {session['user_id'][0]} passed. (Controller.Users.users_crud_show)")
    user = Users.get_one(data)
    # check
    print(f"Now Showing View Page for User with id {data['user_id']}")
    return render_template('/projects/users_crud/show_user.html', user = user)

# Read (One) page will display the User's information by ID
@app.route('/projects/users-crud/show/<user_id>')
def users_crud_show_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    # check 
    print(f"Now Showing View Page for User with id {data['user_id']}")
    return render_template('/projects/users_crud/show_user.html', user = user)

# Edit link will render the Users Edit page
@app.route('/projects/users-crud/edit/<user_id>')
def users_crud_edit_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    # check
    print(f"Now Showing Edit Page for User with id {data['user_id']}")
    return render_template('/projects/users_crud/edit_user.html', user = user)

# After successful update of user, redirect to the Read (One) page and display the updated information
@app.route('/users-crud/edit/process/<user_id>', methods = ['post'])
def users_crud_edit_process_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    data['first_name'] = request.form['first_name']
    data['last_name'] = request.form['last_name']
    data['email'] = request.form['email']
    data['updated_at'] = currentDateTime
    session['user_id'] = user_id
    Users.update(data)
    # check
    print(f"Update made on User with id {data['user_id']} at {data['updated_at']}")
    return redirect('/projects/users-crud/show')

# Delete link will delete the User from the database, and redirect to the Read (All) page
@app.route('/projects/users-crud/delete/<user_id>')
def users_crud_delete_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    # check
    print(f"Now Showing User with id {user_id} for Delete Confirmation")
    return render_template('/projects/users_crud/delete_user.html', user = user)

# Delete link will delete the User from the database, and redirect to the Read (All) page
@app.route('/users-crud/delete/process/<user_id>')
def users_crud_delete_process_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    Users.delete(data)
    # check
    print(f"Deleted User with id {user_id}")
    return redirect('/projects/users-crud')

