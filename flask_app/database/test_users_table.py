# import the sqlite3 module from python standard library
import sqlite3

# since sqlite3 uses UTC time for the TimeStamp, we need to import the datetime module from the python standard library
# import the datetime module from the python standard library
import datetime

# for passing the date time as a variable, get the current datetime and store it in a variable
# modules cannot be called and passed as a variable
currentDateTime = datetime.datetime.now()

# make sure to change your current working directory in your terminal to where you want the database to be created
# sqlite will connect to the database specified in the path, if the file does not exist, 
# then it will create the file in the cwd

# if you are not connecting to the database file from the same directory, then you will need to use an absolute path
# note that the path to the database is absolute since we are not connecting to the database file from the same directory
db = 'C:/Users/Gianni/Desktop/SDE/GitHubRepos/LucidDeveloper/Portfolio/flask_app/database/users.db'

# connect to the database connection with detect_types so that we can easily pass datetime information
connection = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

# create a cursor to allow us to execute queries (sql commands)
cursor = connection.cursor()

# Note!
# in order to store the datetime information in the table, we need to use the column datatype ‘TIMESTAMP’.
# sqlite3 will store the datetime information in the format of YYYY-MM-DD HH:MM:SS.SSS UTC
# for local time you will have to import the datetime module from the python standard library 
# and use the datetime.datetime.now() method and store it in a variable to be passed as a variable for query execution

'''query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="users";'
table = cursor.execute(query).fetchone()

if not table:
    print("table does not exist")
    print("creating table")
'''


#    # create a table for users
#    cursor.execute('''CREATE TABLE users (
#                    ROWID INTEGER PRIMARY KEY AUTOINCREMENT, 
#                    first_name TEXT, last_name TEXT, email TEXT,
#                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#                    );''')


'''
else:
    print(f"table {table} exists")

query = 'SELECT * FROM users;'
users = cursor.execute(query).fetchall()

if not users:
    print("table is empty")
else:
    print (f"table {table} is not empty")
    for user in users:
        print(user)'''

        
'''query = 'SELECT seq FROM sqlite_sequence WHERE name="users";'
seq = cursor.execute(query).fetchall()
print("Sequence:", seq)

query = "SELECT last_insert_rowid() FROM users;"
last_row_id = cursor.execute(query).fetchall()
print("Inserted row with id:", last_row_id)

query = 'SELECT max(id) from users;'
list_max_id = cursor.execute(query).fetchall()
print("List Max id:", list_max_id)

query = 'SELECT max(id) from users;'
max_id = cursor.execute(query).fetchone()
print("Max id:", max_id)

query = 'SELECT max(ROWID) from users;'
list_max_id = cursor.execute(query).fetchall()
print("List Max id:", list_max_id)

query = 'SELECT max(ROWID) from users;'
max_id = cursor.execute(query).fetchone()
print("Max id:", max_id)
'''




# execute formatted sql commands to insert data into the table
# example:
# cursor.execute(query, data)
# Note!
# query must be in the form of a string,
# data must be in the form of a tuple or a dictionary
# if single variable is being passed, data must be in the form of a tuple with a comma or 
# else it will not be recognized as a tuple

# cursor.execute('''INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
#             VALUES ("Richard", "Nixon","richard.nixon@gmail.com",?,?);''', (currentDateTime, currentDateTime))
# cursor.execute('''INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
#             VALUES ("Beyonce", "Knowles","beyonce.knowles@gmail.com",?,?);''', (currentDateTime, currentDateTime))

#print(cursor.execute('SELECT * FROM users;').fetchall())

# cursor.execute('DELETE FROM users WHERE id = 8;')
# results = cursor.execute('SELECT * FROM users;').fetchall()
# print(results)


# cursor.execute('SELECT * FROM users;')
# one = cursor.execute('SELECT * FROM users;').fetchone()
# many = cursor.fetchall()
# print(one)
# print(many)
# print(one[1])


# print(cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="users";').fetchall())

#query = 'SELECT * FROM users WHERE id = :id;'
#data = {'id': 1}
#query = cursor.execute(query, data).fetchall()

#print(query)
#print(query[0])
#print(str(query[0]).lower().find("nixon"))
'''query = 'DROP TABLE users;'
cursor.execute(query)
query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="users";'
table = cursor.execute(query).fetchall()

if  not  table:
    print("table no longer  exists")
else:
    print(f"table {table} still exists")
'''

query = 'SELECT max(ROWID) FROM users;'
max_id = cursor.execute(query).fetchone()

print("max_id:", max_id[0])

# save the changes to the database
connection.commit()

# close the cursor
cursor.close()

# close the connection
connection.close()
