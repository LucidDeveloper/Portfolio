# Model file user_crud_sqlite_model.py filters data to and from the Database users.db, 
# using the sqlite3 queries and the sqlite_connection_configuration.py file.

# As the client creates, reads, updates, and deletes information, the controller file 
# users_crud_sqlite_controller.py, which interacts with the website, receives the data 
# from the client to send to the model, the model then takes the data and updates the database,
# and sends it back to the controller, which then presents it to the client on the website.

# import database connection
from flask_app.config.sqlite_connection_configuration import connectToSQLite

# set database name
db = 'C:/Users/Gianni/Desktop/SDE/GitHubRepos/LucidDeveloper/Portfolio/flask_app/database/users.db'

# create a class for the user table
class Users:
    
    def __init__(self,data):
        # indices must be integers since data from sqlite
        # is stored and sent as a tuple and not as a dictionary
        self.id = data[0]
        self.first_name = data[1]
        self.last_name = data[2]
        self.email = data[3]
        self.created_at = data[4]
        self.updated_at = data[5]
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToSQLite(db).query_db(query)
        # sqlite3 returns results as a list of tuples
        users = []
        if results == []:
            return users
        else:
            # Create List of Objects from list of tuples
            for user in results:
                users.append(cls(user)) # cls method instantiates each group of data and Creates an Object (cls() is the constructor method)
            return users # Returns list of objects from list of tuples
    
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM users WHERE ROWID = :user_id;'
        print(f"first run: query: {query} (Model.Users.get_one)")
        print(f"first run:  data: {data} (Model.Users.get_one)")
        results = connectToSQLite(db).query_db(query, data)
        print(f"results:{results}")
        
        users = []
        
        if results == False:
            # run Query again
            results = connectToSQLite(db).query_db(query, data)
            print(f"second run: query: {query} (Model.Users.get_one)")
            print(f"second run: data: {data} (Model.Users.get_one)")
            print(f"2nd results:{results}")
        
        for user in results:
            # Create List of Objects
            users.append(cls(user)) # cls method Creates Objects (cls() is the constructor method)
        return users[0] # Returns object at position 1 (index 0 ) from created List
    
    @classmethod
    def save(cls,data):
        query = '''INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
        VALUES (:first_name,:last_name,:email,:created_at,:updated_at);'''
        connectToSQLite(db).query_db(query, data)
        return
    
    @classmethod
    def get_last_id(cls):
        query = 'SELECT max(ROWID) FROM users;'
        user_id = connectToSQLite(db).query_db(query)
        print(f"max rowid: {user_id} (Model.Users.get_last_id)" )
        return user_id # Returns respective id of created user record
    
    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM users WHERE ROWID = :user_id;'
        connectToSQLite(db).query_db(query, data)
        return # Deletes User record by id, returns nothing
    
    @classmethod
    def update(cls,data):
        query = 'UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = :updated_at WHERE ROWID = :user_id;'
        connectToSQLite(db).query_db(query, data)
        return # Updates User record by id, returns nothing
    