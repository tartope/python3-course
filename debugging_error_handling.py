# import pdb

# Raise keyword: use this keyword to "raise" errors

# the keyword "raise", then error type, then an optional argument/string to explain the error
# raise ValueError('invalid value') 

# raise ValueError

# raise NameError("blahblah")

def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")

    # better to separate all possible Errors to easily determine the cause of the error:

    # if color is not a string, then raise TypeError
    if type(color) is not str:
        raise TypeError("color must be instance of string")

    # if text is not a string, then raise TypeError
    if type(text) is not str:
        raise TypeError("text must be instance of string")

    # if trying to call colorize with a color that is not in "colors", then raise a ValueError
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

# colorize("hello", "red")  #//=> Printed hello in red
# colorize(34, "red")  #//=> TypeError: text must be instance of string

# result after adding "colors" tuple and ValueError
# colorize("hello", "red")  #//=> ValueError: color is invalid color

# colorize("hello", 10)  #//=> TypeError: color must be instance of string
# colorize([], "cyan")  #//=> TypeError: text must be instance of string
#_______________________________________________________________

# Handle Errors: in Python, it's strongly encouraged to use try/except blocks, to catch exceptions when we can do something about them:

# foobar is undefined so it raises a NameError and no code that is after will be run:
# foobar #//=> NameError: name 'foobar' is not defined

# put foobar in a try/except block. the block raises and error if there's an exception; without the try/except block the code would break and nothing else would run; with the try/except block, nothing breaks, and the code after it is run (ie. "after the try" is run)
# try:
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")

# try:
#     buddy
# except NameError:
#     print("You tried to use a variable that was never declared!")

d = {"name": "Ricky"}
# d["city"]  #//=>  KeyError: 'city'  (because the key "city" does not exist)

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

# print(get(d, "name")) #//=> Ricky
# print(get(d, "city")) #//=> None
#_______________________________________________________________

# Try, Except, Else, and Finally:

# try:
#     num = int(input("please enter a number: "))
# except:
#     print("That's not a number!")
# else:
#     print("I'M IN THE ELSE!")
# finally:
#     print("RUNS NOT MATTER WHAT!")

# entering 10 doesn't break the code; and "else" will run when "except" does not
# entering a letter returns the error message #//=> That's not a number!
# "try" will run. if there's a problem "except" will run.  if there's not a problem "else" will run. "finally" will run no mater what.
#_______________________________________________________________

# a guessing game might look like below; if a user continues to enter the wrong input, they will be prompted until they enter the correct input, then the loop will break and the remaining code will run.
# while True:
#     try:
#         num = int(input("please enter a number: "))
#     except ValueError:
#         print("That's not a number!")
#     else:
#         print("Good job, you entered a number!")
#         break
#     finally:
#         print("RUNS NOT MATTER WHAT!")

# print("Rest of game logic runs!")
#_______________________________________________________________

# def divide(a, b):
#     try:
#         return a / b
#     except:
#         print("something went wrong...")

# print(divide(1,2))  #//=> 0.5
# print(divide(1,0))  #//=> something went wrong...
#                     #//=> None <-- because we tried to print something and nothing came back

# or:
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("don't divide by zero please")
#     except TypeError:
#         print("a and b must be ints or floats")

# print(divide(1,2))  #//=> 0.5
# print(divide(1,0))  #//=> don't divide by zero please
#                     #//=> None <-- because we tried to print something and nothing came back
# print(divide(1, "a")) #//=> a and b must be ints or floats

#or
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("don't divide by zero please")
    # if we want the error itself that is being triggered, add "as err" then "print(err)"
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

# print(divide(1,2))  #//=> 1 divided by 2 is 0.5
# print(divide(1, "a")) #//=> a and b must be ints or floats
                        #//=> unsupported operand type(s) for /: 'int' and 'str'  <-- this is from the "as err"/"print(err)" lines
                        #//=> None  <-- because we tried to print something and nothing came back
#_______________________________________________________________

# Debugging with PDB (Python Debugger); used when an unexpected error is encountered.
# it's a module that has to be imported

#import pdb at top of page; then "pdb.set_trace()" is placed wherever you want the code to stop. run the file to start the debugger
# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging) (also used to quit the debugger)

# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)

#or

# def add_numbers(a, b, c, d):  #<-- if you have values that conflict wiht the commands use "p c" (print c)
#     import pdb; pdb.set_trace()  #<-- commonly seen; can do multiple lines on one line but must add the semicolon

#     return a + b + c + d

# add_numbers(1,2,3,4)  #<-- PDB does not run until the function is executed/called
#_______________________________________________________________

# Practice example 1.
# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct type of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples
    
    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"

def divide(num1, num2):
    try:
        result = num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return result