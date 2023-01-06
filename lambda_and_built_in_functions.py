# import sys is used below in the generator expressions example
import sys
# import math to use fabs() method 
import math

# regular function 
def square(num):
    return num * num

# print(square(9)) #//=> 81

# same function as above (works the same way)
def square2(num): return num * num

# print(square2(9))  #//=> 81


# Lambda (a function that has no name; a lambda can only be one line; the expression "num * num" is automatically returned; sometimes called anonymous functions; it can be saved to a variable but not typically stored in a variable (this is an example of how it works))
square3 = lambda num: num * num

# print(square3(9))  #//=> 81

add = lambda a,b: a + b
# print(add(9,9))  #//=> 18

# print(square.__name__) #//=>  square
# print(square2.__name__) #//=>  square2
# print(square3.__name__) #//=>  <lambda>  (it has no name, it's just a lambda)
# print(add.__name__) #//=>  <lambda>  (it has no name, it's just a lambda)

# More Lambda Syntax examples:
# lambda parameters: body of function

add_values = lambda x,y: x + y
# print(add_values(10,20))  #//=> 30

multiply_values = lambda x,y: x * y
# print(multiply_values(10,20))  #//=> 200
#_____________________________________________________________

# map() (a standard function that accepts at least 2 arguments, a function and an iterable; it runs the lambda for each value in the iterable and returns a map object)

nums = [2,4,6,8,10]
# this uses lambda to double the numbers in nums
doubles = map(lambda x: x*2, nums)
# print(list(doubles)) #//=> [4, 8, 12, 16, 20]

# can also be written like:
doubles = list(map(lambda x: x*2, nums))
# print(doubles) #//=> [4, 8, 12, 16, 20]

people = ["Darcy", "Christina", "Dana", "Annabel"]

peeps = map(lambda name: name.upper(), people)
# print(list(peeps))  #//=> ['DARCY', 'CHRISTINA', 'DANA', 'ANNABEL']

names = [
    {"first": "Rusty", "last": "Steele"},
    {"first": "Colt", "last": "Steele"},
    {"first": "Blue", "last": "Steele"}
]
# for x (each dictionary), x["first"] gives the value of the key of first
first_names = list(map(lambda x: x["first"], names))
# print(first_names) #//=>  ['Rusty', 'Colt', 'Blue']
#_____________________________________________________________

# Practice exercise 1.
# Map Time Exercise
# Write a function called decrement_list  that accepts a single list of numbers as a parameter.  It should return a copy of the list where each item has been decremented by one. Use map to do this! For example:
# decrement_list([1,2,3])   #[0,1,2]
# decrement_list([20,14,11])  #[19,13,10]
# Tips:
# Remember map doesn't return a list on its own.  decrement_list , however, should return a list.
# You can either pass map another name function or use a lambda.  A lambda is preferable, even if it is a little scary looking.
def decrement_list(collection):
    return list(map(lambda x: x-1, collection))

# print(decrement_list([1,2,3]))  #//=> [0, 1, 2]
#_____________________________________________________________

# filter() (filters out particular items that we want based on a condition; anytime we use filter it needs to return True or False; the True/False is how filter decides what to put in the new list):

collection = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, collection))
# print(evens)  #//=> [2,4]

names2 = ["austin", "penny", "anthony", "angel", "billy"]
# filters out into a new list only names who's first character equal "a"
a_names2 = filter(lambda n: n[0] == "a", names2)
# print(list(a_names2))  #//=> ['austin', 'anthony', 'angel']



users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
# if the list length is 0, filter out those users into a new list
inactive_users3 = list(filter(lambda u: len(u["tweets"]) == 0, users))
# print(inactive_users3)  #//=> [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]
# or
# if the list length is Falsy (use "not"), filter out those users into a new list
inactive_users = list(filter(lambda u: not u['tweets'], users))
# print(inactive_users)  #//=> [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]
# print(inactive_users2) #//=> [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]

# extract usernames of inactive users w/ map and filter:
# map is the first argument using lambda, and filter is the second argument (within filter is lambda); basically map is iterating through the filtered list
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))
# print(usernames) #//=> ['JEFF', 'BOB123', 'GUITAR_GAL']

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]

# Return a new list with the string "Your instructor is " + each value in the names3 array, but only if the value is less than 5 characters (using filter and map)
names3 = ["Lassie", "Colt", "Rusty"]

instructor = list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) < 5, names3)))
# print(instructor)  #//=> ['Your instructor is Colt']
# or using list comprehension
instructor2 = [f"Your instructor is {name}" for name in names3 if len(name) <5]
# print(instructor2) #//=> ['Your instructor is Colt']
#_____________________________________________________________

# Practice exercise 2.
# Filter Exercise!
# Write a function called remove_negatives that accepts a list of numbers and returns a copy of the lists with all negative numbers removed. Use filter() in your implementation, not a list comprehension!
# remove_negatives([-1,3,4,-99])     #[3,4]
# remove_negatives([-7,0,1,2,3,4,5])      #[0, 1, 2, 3, 4, 5]
# remove_negatives([50,60,70])   #[50,60,70]
# HINTS
# Make sure you return a list!  Remember filter does not return a list! You have to convert the result to a list yourself.
# Note that 0 is not considered negative, so it should not be filtered out!
def remove_negatives(lst):
    return list(filter(lambda num: num >= 0, lst))

# print(remove_negatives([-1,3,4,-99])) #//=> [3, 4]
#_____________________________________________________________

# all() (returns True if all elements of the iterable are truthy (or if the iterable is empty)):
all([0,1,2,3]) #//=> False

all([char for char in "eio" if char in "aeiou"])  #//=> True

all([num for num in [4,2,10,6,8] if num % 2 == 0])  #//=> True

people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
all([name[0] == "C" for name in people]) #//=> True

nums2 = [2, 60, 26, 18]
all([num % 2 == 0 for num in nums2]) #//=> True

# any() (returns True if any element of the iterable is truthy. If the iterable is empty, returns False).
any([0,1,2,3]) #//=> True
any([val for val in [1,2,3] if val > 2]) #//=> True
any([val for val in [1,2,3] if val > 5]) #//=> False

nums3 = [2, 60, 26, 18, 21]
any([num % 2 != 0 for num in nums3])  #//=> True
any([num % 2 == 0 for num in nums3])  #//=> True
#_____________________________________________________________

# Generator Expression
# below: this all() method without the list comprehension still returns true, so the list part is not needed
people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
all(name[0] == "C" for name in people) #//=> True

# below is a lighter weight version of a list (can't do things like .append(); it can be used if we don't actually want a list at the end of what we're doing; it saves memory)
(name[0] == "C" for name in people) #//=> <generator object <genexpr> at 0x1002d7510>

# A simple comparison of size (in Bytes)
#  "sys" module used; it's imported at the top of the page
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

# print("To do the same thing, it takes...")  #//=> To do the same thing, it takes...
# print(f"List Comprehension: {list_comp} bytes")  #//=> List Comprehension: 8856 bytes
# print(f"Generator Expression: {gen_exp} bytes")  #//=> Generator Expression: 208 bytes
#_____________________________________________________________

# Practice exercise 3. 
# Any/All Exercise
# Implement a function is_all_strings  that accepts a single iterable and returns True if it contains ONLY strings.  Otherwise, it should return false.  
# is_all_strings(['a', 'b', 'c'])  #True
# is_all_strings([2,'a', 'b', 'c'])  #False
# is_all_strings(('hello', 'goodbye'))  #True
def is_all_strings(lst):
    return all([type(l) == str for l in lst])

# print(is_all_strings(['a', 'b', 'c']))  #//=> True
#_____________________________________________________________

# sorted() (a built-in function that works with other iterable collections other than lists (ie. tuple); returns a new sorted list from the items in iterable); works on anything iterable:
# sorted on lists:
more_numbers = [6,1,8,2]
# print(sorted(more_numbers)) #//=> [1, 2, 6, 8]

nums4 = [4,6,1,30,55,23]
nums4.sort()  #//=>  [1, 4, 6, 23, 30, 55]; nums4 is sorted in place (the variable nums4 is changed to a sorted list)
sorted(nums4)  #//=>  [1, 4, 6, 23, 30, 55]; nums4 is not changed (the original variable nums4 remains the same)
sorted(nums4, reverse= True)  #//=>  [55, 30, 23, 6, 4, 1]

#sorted on tuples:
sorted((2,1,45,23,99))  #//=> [1, 2, 23, 45, 99]

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# print(sorted(users, key= len)) #//=> [{'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']}, {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best', "I'm hungry"]}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'jeff', 'tweets': [], 'color': 'purple'}, {'username': 'bob123', 'tweets': [], 'num': 10, 'color': 'teal'}]  (everything is sorted from shortest dictionary to longest)

# sorted by username with lambda
# the key to sort off of is the user, username, for each user:

# print(sorted(users, key= lambda user: user["username"]))  #//=> [{'username': 'bob123', 'tweets': [], 'num': 10, 'color': 'teal'}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best', "I'm hungry"]}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'jeff', 'tweets': [], 'color': 'purple'}, {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']}]

# sorted by tweets using lambda
# print(sorted(users, key= lambda user: len(user["tweets"])))  #//=> [{'username': 'jeff', 'tweets': [], 'color': 'purple'}, {'username': 'bob123', 'tweets': [], 'num': 10, 'color': 'teal'}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best', "I'm hungry"]}, {'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']}]

# reversed sort by tweets using lambda
# print(sorted(users, key= lambda user: len(user["tweets"]), reverse=True))  #//=> [{'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best', "I'm hungry"]}, {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'jeff', 'tweets': [], 'color': 'purple'}, {'username': 'bob123', 'tweets': [], 'num': 10, 'color': 'teal'}, {'username': 'guitar_gal', 'tweets': []}]

songs = [
    {"title": "happy birthay", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# sorted by playcount:
# print(sorted(songs, key= lambda song: song["playcount"]))  #//=> [{'title': 'happy birthay', 'playcount': 1}, {'title': 'Survive', 'playcount': 6}, {'title': 'Toxic', 'playcount': 31}, {'title': 'YMCA', 'playcount': 99}]

# print(sorted(songs, key= lambda song: song["playcount"], reverse= True))  #//=> [{'title': 'YMCA', 'playcount': 99}, {'title': 'Toxic', 'playcount': 31}, {'title': 'Survive', 'playcount': 6}, {'title': 'happy birthay', 'playcount': 1}]
#_____________________________________________________________

# max() (return the largest item in an iterable or the largest of two or more arguments):
# min() (return the smallest item in an iterable or the smallest of two or more arguments):
max(3, 67, 99) #//=> 99
max("c", "d", "a")  #//=> 'd'
max([3,4,1,2])  #//=> 4
max((1,2,3,4))  #//=> 4
max(("awesome"))  #//=> 'w'
max({1: "a", 3: "c", 2: "b"})  #//=> 3

nums5 = [40, 32, 6, 5, 10]
max(nums5)  #//=> 40
min(nums5)  #//=> 5
max("hello world")  #//=> 'w'
min("hello world")  #//=> ' '
# max on a tuple:
max((3,5,23,65)) #//=> 65



names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
min(len(name) for name in names) # 3

# find the longest name itself
max(names, key=lambda n:len(n)) #Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the song with the highest playcount
max(songs, key=lambda s: s['playcount']) #{"title": "YMCA", "playcount": 99=}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #"YMCA"
#_____________________________________________________________

# Practice exercise 4.
# Extremes Exercise - Using Min and Max
# Write a function called extremes  which accepts an iterable. It should return a tuple containing the minimum and maximum elements.  For example:
# extremes([1,2,3,4,5])  # (1, 5)
# extremes((99,25,30,-7))  # (-7, 99)
# extremes("alcatraz")  #( 'a', 'z')
# REMEMBER, RETURN A TUPLE!!!
def extremes(lst):
    return (min(lst), max(lst))

# print(extremes([1,2,3,4,5])) #//=> (1,5)
#_____________________________________________________________

# reversed() (returns a reverse iterator; can iterate over things):
reversed([1,2,3,4,5]) #//=> <list_reverseiterator object at 0x1022d80d0>
list(reversed([1,2,3,4,5])) #//=>  [5, 4, 3, 2, 1]

# use reversed if you were iterating over something in reverse:
# for char in reversed("hello world"):
# 	print(char) #//=> d
# 					# l
# 					# r
# 					# o
# 					# w
					
# 					# o
# 					# l
# 					# l
# 					# e
# 					# h
# 					# a

# for x in reversed(range(0,10)):
# 	print(x) #//=> 9
# 				# 8
# 				# 7
# 				# 6
# 				# 5
# 				# 4
# 				# 3
# 				# 2
# 				# 1
# 				# 0

reversed("hello")  #//=> <reversed object at 0x1022d80d0>
list(reversed("hello"))  #//=> ['o', 'l', 'l', 'e', 'h']
"".join(list(reversed("hello")))  #//=> 'olleh'
#_____________________________________________________________

# len() (return the length (number of itmes) of an object.  The argument may be a sequence (string, tuple, list, or range) or a collection (dictionary, set)):
# len with a string
len("awesome") #//=> 7
# len with a tuple
len((1,2,3,4)) #//=> 4
# len with a list
len([1,2,3,4]) #//=> 4
# len with a range
len(range(0,10)) #//=> 10

# len with a dictionary
len({"a": 1, "b": 2, "c": 3}) #//=> 3
# len with a set
len({1,2,3,4}) #//=> 4
#_____________________________________________________________

# abs() (return the absolute value of a number.  The argument may be an integer or a floating point number; in math, the absolute value of a positive number is always that number, and the absolute value of a negative number, is that numbers positive):
abs(-5)  #//=> 5
abs(5)  #//=> 5

abs(3.44444)  #//=> 3.44444
abs(-3.44444)  #//=> 3.44444

# abs("20") #//=> TypeError: bad operand type for abs(): 'str'
abs(float("20")) #//=> 20.0
abs(int("20")) #//=> 20

# fabs() (float absolute value; does the exact same thing as abs() but treats everything as a float first; must import math (see import at the top of page))
# print(math.fabs(-4)) #//=> 4,0


# sum() (takes an iterable and an optional start; returns the sum of start and the items of an iterable from left to right and returns the total; start by default is 0):
sum([1,2,3]) #//=> 6
# sum with a positive number for start
sum([1,2,3], 10) #//=> 16
# sum with a negative number for start
sum([1,2,3], -6) #//=> 0
# sum with a tuple and floats
sum((1.5, 2, 3.7))  #//=> 7.2
# sum with a set containing numbers
sum({1,50,100})  #//=> 151

# sum with a list of strings (it trys to add the start 0, to the string and returns an error)
# sum(["hi", "there"])  #//=> TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sum(["hi", "there"], "lol")  #//=> TypeError: sum() can't sum strings [use ''.join(seq) instead]


# round() (return number rounded to ndigits precision after the decimal point.  If ndigits is omitted or is None, it returns the neraest integer to its input):
round(10.2)  #//=> 10
# round to 2 digits
round(1.212121, 2)  #//=> 1.21
round(3.51234)  #//=> 4
round(3.51234, 3)  #//=> 3.512
# round and specify None
round(3.51234, None)  #//=> 4

# floats are only precise up to so far
round(9.9999999999999999999999999999999999999999999, 15)  #//=> 10.0
#_____________________________________________________________

# Practice exercise 5.
# Greatest Magnitude Exercise
# Write a function max_magnitude  that accepts a single list full of numbers. It should return the magnitude of the number with the largest magnitude (the number that is furthest away from zero).
# max_magnitude([300, 20, -900])   #900
# max_magnitude([10, 11, 12])   #12
# max_magnitude([-5, -1, -89])   #89
# Hint: use max and abs!

# my solution:
def max_magnitude(lst):
    new_list = []
    for num in lst:
        new_list.append(abs(num))
    return max(new_list)

# print(max_magnitude([300, 20, -900])) #//=> 900

# alternative solution from instructor:
def max_magnitude2(nums):
    return max(abs(num) for num in nums)

# Practice exercise 6.
# sum_even_values
# Write a function called sum_even_values. This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2. If there are no numbers divisible by 2, the function should return 0.  To be clear, it accepts all the numbers as individual arguments!
# sum_even_values(1,2,3,4,5,6) # 12
# sum_even_values(4,2,1,10) # 16
# sum_even_values(1) # 0

# my solution:
def sum_even_values(*args):
    new_list = []
    for arg in args:
        if arg % 2 == 0:
            new_list.append(arg)
    return sum(new_list)

# print(sum_even_values(1,2,3,4,5,6)) #//=> 12
# print(sum_even_values(1)) #//=> 0

# alternative solution from instructor:
def sum_even_values2(*args):
    return sum(arg for arg in args if arg % 2 == 0)

# Practice exercise 7.
# sum_floats
# Write a function called sum_floats. This function should accept a variable number of arguments. The function should return the sum of all the parameters that are floats. If there are no floats the function should return 0

# my solution:
def sum_floats(*args):
    new_list = []
    for arg in args:
        if type(arg) == float:
            new_list.append(arg)
    return sum(new_list)
    pass

# print(sum_floats(1.5, 2.4, 'awesome', [], 1))  #//=> 3.9
# print(sum_floats(1,2,3,4,5))  #//=> 0

# alernative solution from instructor:
def sum_floats2(*args):
    return sum(arg for arg in args if type(arg) == float)
#_____________________________________________________________


# zip() (make an iterator that aggregates elements from each of the iterables; returns an iterator of tupoles, where the i-th tuple contains the i-th element from each of the argument sequences or iterables; the iterator stops when the shortest input iterable is exhausted) (another explanation: takes two lists of numbers of equal length, it makes a new list of pairings of first two numbers, then second two numbers, and so on; it zips them together)
first_zip = zip([1,2,3], [4,5,6])
list(first_zip)  #//=>  [(1, 4), (2, 5), (3, 6)]
dict(first_zip)  #//=>  {1: 4, 2: 5, 3: 6}

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
z = zip(nums1, nums2)  #//=> <zip object at 0x104346500>
list(z) #//=> [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
dict(z) #//=> {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}

# it goes from left to right
z = zip(nums2, nums1)
list(z) #//=> [(6, 1), (7, 2), (8, 3), (9, 4), (10, 5)]
dict(z) #//=> {6: 1, 7: 2, 8: 3, 9: 4, 10: 5}

# lists don't have to be exactly the same length:
nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10,11,12]
z = zip(nums1, nums2)
list(z) #//=> [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]  (it stops as soon as the shortest iterable is exhausted; we don't see 11 and 12)

# not limited to only 2 arguments for zip:
words = ["hi", "lol", "haha", ":)"]
list(zip(words, nums1, nums2)) #//=> [('hi', 1, 6), ('lol', 2, 7), ('haha', 3, 8), (':)', 4, 9)]  <-- a list of tuples with 3 elements each ("words" is the shortest so it stops when the end of "words is reached")

#  can use the * operator to unpack a list:
five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
list(zip(*five_by_two))  #//=>  [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
#_____________________________________________________________

# More Complex zip() examples:
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

# pair the final grades
final_grades1 = [pair for pair in zip(midterms, finals)]
# print(final_grades1)  #//=>[(80, 98), (91, 89), (78, 53)]
# get the max of the pairing
final_grades1 = [max(pair) for pair in zip(midterms, finals)]
# print(final_grades1)  #//=> [98, 91, 78]

# returns dict with {student:highest score} USING DICT COMP
# {student_name: max(midterms, finals), for every tuple in zip(students, midterms, finals)}
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
# print(final_grades) #//=> {'dan': 98, 'ang': 91, 'kate': 78}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
# enclose everything in a dictionary 
final_grades = dict(
	# zip(students with map(max(pair))
	zip(
		students,
		# inside map(use lambda function to find the max(pair) of the tuple(midterms, finals))
		map(
			lambda pair: max(pair),
			# zip the midterms and finals together
			zip(midterms, finals)
		)
	)
)
# print(final_grades)  #//=> {'dan': 98, 'ang': 91, 'kate': 78}

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
# enclose everything in a dictionary
avg_grades = dict(
	# zip(students with map(average of the pairs)
	zip(
		students,
		# inside map(use lambda function to find the average of index 0 and index 1), of the tuple(midterms, finals))
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			# zip the midterms and finals together
			zip(midterms, finals)
		)
	)
)
# print(avg_grades)  #//=> {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
#_____________________________________________________________

# Practice exercise 7.
# Interleaving Strings (kind of tough!)
# This challenge is a bit more involved than the others in this section.  Do not worry if you can't get it!
# Write a function interleave  that accepts two strings.  It should return a new string containing the 2 strings interwoven or zipped together. For example:
# interleave('hi','ha')    # 'hhia'
# interleave('aaa', 'zzz')  # 'azazaz'
# interleave('lzr','iad') #  'lizard'
#  This might seem like an easy task using zip , but in fact there are a couple intermediate steps to go from zip  back to a single string.  If you need help, I've written up a basic walkthrough of the steps:
# suppose we call interleave('hi', 'no')  
# zip  the two strings together, giving you a list of tuples (once you convert from the default zip_object) -  [('h','n'), ('i','o')]  
# For each of the tuples in the list, join them together using "".join  resulting in ['hn', 'io']  - Easiest if you use a list comp.  You need to join EACH tuple.
# Finally, join the items in the list together using "".join  again resulting in 'hnio'  
# Don't stress if you don't get this one!

# my solution:
def interleave(a, b):
    zip_str = list(zip(a,b))
    join_elements = ["".join(element) for element in zip_str]
    return "".join(join_elements)

# print(interleave('hi','ha')) #//=> hhia

# alternative solution from instructor:
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

# Practice example 8.
# triple_and_filter
# Write a function called triple_and_filter. This function should accept a list of numbers, filter out every number that is not divisible by 4, and return a new list where every remaining number is tripled.

# my solution:
def triple_and_filter(lst):
    divisible_by_four = list(filter(lambda num: num % 4 == 0, lst))
    return list(map(lambda x: x * 3, divisible_by_four))
    pass

# print(triple_and_filter([1,2,3,4])) #//=> [12]
# print(triple_and_filter([6,8,10,12])) #//=> [24, 36]

# alternative solution from instructor:
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

# Practice example 9.
# extract_full_name
# Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.

# instructors solution:
#takes a list as a parameter
def extract_full_name(l):
	# map(using lambda function the value of "first" and "last" in its own string, from the list parameter passed)
	# return the mapped outcome in a list()
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
# print(extract_full_name(names)) #//=> ['Elie Schoppik', 'Colt Steele']