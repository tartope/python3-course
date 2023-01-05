# import sys is used below in the generator expressions example
import sys

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

# Map (a standard function that accepts at least 2 arguments, a function and an iterable; it runs the lambda for each value in the iterable and returns a map object)

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

# Filter (filters out particular items that we want based on a condition; anytime we use filter it needs to return True or False; the True/False is how filter decides what to put in the new list):

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

# all (returns True if all elements of the iterable are truthy (or if the iterable is empty)):
all([0,1,2,3]) #//=> False

all([char for char in "eio" if char in "aeiou"])  #//=> True

all([num for num in [4,2,10,6,8] if num % 2 == 0])  #//=> True

people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
all([name[0] == "C" for name in people]) #//=> True

nums2 = [2, 60, 26, 18]
all([num % 2 == 0 for num in nums2]) #//=> True

# any (returns True if any element of the iterable is truthy. If the iterable is empty, returns False).
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

# sorted (a built-in function that works with other iterable collections other than lists (ie. tuple); returns a new sorted list from the items in iterable); works on anything iterable:
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

# max (return the largest item in an iterable or the largest of two or more arguments):
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

print(extremes([1,2,3,4,5])) #//=> (1,5)