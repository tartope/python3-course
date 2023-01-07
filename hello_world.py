# use 'python3' to open a REPL and 'cmd+D' or 'quit()' to exit.
# use 'python3 <fileName>' to run code in terminal.
# open REPL and use 'help(method name)' to get info on that method (ie. help(list)).
# use 'type(variable name)' to get data type of the value in that variable.

# print('Hello World!')
# print('Goodbye World!')
#__________________________

# variables can be assigned at the same time as other variables:
# all, at, once = 5, 10, 15
#__________________________

# 'None' seems to be similar to JS 'null':
# child = None
# print(child)
# child = "Buddy"
# print(child)
#__________________________

# whether using single or double quotes, stay consistent (doesn't ruin the program, but just a stylistic thing):
# name = "Buddy"
# name2 = 'Buddy'
# message = "He said 'Hello there!'"
# message2 = 'He said "Hello there!"'
#__________________________

# String Escape Sequences:

# creates a new line:
# new_line = "hello \nworld"
# print(new_line)

# prints out the backslash symbol:
# back_slash = "this is a backslash: \\"
# print(back_slash)

# removes the character behind it:
# back_space = "hel\blo"
# print(back_space)

# double, double quotes (same thing with single quotes):
# message = "He said \"Hello there!\""
# print(message)
#__________________________

# concatenation:
# string_one = "Hello"
# string_two = "Buddy"
# print(string_one + " " + string_two)

# can use '+=' operator with strings:
# string_one = "ice"
# string_one += " cream"
# print(string_one)

# people = 99
# people += 1
# print(people)
# people -= 10
# print(people)
# people *= 10
# print(people)
#__________________________

# formating strings/interpolate variables (using F-Strings, the new way (Python 3.6+)):
# x = 10
# formatted = f"I've told you {x} times already!"
# print(formatted)

# guess = 8
# print(f"Your guess of {guess} was incorrect.")
# print(f"Your guess of {guess + 1} was incorrect.")
# name = "Buddy"
# print(f"Nice try {name} but your guess of {guess} was incorrect.")

# formating strings/interpolate variables (using '.format()' method, the old way(Python 2 -> 3.5)):
# formatted2 = "I've told you {} times already!".format(10)
# print(formatted2)

# formating strings/interpolate variables (using '.format method', the old old way '% operator(deprecated)):
# formatted3 = "I've told you %d times already!" % (x)
# print(formatted3)
#__________________________

# strings and indexes:
# "lol" this string is indexed (each character has a number that starts at 0, and can be accessed using that number)
# name = "Buddy"
# print(name[0])
# print(name[1])

# negative numbers returns the character from the end of the string:
# print(name[-1])
# print(name[-2])
#__________________________

# converting data types:
# decimal = 12.56345634534
# integer = int(decimal)
# print(integer)

# my_list = [1, 2, 3]
# my_list_as_a_string = str(my_list)
# print(my_list_as_a_string)      # //=> "[1, 2, 3]"

# num = 12
# print(type(num))
# num = float(num)
# print(type(num))
# print(num)

# print(int(99.99))
# print(str(8))       # //=> "8"
#__________________________
