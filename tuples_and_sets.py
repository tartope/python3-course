# Define a tuple (an ordered collection or grouping of items; similar to list but uses different syntax and is immutable)
value = (1,)  #<-- a tuple with one value inside (must have the comma)
x = (1,2,3)
3 in x #//=> True
# x[0] = "change me!" #//=> TypeError: 'tuple' object does not support item assignment

alphabet = ("a", "b", "c", "d")
type(alphabet) #=> <class 'tuple'>
# alphabet.append("e") #=> AttributeError: 'tuple' object has no attribute 'append'
#_____________________________________________________________

# a good example of data for a tuple (the months are always in the same order and they never change)
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Creating/Accessing tuples (use the "()" or "tuple" function; accessing is just like a list)
first_tuple = (1,2,3,3,3)
first_tuple[1] #//=> 2
first_tuple[2] #//=> 3
first_tuple[-1] #//=> 3

# second_tuple = tuple(5,1,2)
# second_tuple[0] #//=> 5
# second_tuple[-1] #//=> 2
#_____________________________________________________________

# Tuples can be used as keys in dictionaries
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}
locations[(37.7749, 122.4194)] #//=> 'San Francisco Office'

# Some dictionary methods like ".items()" return tuples
cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "my chapstick"}
# cat.items() #//=> dict_items([('name', 'biscuit'), ('age', 0.5), ('favorite_toy', 'my chapstick')])
#                                  ^tuple               ^ tuple           ^tuple
#_____________________________________________________________

# Tuple methods:
# looping
names = ("Colt", "Blue", "Rusty", "Lassie")
# for name in names:
#     print(name)

# for month in months:
#     print(month)

# i = len(months)-1
# while i >= 0:
#     print(months[i])
#     i -= 1

# count (returns the number of times a value appears in a tuple):
x = (1,2,3,3,3)
x.count(1) #//=> 1
x.count(3) #//=> 3

# index (returns the index at which a value is found in a tuple):
t = (1,2,3,3,3)
t.index(1) #//=> 0
# t.index(5) #//=> ValueError: tuple.index(x): x not in tuple
t.index(3) #//=> 2 (only the first matching index is returned)

# tuples can be nested too
nums = (1,2,3, (4,5), 6, 7)
nums[0] #//=> 1
nums[3] #//=> (4,5)
nums[3][1] #//=> 5

# can use slices
nums[0:] #//=> (1, 2, 3, (4, 5), 6, 7)
nums[0:4] #//=> (1, 2, 3, (4, 5))
nums[0:4:2] #//=> (1,3)
#_____________________________________________________________

# Sets
# creating/accessing sets:
# sets cannot have duplicates
s = set({1,2,3,4,5,5,5}) #//=> {1, 2, 3, 4, 5}

# creating a new set
s = set({1,4,5})

# creates a set with the same values as above
s = ({1,4,5})

4 in s #//=> True
8 in s #//=> False
# s[0] #//=> TypeError: 'set' object is not subscriptable

# sets can have any data type inside
s = ({1,4,5,"a", "b", 23.3334}) #//=> {1, 4, 5, 23.3334, 'a', 'b'}

# Looping through sets
numbers = {1,2,3,4}
for number in numbers:
    print(number)

#_____________________________________________________________

# Common use case for sets
# remove the duplicates and distill this down to a list of unique cities
cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shanghi", "Boulder", "San Francisco", "Oslo", "Tokyo"]

# prints a list of cities in a set without duplicates
print(set(cities)) #//=> {'Boulder', 'Tokyo', 'Los Angeles', 'Santiago', 'San Francisco', 'Shanghi', 'Florence', 'Kyoto', 'Oslo'}

# changes the set back to a list but with no duplicates
print(list(set(cities))) #//=> ['Florence', 'Kyoto', 'Boulder', 'San Francisco', 'Tokyo', 'Oslo', 'Shanghi', 'Los Angeles', 'Santiago']

# number of unique cities
print(len(set(cities))) #//=> 9
#_____________________________________________________________

# Set methods:
# add (add an element to a set. If the element is already in the set, the set doesn't change)
s = set([1,2,3])
s.add(4) #//=> {1, 2, 3, 4}
s.add(4) #//=> {1, 2, 3, 4}

# remove (removes a value from the set - returns a KeyError if the value is not found)
set1 = {1,2,3,4,5,6}
set1.remove(3) #//=> {1, 2, 4, 5, 6}
# set1.remove(44) #//=> KeyError: 44

# .discard() (avoids the KeyError messages)
set1.discard(44) #//=> no error message
set1.discard(4) #//=> {1, 2, 5, 6}

# copy (creates a copy of the set)
s = set([1,2,3])
another_set = s.copy() #//=> {1, 2, 3}
another_set is s #//=> False

# clear (removes all the contents of the set)
s.clear() #/=> set()

# Set Math (has a few mathematical methods):
# - intersection
# - symmetrical difference
# - union

# suppose two classes
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# generate a set with all unique students using "union"; no duplicates in list (the "|" character represents "union")
math_students | biology_students #//=> {'Prashant', 'Charlotte', 'Matthew', 'Jane', 'Oliver', 'Helen', 'Aparna', 'James', 'Mesut'}

# generate a set of students who are in both classes using "intersection" (the "&" character represents "intersection")
math_students & biology_students #//=> {'Matthew', 'James'}
#_____________________________________________________________

# Set Comprehension (similar to dictionary comprehension but no key-value specified)
# set comprehension syntax
{x**2 for x in range(10)} #//=> {0, 1, 64, 4, 36, 9, 16, 49, 81, 25} <-- there's no order to set comprehension
# dictionary comprehension syntax
{x: x**2 for x in range(10)} #//=> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} <-- returns a dictionary
# set comprehension using string with duplicates
{char.upper() for char in "hello"} #//=> {'O', 'E', 'L', 'H'}  <--returns one of each character upper cased (no order)

string = "hello"
{char for char in string if char in "aeiou"} #//=> {'e', 'o'}
len({char for char in string if char in "aeiou"}) #//=> 2
len({char for char in string if char in "aeiou"}) == 5 #//=> False

string2 = "sequoia"
{char for char in string2 if char in "aeiou"} #//=> {'i', 'u', 'e', 'a', 'o'}
len({char for char in string2 if char in "aeiou"}) #//=> 5
len({char for char in string2 if char in "aeiou"}) == 5 #//=> True

def are_all_vowels_in_string(string):
    # checks if resulting set is equal to 5, returns True
    return len({char for char in string if char in "aeiou"}) == 5
