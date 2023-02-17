import sqlite3

# Connect to DB with Python:

# - import sqlite3
# - connect to db: sqlite3.connect() and assign it to a variable
# - make cursor: con.cursor and assign it to a variable
# - execute sql code by passing it into execute() method: c.execute()
# - commit the changes: con.commit()
# - close the db at the end: con.close()

# connect to, or create and connect to, a db using Python
con = sqlite3.connect("my_friends.db")

# Cursor: a temporary work space for sql commands; it allocates a litte bit of memory for us to work and it usually returns data; you basically create a cursor and then execute differnt lines of sql with it.  See pattern below:
# 1. create cursor object
c = con.cursor()
# 2. execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# INSERTING with Python:

# one way to insert values into a table (does not use Python); not the best way because it is hardcoded; because this line is long, people will use triple quotes and break it up into multiple lines.
# insert_query = '''INSERT INTO friends 
#                     VALUES ('Merriwether', 'Lewis', 7)'''
# c.execute(insert_query)

# second way to insert values; also not the best way
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
# c.execute(query)

# BEST WAY to INSERT INTO table:

# - INSERT one value:
# form_first = "Mary-Todd"
# # placeholder "?" for each value
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# # pass in a tuple containing values to be added; REMEMBER: one item tuples need the comma at the end
# c.execute(query, (form_first,))

# - INSERTING multiple values:
# data = ("Crocodile", "Dundee", 5)
# # placeholder "?" for each value
# query = "INSERT INTO friends VALUES (?, ?, ?)"
# # pass in data containing values to be added
# c.execute(query, data)

# Bulk INSERTS with Python:

people = [
    ("R", "Amundsen", 5),
    ("R", "Parks", 8),
    ("H", "Hudson", 7),
    ("N", "Armstrong", 7),
    ("D", "Boone", 3),
]

# one way to insert bulk items (if all you're doing is inserting bulk data): pass in query and then data
# c.executemany("INSERT INTO friends VALUES (?, ?, ?)", people)

# second way to insert bulk items (if you're inserting bulk data and then doing something else with it, so you only iterate once): iterate over list with a for loop, pass in query, and then data
# for person in people:
#     c.execute("INSERT INTO friends VALUES (?, ?, ?)", person)
#     print("INSERTING NOW!!!")

# example of insert bulk and averaging closeness of friendship:
# assign zero to average
# average = 0
# for person in people:
#     c.execute("INSERT INTO friends VALUES (?, ?, ?)", person)
#     # add each "closeness" rating to average (index 2 of person tuple)
#     average += person[2]
# print(average/len(people))

# SELECTING with Python:

# c.execute("SELECT * FROM friends") #<-- paired with c.fetchall()
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")  #<-- paired with c.fetchone()
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")  #<-- paired with c.fetchall()

# print(c)  #//=> <sqlite3.Cursor object at 0x102dad3c0>  <-- returns an object that is an iterator

# one way to iterate over the data:
# - Iterate over the cursor
# for result in c:
#     print(result) #//=> returns all tuples with the data; iterates one at a time

# another way to iterate and return a list:
# Fetch ALL results as a list
# print(c.fetchall())

# Fetch One result
# this gives only the first Rosa in the db
# print(c.fetchone())

# SQL INJECTION:




# 3. commit changes
con.commit()

# At the very end, close the connection
con.close()