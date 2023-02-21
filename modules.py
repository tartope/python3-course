# Modules (there are different types of modules such as custom modules that we write and require in other files, and there are built-in modules that come with Python by default but we must manually import them to use them):
# - keeps Python files small
# - reuse code across multiple files by importing (if we have 10 files and we're using the same function in all files, we don't need to redefine that function everytime; we can import it and write it once in a single file)
# - a module is just a Python file

# Built-in Modules Example:
# import random

# print(random.choice(["apple", "banana", "cherry", "durian"]))  #//=> cherry (picks a random element)
# print(random.randint(1,100))   #//=> 58 (picks a random number)
# print(random.shuffle(["apple", "banana", "cherry", "durian"]))

# we can alias the module name (usually done with long module names; you can make the name shorter):
# import random as rand

# print(rand.choice(["apple", "banana", "cherry", "durian"]))   #//=> apple
# print(rand.shuffle(["apple", "banana", "cherry", "durian"]))
# print(rand.randint(1,100))  #//=> 54

# Importing Parts of a Module:
# - the "from" keyword lets you import parts of a module
# - handy rule of thumb: only import what you need
# - if you still want to import everything, you can also use the "from MODULE import *" pattern
# from random import choice, randint  
# print(choice(["apple", "banana", "cherry", "durian"]))   #//=> apple  #<-- no longer need to call the "random" part but can just call "choice" or "randint"
# print(randint(1,100))  #//=> 32
# print(shuffle(["apple", "banana", "cherry", "durian"]))  #//=> name 'shuffle' is not defined  (because "shuffle" has not been imported)

# Different ways to import (all of these work):
# - import random
# - import random as omg_so_random
# - from random import *  (not best to do; should only import what you need)
# - from random import choice, shuffle
# - from random import choice as gimme_one, shuffle as mix_up_fruits

# from random import choice as pick, randint as magic_number_chooser
# print(pick(["apple", "banana", "cherry", "durian"]))  #//=> durian
# print(magic_number_chooser(1,100))  #//=> 39
#_______________________________________________________________

# Practice Example 1.

# Built In Modules Exercise
# It's time to get some practice with built-in modules.  Here's your mission;

# Import the math  module
# Use math.sqrt  to find the square root of 15129 and save it to variable called answer.

# from math import sqrt
# answer = sqrt(15129)
# print(answer)  #//=> 123.0
#_______________________________________________________________

# Practice Example 2.

# Built-In Modules: Slightly Tougher Challenge
# Define a function called contains_keyword  that accepts any number of string arguments.  It should return True  if any of the arguments are considered Python keywords (things like "def", "return", "if", etc.)  Otherwise it should return False.   Python has a built-in module called keyword  that contains a method called iskeyword .  Import keyword  and then use keyword.iskeyword  in you own function to determine if a given string is a keyword.

# contains_keyword("hello", "goodbye")  #False

# contains_keyword("def", "haha", "lol", "chicken", "alaska")  #True

# contains_keyword("four", "for", "if")  #True

# contains_keyword("blah", "doggo", "crab", "anchor")  #False

# contains_keyword("grizzly", "ignore", "return", "False")  #True

# Note: don't just manually check for the keywords you know like return, def, if, and for.  The test logic for this exercise will use a bunch of keywords we haven't yet covered, so definitely make sure to import and use the keyword module to help you! That's the point of this exercise, after all :)

# import keyword

# def contains_keyword(*args):
#     for word in args:
#         if keyword.iskeyword(word): 
#             return True
#     return False

# print(contains_keyword("hello", "goodbye"))  #//=> False
# print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))  #//=> True
#_______________________________________________________________

# Custom Modules (refer to the 3 files fruits, bananas, apples):
# - you can "import" from your own code too
# - the syntax is the same as before
# - import from the name of the Python file
# - if you have code that needs to be used in more than one place, put it in a module
# - if you have a really long file, and you have a way that you can group some of the functions into a module, or separate file, you can do that too
#_______________________________________________________________

# External Modules:
# - built-in modules come with Python
# - external modules are downloaded from the internet
# - you can download external modules using "pip" (pip installs packages)

# pip:
# - package management system for Python
# - as of 3.4, comes with Python by default
# - run command: python3 -m pip install NAME_OF_PACKAGE

# from termcolor import colored

# a built-in function that can get a list of names that a certain package/module comes with or any object:
# print(dir(termcolor))  #//=> ['ATTRIBUTES', 'COLORS', 'HIGHLIGHTS', 'RESET', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'annotations', 'colored', 'cprint', 'termcolor']

# or 
# print(help(termcolor))  #//=> will get a menu output in terminal of all functions and attributes for termcolor

# by default the below line does not print anything, so we save it to a variable and print the variable
# text = colored("Hi there", color="magenta")
# print(text)  #//=> Hi there <-- printed to terminal in magenta

# text = colored("Hi there", color="magenta",  on_color="on_yellow")
# print(text)  #//=> Hi there <-- printed to terminal in magenta, highlighted in yellow

# text = colored("Hi there", color="magenta",  on_color="on_cyan", attrs=["blink"])
# print(text)  #//=> Hi there <-- printed to terminal in magenta, highlighted in cyan, supposed to be blinking

# refer to ascii_art.py file for more practice
#_______________________________________________________________

# autopep8 Package: a package that you can download that will automatically format your code to conform to the pep8 style guide
# see ugly_code.py file for reference
#_______________________________________________________________

# The __name__ Variable:
# - when run, every Python file has a __name__ variable
# - if the file is the main file being run, by default, its value is "__main__"
# - otherwise, its value is the file name
# - refer to say_hi.py and say_sup.py for examples
#_______________________________________________________________

# Environment Set-up:
# - install virtual environment globally: python3 -m pip install virtualenv
# - create virtual environment in root of project with: python3 -m venv env
# - load dependencies in requirements.txt file: python3 -m pip install -r requirements.txt
# - run server with: python3 server.py (file name of server)
# - run client with: python3 client.py (file name of client)
#_______________________________________________________________

# Environment Set-up for Django:
# - install virtual environment globally: python3 -m pip install virtualenv
# - create project directory and cd into it
# - create virtual environment in root of project with: python3 -m venv env (or python3 -m venv .venv) (can use ls -a to see the .venv directory after it's created)
# - open project directory (you will see the .venv directory), and activate the venv, run: . .venv/bin/activate   (activate this anytime you want to work on the project); to deactivate venv, in the shell just run: deactivate
# - install django, run: pip install django (this will download django and any dependencies)
# - install django framework, run: pip install djangorestframework (this is the tool used to create the rest API)
# **- by default, django project comes with a security that blocks requests coming from different domains; to disable, run: pip install django-cors-headers
# - see all commands, run: django-admin (you will see all the commands that can be used with this, like runserver or startproject)
# - create project, run: django-admin startproject <projectname> .
# - a wrapper around the django-admin that does a little extra set-up for us and makes things easier. start the server, run: python manage.py runserver
# - take care of migrations error; with server running, activate venv, run: . .venv/bin/activate
# - then run: python manage.py migrate
# - use django's admin page to see different tables (and data inside); with server running, in the browser type /admin (you are brough to admin page where you login)
# - set-up admin, run: python manage.py createsuperuser   (create a username, email, and password)
# - to get a table on admin page, inside of project file make a new file, models.py
# - inside file: from django.db import models
# - create class for model
# **- to use PostgreSQL, install the database adapter, run: pip install psycopg2
# **- in settings: all 'rest_framework' and 'corsheaders' to INSTALLED_APPS; add 'CORS_ORIGIN_ALLOW_ALL = True'; add 'corsheaders.middleware.Cors.Middleware' to MIDDLEWARE; change DATABASES default engine to 'postgresql', add user, and add password.
# **- create psql db; create superuser and password
# - migrate, run (similar to creating schema files): python manage.py makemigrations <project name>
# - you will see error "no installed app with label '<project name>'"; got to settings.py file and add <project name> to INSTALLED_APPS list
# - apply to db, run (acutally migrates and creates table): python manage.py migrate
# - register to different tables to show up in the admin page: create admin.py inside <project name>; inside from django.contrib import admin, from .models import <Project name>


# - load dependencies in requirements.txt file: python3 -m pip install -r requirements.txt
# - run server with: python3 server.py (file name of server)
# - run client with: python3 client.py (file name of client)