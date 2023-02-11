from random import choice
from functools import wraps
from time import time
from time import sleep

# Higher Order Funtion (a function that returns another function from inside, or accepts one or more functions as an argument):
# - Example 1: a type of higer order function (passing functions as arguments)
# def sum(n, func):
#     # make a total variable to return and start at zero
#     total = 0
#     # loop through for every number in range
#     for num in range(n):
#         # square it with the square function, and add it to total
#         total += func(num)
#     # return total
#     return total

# def square(x):
#     return x*x

# def cube(x):
#     return x*x*x

# print(sum(3,square))  #//=> 5  <-- 0+1+4 = 5
# print(sum(3,cube)) #//=> 9  <-- 0+1+8 = 9


# - Example 2: nesting a function within a function and returning the result of that function combined with something else
#  ** import at top of page (from random import choice)

# def greet(person):
#     # greet() calls get_mood()
#     def get_mood():
#         # set msg to choice of 3 statements
#         msg = choice(('Hello there ', 'Go away ', 'I love you '))
#         # return msg
#         return msg
    
#     # set result to concat of get_mood() and person
#     result = get_mood() + person
#     # return result
#     return result

# print(greet("Toby")) #//=> Hello there Toby

# Example 3: nesting functions and returning functions from other functions
# def make_laugh_func():
#     # make_laugh_func() calls get_laugh()
#     def get_laugh():
#         # set laugh to choice of 3
#         l = choice(("HAHAHA", "lol", "tehehe"))
#         # return laugh
#         return l

#     # returns entire get_laugh() function
#     return get_laugh

# set make_laugh_func() to variable, and print variable
# laugh = make_laugh_func()
# print(laugh()) #//=> HAHAHA

# Example 4:
# def make_laugh_at_func(person):
#     def get_laugh():
#         laugh = choice(("HAHAHA", "lol", "tehehe"))
#         return f"{laugh} {person}"

#     return get_laugh()

# laugh_at = make_laugh_at_func("Linda")
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
# def be_polite(fn):
#     # the wrapper does something first, then does the function passed in (greet()), and then does something else
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")

#     return wrapper

# @be_polite
# def greet():
#     print("My name is Buddy.")

# @be_polite
# def rage():
#     print("I don't like you!")

# When the decorator is added (ie. syntactic sugar), we don't need to set "greet = be_polite(greet)", we can just call "greet()"
# print(greet()) #//=>  gives the same output as above
# print(rage()) #//=>  gives the same output as above
#_____________________________________________________________

# Decorator Syntax (the function being wrapped is passed a parameter):
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()

#     return wrapper

# def shout(fn):
#     def wrapper(*args, **kwargs):
#         return fn(*args, **kwargs).upper()

#     return wrapper

# @shout
# def greet(name):
#     return f"Hi, I'm {name}."

# @shout
# def order(main, side):
#     return f"Hi, I'd like the {main}, with a side of {side}, please."

# @shout
# def lol():
#     return "lol"

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


# Decorator Pattern:
# Below solves the problem printing out doc strings or calling help() with decorators:
# - use the module "functools" and from it "wraps"
# wraps perserves a functions metadata
# when it is decorated
# this is good dev behavior to do so other devs can read/pullup your docs as expected

# ** import at top of page (from functools import wraps)
# def log_function_data(fn):
#     # call wraps here; it's parameter needs to match the function called into log_function_data()
#     @wraps(fn)
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

# print(add.__doc__) #//=> Adds two numbers together.     <-- correct doc string
# print(add.__name__) #//=> add                           <-- correct name
# help(add)  #//=>  add(x, y)                             <-- correct help output
                # Adds two numbers together.
#_____________________________________________________________

# Building a speed test decorator:
# example 1.
# below tests generator expressions speed; without using decorators; not as clean as example 2:

# ** import at top of page (from time import time)
# SUMMING 10,000,000 Digits With Generator Expression
# gen_start_time = time() # save start time
# print(sum(n for n in range(100000000)))
# gen_time = time() - gen_start_time # end time - start time

# # SUMMING 10,000,000 Digits With List Comprehension 
# list_start_time = time()
# print(sum([n for n in range(100000000)]))
# list_time = time() - list_start_time


# print(f"sum(n for n in range(10000000)) took: {gen_time}")
# print(f"sum([n for n in range(10000000)]) took: {list_time}")
# first two print statements and last two print statements:
# 4999999950000000
# 4999999950000000
# sum(n for n in range(10000000)) took: 2.569303035736084
# sum([n for n in range(10000000)]) took: 4.191172122955322

# example 2.
# below speed tests function using decorator; cleaner than above code:

# ** import at top of page (from functools import wraps)
# def speed_test(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         result = fn(*args, **kwargs)
#         end_time = time()
#         print(f"Executing {fn.__name__}")
#         print(f"Time Elapsed: {end_time - start_time}")
#         return result
    
#     return wrapper

# @speed_test
# def sum_nums_gen():
#     return sum(x for x in range(90000000))

# @speed_test
# def sum_nums_list():
#     return sum([x for x in range(90000000)])

# print(sum_nums_gen()) #//=> Executing sum_nums_gen
#                         # Time Elapsed: 2.1190221309661865
#                         # 4049999955000000
# print(sum_nums_list()) #//=> Executing sum_nums_list
#                         # Time Elapsed: 3.9902279376983643
#                         # 4049999955000000
#_____________________________________________________________


# Practice example 1.
# show_args
# Write a function called show_args which accepts a function and returns another function. Before invoking the function passed to it, show_args should be responsible for printing two things: a tuple of the positional arguments, and a dictionary of the keyword arguments.

# ** import at top of page (from functools import wraps)
# def show_args(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("Here are the args:", args)
#         print("Here are the kwargs:", kwargs)
#         return fn(*args, **kwargs)
#     return wrapper

# @show_args
# def do_nothing(*args, **kwargs):
#     pass

# print(do_nothing(1,2,3,a= "hi", b= "bye"))  #//=>  Here are the args: (1, 2, 3)
                                                #  Here are the kwargs: {'a': 'hi', 'b': 'bye'}
#_____________________________________________________________

# Ensuring Args with a decorator:
# - another common use case with decorators is to enforce certain restrictions on arguments
# examples:
# - make a decorator that prevented a function from being called with any keyword argument
# - or prevent a function from being called with any numerical argument

# ** import at top of page (from functools import wraps)
# def ensure_no_kwargs(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             raise ValueError("No kwargs allowed!")
#         return fn(*args, **kwargs)

#     return wrapper

# @ensure_no_kwargs
# def greet(name):
#     print(f"Hi there, {name}")

# print(greet("Tony"))  #//=>  Hi there, Tony
# print(greet(name= "Tony"))  #//=>  ValueError: No kwargs allowed!
#_____________________________________________________________

# Practice Example 2.
# double_return
# Write a function called double_return which accepts a function and returns another function. double_return should decorate a function by returning two copies of the inner function's return value inside of a list.

# ** import at top of page (from functools import wraps)
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
        
    return wrapper

@double_return 
def add(x, y):
    return x + y

@double_return
def greet(name):
    return "Hi, I'm " + name

# print(add(1, 2)) # [3, 3]
# print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]
#_____________________________________________________________

# Practice Example 3.
# ensure_fewer_than_three_args
# Write a function called ensure_fewer_than_three_args which accepts a function and returns another function. The function passed to it should only be invoked if there are fewer than three positional arguments passed to it. Otherwise, the inner function should return "Too many arguments!"

# ** import at top of page (from functools import wraps)
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

# print(add_all()) # 0
# print(add_all(1)) # 1
# print(add_all(1,2)) # 3
# print(add_all(1,2,3)) # "Too many arguments!"
# print(add_all(1,2,3,4,5,6)) # "Too many arguments!"
#_____________________________________________________________

# Practice Example 4.
# only_ints
# Write a function called only_ints which accepts a function and returns another function. The function passed to it should only be invoked if all of the arguments passed to it are integers. Otherwise the inner function should return "Please only invoke with integers."
# instructors code below:

# ** import at top of page (from functools import wraps)
def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
        
    return wrapper

@only_ints 
def add(x, y):
    return x + y
    
# print(add(1, 2)) # 3
# print(add("1", "2")) # "Please only invoke with integers."
#_____________________________________________________________

# Practice Example 5.
# ensure_authorized
# Write a function called ensure_authorized which accepts a function and returns another function. The function passed to it should only be invoked if there exists a keyword argument with a name of "role" and a value of "admin". Otherwise, the inner function should return "Unauthorized"

# ** import at top of page (from functools import wraps)
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

# print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
# print(show_secrets(role="nobody")) # "Unauthorized"
# print(show_secrets(a="b")) # "Unauthorized"
#_____________________________________________________________

# Writing and ensuring first arg is Decorator:
# Create decorators that take an argument

# NOT WORKING CODE:
# When we write:
# @decorator
# def func(*args, **kwargs):
#     pass
# # We're really doing:
# func = decorator(func)

# When we write:
# @decorator_with_args(args)
# def func(*args, **kwargs):
#     pass
# # We're really doing:
# func = decorator_with_args(arg)(func)
#---------------------------------------
# the real code example below:

# ** import at top of page (from functools import wraps)
# for this, we pass in a value/arg, not a fn, as a parameter
def ensure_first_arg_is(value):
    # this inner function actually takes the fn parameter (the name "inner" doesn't matter); this is the decorator
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # if args exist and the first arg is not equal to value passed, return the sentence below
            if args and args[0] != value:
                return f"First arg needs to be {value}"
            # else, return the fn
            return fn(*args, **kwargs)
        # return the wrapper
        return wrapper
    # return the inner function
    return inner

@ensure_first_arg_is("burrito")
# *foods replaces *args (name doesn't matter)
def fav_foods(*foods):
    print(foods)

# print(fav_foods("burrito", "ice cream"))  #//=> ('burrito', 'ice cream')  <-- REMINDER: returns a tuple because args is a tuple
# print(fav_foods("ice cream", "burrito"))  #//=> First arg needs to be burrito

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

# print(add_to_ten(10,12))  #//=> 22
# print(add_to_ten(1,2))  #//=> First arg needs to be 10
#_____________________________________________________________

# Enforcing Argument Types with A:
# changing the arguments to string if not a string, and int if not an int

# the outer func that takes the value (*types) as a parameter
def enforce(*types):
    # the inner function actually takes the fn parameter
    def decorator(fn):
        def new_func(*args, **kwargs):
            # args are tuples and immutable so convert to list which is mutable
            newargs = []
            # zip together the argument with type, ie: ("hello", str) (5, int)
            for(a, t) in zip(args, types):
                # cast each argument with the type and append to newargs, ie: ["hello", 5]
                newargs.append(t(a))
            # return the fn passed in but with newargs
            return fn(*newargs, **kwargs)
        return new_func
    return decorator

# pass types wanted as paratmeters
@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a,b):
    print(a / b)

# two strings passed as arguments, changed to appropriate type
# print(repeat_msg("hello", "5")) #//=> hello
                                    # hello
                                    # hello
                                    # hello
                                    # hello

# two ints passed as arguments, changed to appropriate type
# print(divide(1,2)) #//=> 0.5
# two strings passed as arguments, changed to appropriate type
# print(divide("1", "4")) #//=> 0.25
#_____________________________________________________________

# Practice Example 6.
# delay
# Write a function called delay which accepts a time and returns an inner function that accepts a function. When used as a decorator, delay will wait to execute the function being decorated by the amount of time passed into it. Before starting the timer, delay will also print a message informing the user that there will be a delay before the decorated function gets run.
# (Hint: take a look at the sleep function from the built-in time module if you want to pause code execution for a certain amount of time.)

# ** import at top of page (from time import sleep)
# ** import at top of page (from functools import wraps)
def delay(value):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running say_hi".format(value))
            sleep(value)
            return fn(*args,**kwargs)
        return wrapper
    return inner

@delay(10)
def say_hi():
    return "hi"

print(say_hi()) #//=> Waiting 3s before running say_hi
                    # hi