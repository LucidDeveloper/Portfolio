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
        cursor.execute(query, data)
        list_query = cursor.fetchall()
        print("Running Query:", list_query)
        
        # cursor.execute(query, data)
        
        # modify the list query to a string in order to use the .lower() and .find() string methods
        string_query = str(list_query)
        if string_query.lower().find("insert") >= 0:
            # INSERT queries will return the ID NUMBER of the row inserted
            self.connection.commit()
            # close the connection
            self.connection.close()
            return cursor.lastrowid
        elif string_query.lower().find("select") >= 0:
            # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
            result = cursor.fetchall()
            print(result)
            self.connection.commit()
            # close the connection
            self.connection.close()
            return result
        else:
            # UPDATE and DELETE queries will return nothing
            self.connection.commit()
            # close the connection
            self.connection.close()
            return
        
#        except Exception as e:
#                # if the query fails the method will return FALSE
#                print("Something went wrong", e)
#                print("list_query:", list_query)
#                print("tuple_query:", tuple_query)
#                print("string_query:", string_query)
#                print("query:", query)
#                print("data:", data)
#                return False
#        finally:
#            # close the connection
#            self.connection.close()

# function connectToSQLite receives the database we're using and uses it to create an instance of MySQLConnection
def connectToSQLite(db):
    # connect to database
    connection = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = connection.cursor()
    table = cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="users";').fetchall()
    # check database for table users
    if table == []:
        # create table users
        connection.cursor().execute('''CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT, last_name TEXT, email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );''')
        connection.commit()
        connection.cursor().close()
        connection.close()
        print("Table users created.")
        return SQLiteConnection(db)
    else:
        print("Table users already exists.")
        return SQLiteConnection(db)

# by creating an instance of the class SQLiteConnection, we can interact with the database, 
# without having to worry about the connection details