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