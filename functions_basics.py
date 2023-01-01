# Function Structure:

# def name_of_function ():
    # block of runnable code

def say_hi():
    print("Hi")

# say_hi()

def sing_happy_birthday():
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday Dear you")
    print("Happy birthday to you")

# sing_happy_birthday()
#_____________________________________________________________

# Returning Values from Functions:

def print_square_of_7():
    print(7**2)

# print_square_of_7()

def square_of_7():
    return 7**2

result = square_of_7()
# print(result)
#_____________________________________________________________

#Exercise 1:

#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50) (you can use list comprehension or a for loop)
def generate_evens():
    numbers = range(1,50)
    evens = [num for num in numbers if num % 2 == 0]
    return evens

# print(generate_evens())

def generate_evens2():
    result = []
    for num in range(1,50):
        if num % 2 == 0:
            result.append(num)
    return result

# print(generate_evens2())
#_____________________________________________________________

# Using Parameters

def square(num):
    return num ** 2

# print(square(4))
# print(square(8))

def sing_happy_birthday2(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print(f"Happy birthday Dear {name}")
    print("Happy birthday to you")

# sing_happy_birthday2("Buddy")

def add(a,b):
    return a+b

# print(add(2,4))

def multiply(first,second):
    return first * second

# print(multiply(2,4))

def divide(num1, num2):
    return num1 / num2

# order matters when passing arguments into parameters
# print(divide(2,5)) #//=> 0.4
# print(divide(5,2))  #//=> 2.5
#_____________________________________________________________

# Exercise 2:
# Implement a function yell  which accepts a single string argument.  It should return(not print) an uppercased version of the string with an exclamation point aded at the end.  For example: yell("go away")   # "GO AWAY!"

# formatted with '.format()' method
def yell(str):
    return "{}!".format(str).upper()

# print(yell("hello"))

# formatted with F-Strings
def yell2(str):
    return f"{str}!".upper()

# print(yell2("hi"))
#_____________________________________________________________

# Common mistakes with Returning:

# 1. watch out for return keyword indentations

list_of_numbers = range(1,8)

# incorrect
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total  #//=> will only return the total after the first loop because return is inside the for loop (watch out for indentations!)

# print(sum_odd_numbers(list_of_numbers)) #//=> 1

# correct
def sum_odd_numbers2(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total  #//=> properly indented outside of the for loop and returns the expected total

# print(sum_odd_numbers2(list_of_numbers)) #//=> 16

# 2. Unnecessary "else"; unnecessary code

# the else statement is unnecessary
def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:
        return False

# print(is_odd_number(4))
# print(is_odd_number(9))

# revised version without the "else"
def is_odd_number2(num):
    if num % 2 != 0:
        return True
    return False

# print(is_odd_number2(4))
# print(is_odd_number2(9))
#_____________________________________________________________

# Default Parameters (giving parameters a default value):

def exponent(num, power=2):
    return num ** power

# print(exponent(2,3)) #//=> 8
# print(exponent(3,2)) #//=> 9
# print(exponent(7)) #//=> 49

def add(a=10, b=20):
    return a + b

# print(add())  #//=> 30
# print(add(1,10))  #//=> 11

# What can Default Parameters be?: anything (functions, lists, dictionaries, strings, booleans)

def add(a,b):
    return a + b

# default parameters have to go at the end (or every single parameter has a default value because arguments are passed to parameters in order)
def math(a,b, fn=add):
    return fn(a,b)

def subtract(a,b):
    return a - b


# print(math(2,2))  #//=> 4
# print(math(2,2, subtract))  #//=> 0
#_____________________________________________________________

# Exercise 3.

# Write a function called speak  that accepts a single parameter, animal.  
# If animal is "pig", it should return "oink". 
# If animal is "duck", it should return "quack".  
# If animal is "cat", it should return "meow"
# If animal is "dog", it should return "woof"
# If animal is anything else, it should return "?"
# If no animal is specified, it should default to "dog"

def speak(animal= "dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

# print(speak())

# refactored version:
def speak2(animal="dog"):
    # create dictionary that maps animal names to noises
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    # get the value of the key and set it to variable noise
    noise = noises.get(animal)
    # if noise is true return the value
    if noise:
        return noise
    # else return "?"
    return "?"

# print(speak2())
#_____________________________________________________________

# Keyword Arguments (allows us to specify only if we know the name of the parameters, so the order doesn't matter anymore):

def full_name(first, last):
    return f"Your name is {first} {last}"

# print(full_name(first= "Tunisia", last="Artope")) #//=> "Your name is Tunisia Artope"
# print(full_name(last= "Artope", first="Tunisia")) #//=> "Your name is Tunisia Artope"
# print(full_name("Tunisia", "Artope")) #//=> "Your name is Tunisia Artope"

def exponent2(num, power=2):
    return num ** power

# print(exponent2(4,3)) #//=> 64
# print(exponent2(num= 4, power= 3))  #//=> 64
# # the order doesn't matter with keyword arguments:
# print(exponent2(power= 3, num= 4))  #//=> 64
#_____________________________________________________________

# Scope:

# global
# the increment function can't CHANGE the global variable "total", therefore you get the error message below:
total = 0

def increment():
    total += 1
    return total

# print(increment())  #//=> UnboundLocalError: cannot access local variable 'total' where it is not associated with a value

# corrected function: if a function must use a global variable, use the "global" keyword inside the function
def increment2():
    # use the "global" keyword in order to manipulate "total" variable in global scope
    global total
    total += 1
    return total

# print(increment2())  #//=> 1

# global variables can be accessed but not CHANGED; must use "global" keyword to manipulate the global variable
name = "Rusty"

def greet():
    print(name)

# print(greet())  #//=> Rusty

# nonlocal (lets us modify a parent's variables in a child (aka nested) function)
def out():
    count = 0
    def inner():
        # use "nonlocal" to manipulate variable that's in the parent scope
        nonlocal count
        count += 1
        return count
    return inner()
#_____________________________________________________________

# Documenting functions: use """ """ (triple double quotes)
def say_hello():
    """ A simple function that returns the string hello"""
    return "Hello!"

#this syntax retrieves what's in the triple double quotes
print(say_hello.__doc__) #//=> A simple function that returns the string hello

def exponent3(num, power=2):
    """exponent(num,power) raises num to specified power. Power defaults of 2."""
    return num ** power

print(exponent3.__doc__) #//=> exponent(num,power) raises num to specified power. Power defaults of 2. 
#_____________________________________________________________

# More practice exercises:

# 1. Write a function called product that accepts two parameters and returns the product of the two parameters (multiply them together)
def product(a, b):
    return a * b

# 2. Write a function called return_day. this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return None. Hint: store the days of the week in a list (or dict using numbers as keys).
def return_day(num):
    days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
    days = days.get(num)
    if num < 1 or num > 7:
        return None
    return days

# 3. Write a function called last_element. This function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.
def last_element(list):
    if len(list) == 0:
        return None
    return list[-1]

# 4. Write a function called number_compare. This function takes in two parameters (both numbers). If the first is greater than the second, this function returns "First is greater" If the second number is greater than the first, the function returns "Second is greater" Otherwise the function returns "Numbers are equal"
def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater"
    elif num2 > num1:
        return "Second is greater"
    else:
        return "Numbers are equal"

# 5. Write a function called single_letter_count. This function takes in two parameters (two strings). The first parameter should be a word and the second should be a letter. The function returns the number of times that letter appears in the word. The function should be case insensitive (does not matter if the input is lowercase or uppercase). If the letter is not found in the word, the function should return 0.  Hint: take advantage of count() method
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

# 6. Write a function called multiple_letter_count. This function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the values being the count of the letter.  Hint: use a dictionary comprehension and count(). Here's how it should work: multiple_letter_count("awesome")   # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
def multiple_letter_count(str):
    return {letter: str.count(letter) for letter in str}

# 7. Write a function called list_manipulation. This function should take in four parameters (a list, command, location and value).
# If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
# If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
# If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
# If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list
def list_manipulation(list, command, location, value=None):
    if(command == "remove" and location == "end"):
        return list.pop()
    elif(command == "remove" and location == "beginning"):
        return list.pop(0)
    elif(command == "add" and location == "beginning"):
        # must return list separately from insert for function to work (?)
        list.insert(0, value)
        return list
    elif(command == "add" and location == "end"):
        # must return list separately from append for function to work (?)
        list.append(value)
        return list

