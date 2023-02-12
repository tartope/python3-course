from csv import reader
from csv import DictReader
from csv import writer
from csv import reader, writer
from csv import writer, DictWriter

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
#     # this line data the headers
#     csv_writer.writerow(["Name", "Age"])
#     # this line adds the data
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
with open("cats.csv", "w") as file:
    # define headers first
    headers = ["Name", "Breed", "Age"]
    # make our csv writer
    csv_writer = DictWriter(file, fieldnames= headers)
    # take the headers passed in under filednames and write them to the file for us
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })

# using "writer" usually means less code; using DictWriter usually means being more explicit in your code (being easier to understand); it's just a preference.