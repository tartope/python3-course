from csv import reader
from csv import DictReader
from csv import writer
from csv import reader, writer
from csv import writer, DictWriter
from csv import DictReader, DictWriter
import csv
import json

# Reading CSV (comma separated values) files: a way of taking data, usually tabular data, and putting it in a file and storing it so that we can do something with it later.
# -it's a common format that we can work with.
# - CSV files are a common file format for tabular data; it does not suit all kinds of data; it needs to be homogenous data that follows a pattern
# - we can read CSV files just like other text files (except it's not really a good idea)
# - Python has a built-in CSV module to read/write CSVs more easily

# see fighers.csv for details:
# - the first row in any CSV file contains the headers; the headers set-up what the data is; everything is separated by commas

# CSV Module:
# - reader: lets you iterate over rows of the CSV as lists (allows you to iterate over each row of a CSV, and each row is a separate list); it does not give a list by default, it's an iterator
# - Dictreader: lets you iterate over rows of the CSV as OrderDicts (the rows are known as ordered dicts, a dictionary with order so that it remembers what orcer things were in); the headers are automatically set-up to be the keys


# below is the INCORRECT way of reading CSVs; DON'T DO THIS!:
# with open("fighters.csv") as file:
#     data = file.read()


# Example 1 using reader()
# below is the CORRECT way of reading CSVs; THIS IS BETTER:
# ** import at top of page (from csv import reader)
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     # print(csv_reader)  #<-- <_csv.reader object at 0x102dacac0>  (gives us just the object)
#     for row in csv_reader:
#         # each row is a list
#         print(row)  #<--  ['Name', 'Country', 'Height (in cm)']   (IMPORTANT: the first row of the headers is still included)
#                         # ['Ryu', 'Japan', '175']
#                         # ['Ken', 'USA', '175']
#                         # ['Chun-Li', 'China', '165']
#                         # ['Guile', 'USA', '182']
#                         # ['E. Honda', 'Japan', '185']
#                         # ['Dhalsim', 'India', '176']
#                         # ['Blanka', 'Brazil', '192']
#                         # ['Zangief', 'Russia', '214']


# Example 2 using reader()
# if you want to iterate through the data such as:
# ** import at top of page (from csv import reader)
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")  #<-- Name is from Country
#                                                         # Ryu is from Japan
#                                                         # Ken is from USA
#                                                         # Chun-Li is from China
#                                                         # Guile is from USA
#                                                         # E. Honda is from Japan
#                                                         # Dhalsim is from India
#                                                         # Blanka is from Brazil
#                                                         # Zangief is from Russia


# Example 3 using reader()
# if you don't want the headers:
# ** import at top of page (from csv import reader)
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     # this moves us forward once, and it starts after the headers
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")  #<-- Ryu is from Japan
#                                                         # Ken is from USA
#                                                         # Chun-Li is from China
#                                                         # Guile is from USA
#                                                         # E. Honda is from Japan
#                                                         # Dhalsim is from India
#                                                         # Blanka is from Brazil
#                                                         # Zangief is from Russia


# Example 4 using reader()
# if you did want the headers, and you wanted to work with the data, and you don't want to just print it out or go through it one time, than you could turn it into a list.
# this gives a list of lists:
# ** import at top of page (from csv import reader)
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)  #<-- [['Name', 'Country', 'Height (in cm)'], ['Ryu', 'Japan', '175'], ['Ken', 'USA', '175'], ['Chun-Li', 'China', '165'], ['Guile', 'USA', '182'], ['E. Honda', 'Japan', '185'], ['Dhalsim', 'India', '176'], ['Blanka', 'Brazil', '192'], ['Zangief', 'Russia', '214']]


# Example 1 using DictReader()
# ** import at top of page (from csv import DictReader)
# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         # each row is an OrderedDict
#         print(row)  #<-- {'Name': 'Ryu', 'Country': 'Japan', 'Height (in cm)': '175'}
#                         # {'Name': 'Ken', 'Country': 'USA', 'Height (in cm)': '175'}
#                         # {'Name': 'Chun-Li', 'Country': 'China', 'Height (in cm)': '165'}
#                         # {'Name': 'Guile', 'Country': 'USA', 'Height (in cm)': '182'}
#                         # {'Name': 'E. Honda', 'Country': 'Japan', 'Height (in cm)': '185'}
#                         # {'Name': 'Dhalsim', 'Country': 'India', 'Height (in cm)': '176'}
#                         # {'Name': 'Blanka', 'Country': 'Brazil', 'Height (in cm)': '192'}
#                         # {'Name': 'Zangief', 'Country': 'Russia', 'Height (in cm)': '214'}


# Example 2 using DictReader()
# ** import at top of page (from csv import DictReader)
# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         # each row is an OrderedDict
#         print(row["Name"])  #<-- Ryu
#                                 # Ken
#                                 # Chun-Li
#                                 # Guile
#                                 # E. Honda
#                                 # Dhalsim
#                                 # Blanka
#                                 # Zangief


# Other Delimiters:
# - Readers accept a delimiter kwarg in case your data isn't separated by commas (separated by any other symbol and must be the same symbol throughout)


# Example 1 using Delimiter:
# ** import at top of page (from csv import reader)
# with open("fighters_two.csv") as file:
#     csv_reader = reader(file, delimiter= "|")
#     for row in csv_reader:
#     #each row is a list
#         print(row)  #<-- ['Name', 'Country', 'Height (in cm)']
#                         # ['Ryu', 'Japan', '175']
#                         # ['Ken', 'USA', '175']
#                         # ['Chun-Li', 'China', '165']
#                         # ['Guile', 'USA', '182']
#                         # ['E. Honda', 'Japan', '185']
#                         # ['Dhalsim', 'India', '176']
#                         # ['Blanka', 'Brazil', '192']
#                         # ['Zangief', 'Russia', '214']

#_____________________________________________________________

# Writing to CSV files: there are 2 different ways (with lists or dictionaries)

# Writing CSV files, using lists:
# - writer: creates a writer object for writing to CSV
# - writerow: method on a writer to write a row to the CSV 

# Example 1 using writer/writerrow
# ** import at top of page (from csv import writer)
# this wrote a new file cats.csv and added the data
# with open("cats.csv", "w") as file:
#     csv_writer = writer(file)
#     # this line adds the headers
#     csv_writer.writerow(["Name", "Age"])
#     # these lines adds the data
#     csv_writer.writerow(["Buddy", 11])
#     csv_writer.writerow(["Kitty", 1])


# Example 2 using writer/writerrow (not nested)
# ** import at top of page (from csv import reader, writer)
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     # turn it into a list in a list using list comprehension:
#     # for every row in csv_reader, make every "s"(item) in that row uppercase
#     fighters = [[s.upper() for s in row] for row in csv_reader]
#     # for every row in fighters, print row
#     for row in fighters:
#         print(row)

# # now that everything is all caps, take the fighters data and write it to the screaming_fighters.csv file:
# with open("screaming_fighters.csv", "w") as file:
#     csv_writer = writer(file)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)


# Example 3 using writer/writerow (nested)
# ** import at top of page (from csv import reader, writer)
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     with open("screaming_fighters.csv", "w") as file:
#         csv_writer = writer(file)
#         # for every fighter in csv_reader
#         for fighter in csv_reader:
#             # turn it into a list in a list using list comprehension:
#             # make every "s"(item) uppercase, for every "s" in fighter
#             csv_writer.writerow([s.upper() for s in fighter])
#_____________________________________________________________

# Writing CSV files, using Dictionaries:
# - DictWriter: creates a writer object for writing using dictionaries
# - fieldnames: kwarg for the DictWriter specifying headers
# - writeheader: method on a writer to write header row
# - writerow: method on a writer to write a row based on a dictionary

# ** import at top of page (from csv import writer, DictWriter)
# with open("cats.csv", "w") as file:
#     # define headers first
#     headers = ["Name", "Breed", "Age"]
#     # make our csv writer
#     csv_writer = DictWriter(file, fieldnames= headers)
#     # take the headers passed in under filednames and write them to the file for us
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Name": "Garfield",
#         "Breed": "Orange Tabby",
#         "Age": 10
#     })

# using "writer" usually means less code; using DictWriter usually means being more explicit in your code (being easier to understand); it's just a preference.

# below takes the fighters.csv file, changes the cm to inches, and copies to another file:
# ** import at top of page (from csv import DictReader, DictWriter)
# def cm_to_in(cm):
#     return float(cm) * 0.393701

# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     fighters = list(csv_reader)

# with open("inches_fighters.csv", "w") as file:
#     # pass in headers and update cm to in
#     headers = ("Name", "Country", "Height")
#     csv_writer = DictWriter(file, fieldnames= headers)
#     csv_writer.writeheader()
#     for f in fighters:
#         csv_writer.writerow({
#             "Name": f["Name"],
#             "Country": f["Country"],
#             # this line changes Height in cm to inches using cm_to_in function, and is stored with Height key
#             "Height": cm_to_in(f["Height (in cm)"])
#         })
#_____________________________________________________________

# Practice Example 1.
# add_user
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.
# Implement the following function:
# add_user : Takes in a first name and a last name and adds a new user to the users.csv file.

# import at top of page (import csv)
# def add_user(first_name, last_name):
#     with open("users.csv", "a") as file:
#         headers = ["First Name", "Last Name"]
#         csv_writer = csv.DictWriter(file, fieldnames = headers)
#         csv_writer.writerow({
#             "First Name": first_name,
#             "Last Name": last_name
#         })

# add_user("Dwayne", "Johnson")
#_____________________________________________________________

# Practice Example 2.
# print_users
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.
# Implement the following function:
# print_users : prints out all of the first and last names in the users.csv file

# import at top of page (from csv import reader)
# def print_users():
#     with open("users.csv") as file:
#         csv_reader = reader(file)
#         next(csv_reader)
#         for row in csv_reader:
#             print("{} {}".format(row[0], row[1]))

# print_users()  #//=> Colt Steele
#                 # Dwayne Johnson

# instructors code, works the same:
# def print_users():
#     with open("users.csv") as csvfile:
#         csv_reader = csv.DictReader(csvfile)
#         for row in csv_reader: 
#             print("{} {}".format(row['First Name'], row['Last Name']))
#_____________________________________________________________

# Practice Example 3.
# find_user
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.
# Implement the following function:
# find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file. If the user is found, find_user  returns the index where the user is found. Otherwise it returns a message stating that the user wasn't found.

# my code and instructors code:
# import at top of page (from csv import reader)
# def find_user(first_name, last_name):
#     with open("users.csv") as file:
#         csv_reader = reader(file)
#         # enumerate method assigns an index to each row
#         for (index, row) in enumerate(csv_reader):
#             if(row[0]==first_name and row[1]==last_name):
#                 return index
#         return "{} {} not found.".format(first_name, last_name)

# print(find_user("Dwayne", "Johnson"))

# instructors code, works the same:
# import at top of page (import csv)
# def find_user(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         for (index, row) in enumerate(csv_reader):
#             first_name_match = first_name == row[0]
#             last_name_match = last_name == row[1]
#             if first_name_match and last_name_match:
#                 return index
#         return "{} {} not found.".format(first_name, last_name)
#_____________________________________________________________

# Pickle: take something from Python, put it in a special pickle file.  The pickle module will serialize the data, converting it into a byte stream, and we can unpickle it when we want to pull it out of the file and turn it back into whatever it was before.  
# see pickling_example.py file (that file created pets.pickle file which has binary data in it)
# because it's binary, can't be used; it's just stored
#_____________________________________________________________

# JSON Pickling:
# import at top of page (import json)
# dumps(): takes the below and turn it into Python formatting (ie, double quotes, None is changed to null, and no tuples); basically json.dumps() formats a Python object as a STRING of JSON.
j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

# print(j)  #//=>  ["foo", {"bar": ["baz", null, 1.0, 2]}]

# to use JSON Pickling, you have to install it first with pip; run: python3 -m pip install jsonpickle
# refer to json_pickly.py file and cat.json file
#_____________________________________________________________

# Practice Example 4.
# update_users
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.
# Implement the following function:
# update_users : Takes in an old first name, an old last name, a new first name, and a new last name. Updates the users.csv file so that any user whose first and last names match the old first and last names are updated to the new first and last names. The function should return a count of how many users were updated.

# my code and instructors code:
# import at top of page (from csv import reader, writer)
# def update_users(old_first, old_last, new_first, new_last):
#     with open("users.csv") as file:
#         csv_reader = reader(file)
#         # turn file into a list of lists
#         rows = list(csv_reader)
#         # print(rows)  #<-- [['First Name', 'Last Name'], ['Colt', 'Steele'], ['Dwayne', 'Johnson'], ['Grace', 'Hopper'], ['Alan', 'Turing'], ['Colt', 'Steele']]
#     count = 0
#     with open("users.csv", "w") as file:
#         csv_writer = writer(file)
#         # for every row in rows
#         for row in rows:
#             if(row[0]== old_first and row[1] == old_last):
#                 # overwrite the row with the new info
#                 csv_writer.writerow([new_first, new_last])
#                 count +=1
#             else:
#                 # else, overwrite with the original row
#                 csv_writer.writerow(row)
#     # return the number of users updated with the count that was incremented in each loop
#     return "Users updated: {}.".format(count)

# update_users("Grace", "Hopper", "Hello", "World")
#_____________________________________________________________

# Practice Example 5.
# delete_users
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.
# Implement the following function:
# delete_users : Takes in a first name and a last name. Updates the users.csv file so that any user whose first and last names match the inputs are removed. The function should return a count of how many users were removed.

# my code and instructors code:
# import at top of page (from csv import reader, writer)
# def delete_users(first_name, last_name):
#     # basic reading the file
#     with open("users.csv") as file:
#         csv_reader = reader(file)
#         # turn the file into a list of lists
#         rows = list(csv_reader)
        
#     count = 0
#     # basic writing the file
#     with open("users.csv", "w") as file:
#         csv_writer = writer(file)
#         # loop through the list of rows
#         for row in rows:
#             # if the row matches the passed name, increase the count (this row doesn't get re-written)
#             if(row[0] == first_name and row[1] == last_name):
#                 count += 1
#             # if it doesn't match, re-write the current row in the list
#             else:
#                 csv_writer.writerow(row)
#     # return the count
#     return "Users deleted: {}.".format(count)
# delete_users("Hello", "World")