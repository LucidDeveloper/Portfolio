# This file contains the configuration for the connection to the database
# Interacting with the Database and Executing the queries from the users model

# import sqlite module from python standard library
import sqlite3

# this class will give us an instance of a connection to our database
class SQLiteConnection:
    def __init__(self, db):
        # connect to the database connection with detect_types so that we can easily pass datetime information
        connection = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        # define and establish the connection to the database to be used in the model
        self.connection = connection
        
    # the method to query the database
    def query_db(self, query, data={}):
        cursor = self.connection.cursor()
        try:
            # run query to format the query and data, and execute the query
            formatted_query = cursor.execute(query, data)
            # print formatted query
            print(f"cursor.execute(query, data): {formatted_query}, (Config.SQLiteConnection.query_db)")
            # modify the query from a list to a string in order to use the .lower() and .find() string methods
            # string_query = str(query)
            # print running query
            print(f"Running Query: {query} (Config.SQLiteConnection.query_db))")
            # check if query is an INSERT, SELECT, UPDATE, or DELETE query
            if query.lower().find("insert") >= 0:
                # INSERT queries will return nothing
                self.connection.commit()
                return
            elif query.lower().find("select") >= 0:
                # SELECT queries will return data
                # fetch all method will return the data from the database as a List of tuples
                fetch_all_result = cursor.fetchall()
                print("fetch all result from sql connection configuration:", fetch_all_result)
                return fetch_all_result # Returns the data from the database as a List of tuples
            elif query.lower().find("max(rowid)") >= 0:
                # SELECT max(rowid) queries will return data
                # fetch one method will return the data from the database as a tuple
                fetch_one_result = cursor.fetchone()
                print("fetch one result from sql connection configuration:", fetch_one_result)
                return fetch_one_result[0] # Returns the first value of the tuple at index 0, as a string
            else:
                # UPDATE and DELETE queries will return nothing
                self.connection.commit()
        except Exception as e:
            # If the Query Fails the method will return FALSE
            print("Something went wrong", e)
            return False
        finally:
            # Close Connection
            self.connection.close()

# function connectToSQLite receives the database we're using and uses it to create an instance of MySQLConnection
# by creating an instance of the class SQLiteConnection, we can interact with the database, 
# without having to worry about the connection details
def connectToSQLite(db):
    # connect to database
    connection = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = connection.cursor()
    # query to check for table users
    query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="users";'
    table = cursor.execute(query).fetchone()
    # check database for table users
    if not  table:
        # create table users
        connection.cursor().execute('''CREATE TABLE users (
                ROWID INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT, last_name TEXT, email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );''')
        # save table
        connection.commit()
        # print table check
        print(f"Table {table} created.")
        return SQLiteConnection(db)
    else:
        return SQLiteConnection(db)
