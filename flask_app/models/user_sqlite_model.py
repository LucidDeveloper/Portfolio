# import database connection
from flask_app.config.sqlite_connection_configuration import connectToSQLite

# set database name
db = 'C:/Users/Gianni/Desktop/SDE/GitHubRepos/LucidDeveloper/Portfolio/flask_app/database/users.db'

# create a class for the user table
class Users:
    
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToSQLite(db).query_db(query)
        print(results)
        users = []
        if not results:
            return users
        else:
            for user in results:
                users.append(cls(user))
            return users # Returns list of objects
    
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM users WHERE id = :id;'
        results = connectToSQLite(db).query_db(query, data)
        users = []
        for user in results:
            users.append(cls(user))
        return users[0] # Returns object at position 1 (index 0 ) from created List of dictionaries
    
    @classmethod
    def save(cls,data):
        query = '''INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
        VALUES (:first_name,:last_name,:email,:created_at,:updated_at);'''
        user_id = connectToSQLite(db).query_db(query, data)
        return user_id # Returns respective id of created user record
    
    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM users WHERE id = :user_id;'
        connectToSQLite(db).query_db(query, data)
        return # Deletes User record by id, returns nothing
    
    @classmethod
    def update(cls,data):
        query = 'UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = :updated_at WHERE id = :user_id;'
        connectToSQLite(db).query_db(query, data)
        return # Updates User record by id, returns nothing
    