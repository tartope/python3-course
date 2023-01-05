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