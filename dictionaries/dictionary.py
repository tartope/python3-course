# Creating a dictionary:
# option 1
cat = {"name": "blue", "age": 3.5, "isCute": True}  #//=> {'name': 'blue', 'age': 3.5, 'isCute': True}
# option 2, creates a dictionary with "dict(key = 'value')" function
cat2= dict(name="kitty") #//=> {'name': 'kitty'}
cat2= dict(name="kitty", age= 0.5) #//=> {'name': 'kitty', 'age': 0.5}

# Accessing individual data in dictionaries:
# option 1
cat["age"]  #//=> 3.5

# option 2, can also access with a variable:
property= "isCute"
cat[property] #//=> True

# error thrown when trying to access a key that doesn't exist:
# cat["breed"] #//=> KeyError: 'breed'
#______________________________________

# How to access all of the values in a dictionary (iterate over a dictionary using loops)
# looping through values with '.values()'
# cat.values() #//=> dict_values(['blue', 3.5, True])
# for value in cat.values():
#     print(value)            #//=> blue
                                # 3.5
                                # True

# looping through keys with '.keys()'
# cat.keys()  #//=> dict_keys(['name', 'age', 'isCute'])
# for key in cat.keys():
#     print(key)              #//=> name
                                # age
                                # isCute

# looping through keys and values with '.items()'
# cat.items() #//=> dict_items([('name', 'blue'), ('age', 3.5), ('isCute', True)])
# for item in cat.items():
#     print(item)             #//=> ('name', 'blue')
                                # ('age', 3.5)
                                # ('isCute', True)

# for key, value in cat.items():
#     print(key, value)       #//=> name blue
                                # age 3.5
                                # isCute True

for key, value in cat.items():
    print(f"key is {key} and value is {value}") #//=> key is name and value is blue
                                                    # key is age and value is 3.5
                                                    # key is isCute and value is True
#______________________________________________________________________________________

# Test for existence of a certain key or value in a dictionary:
# given this dictionary below
cat = {"name": "blue", "age": 3.5, "isCute": True}

# does this dictionary have a KEY
"name" in cat   #//=> True
"awesome" in cat    #//=> False

# if "name" in cat:
#     print("There is a name key")
# else:
#     print("There isn't a name key")

# if "awesome" in cat:
#     print("There is an awesome key")
# else:
#     print("There isn't an awesome key")

# does this dictionary have a VALUE
"blue" in cat.values()  #//=> True
"red" in cat.values()  #//=> False

# if "blue" in cat.values():
#     print("There is blue in value")
# else:
#     print("There isn't a blue in value")
#______________________________________________________________________________________

# Dictionary Methods:

# clear (clears all of the keys and values in a dictionary):
d = dict(a=1, b=2, c=3, d=4)
d.clear()       #//=> {}

# copy (makes a copy of a dictionary):
d = dict(a=1, b=2, c=3, d=4)
clone = d.copy()    #//=> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
clone is d      #//=> False (they point to two differnet places in memory)
clone == d      #//=> True (their values are equal)

# fromkeys (creates key-value pairs from comma separated values; used to create default dictionaries to assign values):
{}.fromkeys("a", "b")   #//=> {'a': 'b'}
{}.fromkeys(["email"], "unknown")   #//=> {'email': 'unknown'}
{}.fromkeys("a", [1,2,3,4,5])   #//=> {'a': [1, 2, 3, 4, 5]}
new_user = {}.fromkeys(["name", "score", "email", "profile bio"], "unknown")    #//=> {'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile bio': 'unknown'}
# can also use "dict.fromkeys"
new_user2 = dict.fromkeys(["name", "score", "email", "profile bio"], "unknown")    #//=> {'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile bio': 'unknown'}
# can use existing name "new_user" but it creates a NEW dictionary; the original "new_user" is unchanged (example shows: can use "{}", "dict", and "variable name" interchangeably)
new_user.fromkeys(range(1,10), "unknown") #//=> {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown'}
# must pass in an iterable list for the keys or see outcome below (it iterates over the string):
new_user.fromkeys("phone", "unknown")       #//=> {'p': 'unknown', 'h': 'unknown', 'o': 'unknown', 'n': 'unknown', 'e': 'unknown'}

# get (retrieves a key in an object and returns None instead of a KeyError if the key does not exist; returns the value if it does exist)
d = dict(a=1, b=2, c=3, d=4)
d["a"]  #//=> 1
d.get("a")  #//=> 1
d["b"]  #//=> 2
d.get("b")  #//=> 2
d["no_key"] #//=> KeyError: 'no_key'
d.get("no_key") #//=> None (nothing shows up in the REPL but 'd.get("no_key" is None' //=> True))

# pop (takes a single argument corresponding to a key and removes that key-value pair from the dictionary; returns the value corresponding to the key that was removed):
d.pop("a")  #//=> 1 (d = {'b': 2, 'c': 3, 'd': 4})

# popitem (removes a random key in a dictionary):
d.popitem() #//=> ('d', 4)

# update (update keys and values in a dictionary with another set of key-value pairs):
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}
second.update(first) #//=> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# overwrite an existing key
second["a"] = "AMAZING" #//=> {'a': 'AMAZING', 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# if we update again, the update overrides our values
second.update(first) #//=> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Practice exercise:
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"
stock_list["cookie"] = 18

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')