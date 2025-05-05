# Configuration file sqlite_connection_configuration.py works together with the model file users_crud_sqlite_model.py 
# to interact with the database.

# import sqlite module from python standard library
import sqlite3
# this class will give us an instance of a connection to our database, every time it is called
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
            # run query to execute the query
            cursor.execute(query, data)
            
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
                return fetch_all_result
            elif query.lower().find("max(rowid)") >= 0:
                # SELECT max(rowid) queries
                fetch_one_result = cursor.fetchone()
                print("fetch all for fetch one result from sql connection configuration:", fetch_one_result)
                return fetch_one_result # Returns the first value at index 0
            else:
                # UPDATE and DELETE queries will return nothing
                self.connection.commit()
        except Exception as e:
            # If the Query Fails the method will return FALSE and catch the exception
            print("Something went wrong", e)
            return False
        finally:
            # Close Connection
            self.connection.close()

# function connectToSQLite receives the data from the website, checks that the database is present and forwards data to
# sqliteConnection Class for interaction with the database
def connectToSQLite(db):
    # connect to database
    connection = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = connection.cursor()
    # query to check for table users
    query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="users";'
    table = cursor.execute(query).fetchall() # fetchall returns a list of tuples
    # check database for table users
    if  table == []:
        # create table users
        connection.cursor().execute('''CREATE TABLE users (
                ROWID INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT, last_name TEXT, email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );''')
        # save table
        connection.commit()
        # table confirmation
        print(f"Table {table} created.")
        return SQLiteConnection(db)
    else:
        # table confirmation
        print(f"Table {table} exists.")
        return SQLiteConnection(db)
