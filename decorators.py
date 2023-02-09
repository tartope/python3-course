# Higher Order Funtion (a function that returns another function from inside, or accepts one or more functions as an argument):
# - Example 1: a type of higer order function (passing functions as arguments)
def sum(n, func):
    # make a total variable to return and start at zero
    total = 0
    # loop through for every number in range
    for num in range(n):
        # square it with the square function, and add it to total
        total += func(num)
    # return total
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

# print(sum(3,square))  #//=> 5  <-- 0+1+4 = 5
# print(sum(3,cube)) #//=> 9  <-- 0+1+8 = 9


# - Example 2: nesting a function within a function and returning the result of that function combined with something else
from random import choice

def greet(person):
    # greet() calls get_mood()
    def get_mood():
        # set msg to choice of 3 statements
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        # return msg
        return msg
    
    # set result to concat of get_mood() and person
    result = get_mood() + person
    # return result
    return result

# print(greet("Toby")) #//=> Hello there Toby

# Example 3: nesting functions and returning functions from other functions
def make_laugh_func():
    # make_laugh_func() calls get_laugh()
    def get_laugh():
        # set laugh to choice of 3
        l = choice(("HAHAHA", "lol", "tehehe"))
        # return laugh
        return l

    # returns entire get_laugh() function
    return get_laugh

# set make_laugh_func() to variable, and print variable
laugh = make_laugh_func()
# print(laugh()) #//=> HAHAHA

# Example 4:
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(("HAHAHA", "lol", "tehehe"))
        return f"{laugh} {person}"

    return get_laugh()

laugh_at = make_laugh_at_func("Linda")
# print(laugh_at)  #//=> lol Linda
#_____________________________________________________________

# Decorators are functions inside of other functions; functions that wrap around other functions
# Again, what is a decorator?:
# - decorators are functions
# - decorators wrap other functions and enhance their behavior
# - decorators are examples of higher order functions
# - decorators have their own syntax, using "@" (syntactic sugar)

# Example of wrapper function without syntactic sugar/decorator:
# def be_polite(fn):
#     # the wrapper does something first, then does the function passed in (greet()), and then does something else.  It doesn't need to be called 'wrapper', it's just a standard name used.
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#
#     return wrapper

# # wrap this function inside the above function and return it, then store it in a variable called "wrapped_greet"
# def greet():
#     print("My name is Buddy.")

# def rage():
#     print("I don't like you!")

# wrapped_greet = be_polite(greet)
# # print(wrapped_greet()) #//=> What a pleasure to meet you!
#                             # My name is Buddy.
#                             # Have a great day!

# polite_rage = be_polite(rage) 
# print(polite_rage())  #//=> What a pleasure to meet you!
                        # I don't like you!
                        # Have a great day!


# Example of function with syntactic sugar/decorator:
def be_polite(fn):
    # the wrapper does something first, then does the function passed in (greet()), and then does something else
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")

    return wrapper

@be_polite
def greet():
    print("My name is Buddy.")

@be_polite
def rage():
    print("I don't like you!")

# When the decorator is added (ie. syntactic sugar), we don't need to set "greet = be_polite(greet)", we can just call "greet()"
# print(greet()) #//=>  gives the same output as above
# print(rage()) #//=>  gives the same output as above
#_____________________________________________________________

# Decorator Syntax (the function being wrapped is passed a parameter):
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()

#     return wrapper

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()

    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
    return "lol"

# print(greet("buddy")) #//=> HI, I'M BUDDY.
# using the version of the function without *args/**kwargs, the below print function won't work due to wrapper excepts only 1 parameter/argument; changing it to *args/**kwargs resolves the problem.
# print(order("burger", "fries"))  #//=> HI, I'D LIKE THE BURGER, WITH A SIDE OF FRIES, PLEASE.
# print(order(side="burger", main="fries"))  #//=> HI, I'D LIKE THE FRIES, WITH A SIDE OF BURGER, PLEASE.
# print(lol())  #//=> LOL
#_____________________________________________________________

# Preserving Metadata:
# Below causes a problem printing out doc strings or calling help() with decorators:
# def log_function_data(fn):
#     def wrapper(*args, **kwargs):
#         # Reminder: the syntax below with 3 double quotes ("""statement""") returns the documentation between it.
#         """I AM A WRAPPER FUNCTION"""
#         print(f"you are about to call {fn.__name__}")
#         print(f"Here's the documentation: {fn.__doc__}")
#         return fn(*args, **kwargs)

#     return wrapper

# @log_function_data
# def add(x,y):
#     """Adds two numbers together."""
#     return x+y

# print(add(10,30)) #//=> you are about to call add
                        # Here's the documentation: Adds two numbers together.
                        # 40


# the 3 lines below, don't refer to add() as expected, it refers to wrapper and prints those doc strings:
# print(add.__doc__) #//=> I AM A WRAPPER FUNCTION  <-- incorrect doc string
# print(add.__name__) #//=> wrapper                 <-- incorrect name
# help(add)  #//=> wrapper(*args, **kwargs)         <-- incorrect help output
                # I AM A WRAPPER FUNCTION


# Decorator Patter:
# Below solves the problem printing out doc strings or calling help() with decorators:
# - use the module "functools" and from it "wraps"
# wraps perserves a functions metadata
# when it is decorated
# this is good dev behavior to do so other devs can read/pullup your docs as expected
from functools import wraps
def log_function_data(fn):
    # call wraps here; it's parameter needs to match the function called into log_function_data()
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Reminder: the syntax below with 3 double quotes ("""statement""") returns the documentation between it.
        """I AM A WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)

    return wrapper

@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x+y

# print(add.__doc__) #//=> Adds two numbers together.     <-- correct doc string
# print(add.__name__) #//=> add                           <-- correct name
# help(add)  #//=>  add(x, y)                             <-- correct help output
                # Adds two numbers together.