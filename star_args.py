# Without *args, a standard function has multiple parameters and arguments
def  sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3

# print(sum_all_nums(4,6,9)) #//=> 19

# *args example (print only)
def  sum_all_nums2(*args):
    print(args)

# print(sum_all_nums2(4,6,9)) #//=> (4,6,9), you get a tuple containing all of the arguments passed in

# *args example
# doesn't need a ton of parameters in order to pass the arguments
def  sum_all_nums3(*args):
    total = 0
    for num in args:
        total += num
    return total

# print(sum_all_nums3(4,6,9)) #//=> 19

# can have *args with two parameters
def  sum_all_nums4(num1, *args):
    print(num1)
    total = 0
    for num in args:
        total += num
    return total

# print(sum_all_nums4(4,6,9)) #//=> prints 4, then prints 15 (the sum of 6 and 9)

# doesn't have to be "*args", it can be *"anything"; as long as the star is there
def sum_all_nums5(*nums):
    total = 0
    for num in nums:
        total += num
    return total

# print(sum_all_nums5(4,6,9)) #//=> prints 19

def ensure_correct_info(*args):
    print(args)
    #if "Tunisia" AND "Artope" are both in the arguments, then return "Welcome back Tunisia!"
    if "Tunisia" in args and "Artope" in args:
        return "Welcome back Tunisia!"
    #otherwise, return "Not sure who you are..."
    return "Not sure who your are..."

# print(ensure_correct_info()) #//=> Not sure who your are... (because the arguments don't contain "Tunisia" AND "Artope")  //=> print statment in function --> ()
# print(ensure_correct_info("hello", False, 78)) #//=> Not sure who your are... (because the arguments don't contain "Tunisia" AND "Artope")
# print(ensure_correct_info(1, True, "Artope", "Tunisia")) #//=> Welcome back Tunisia!  (the arguments now contain "Tunisia" AND "Artope")  //=> print statment in function --> (1, True, 'Artope', 'Tunisia')
#_____________________________________________________________

# Practice Example 1.
# *args Exercise: The Purple Test
# Define a function contains_purple  that accepts any number of arguments.  It should return True  if any of the arguments are "purple" (all lowercase). Otherwise, it should return False .  For example:
# contains_purple(25, "purple")   #True
# contains_purple("green", False, 37, "blue", "hello world")   #False
# contains_purple("purple")   #True
# contains_purple("a", 99, "blah blah blah", 1, True, False, "purple")   #True
# contains_purple(1,2,3)  #False
def contains_purple(*args):
    for arg in args:
        if arg =="purple":
            return True
    return False

# print(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple"))  #//=> True
#_____________________________________________________________

# **kwargs
def fav_colors(**kwargs):
    # print(kwargs)
    # for key= person, value= color in kwargs items()
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

# fav_colors(tunisia="purple", ruby="red", ethel="teal")  #//=> print statment in function --> {'tunisia': 'purple', 'ruby': 'red', 'ethel': 'teal'}
                                                        #//=> tunisia's favorite color is purple
                                                            # ruby's favorite color is red
                                                            # ethel's favorite color is teal


def special_greeting(**kwargs):
    # if David is in the keys AND the value of Davis is "special", return "You get a special greeting David!"
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    # else if David in the keys, return the value of key "David" David
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"

    #else return "Not sure who this is..."
    return "Not sure who this is..."

# print(special_greeting(David= "Hello"))  #//=>  Hello David!
# print(special_greeting(Bob= "hello"))  #//=>  Not sure who this is...
# print(special_greeting(David= "special"))  #//=>  You get a special greeting David!
# print(special_greeting(Heather= "hello", David="special"))  #//=>  You get a special greeting David!
#_____________________________________________________________

# Practice Example 2.
# **kwargs Exercise
# Note: for this exercise, make use of **kwargs.  No default parameters allowed!
# Write a function called combine_words  which accepts a single string called word and any number of additional key word arguments.  If a prefix is provided, return the prefix followed by the word.  If a suffix is provided, return the word followed by the suffix.  If neither is provided, just return the word.  It might sound confusing, but the examples should make this a lot clearer!
# combine_words("child")  #'child'
# combine_words("child", prefix="man")  #'manchild'
# combine_words("child", suffix="ish")  #'childish'
# combine_words("work", suffix="er")  #'worker'
# combine_words("work", prefix="home")  #'homework'
def combine_words(word,**kwargs):
    # if "prefix" is in the key, return the value of key 'prefix' + word
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    # else if return word + the value of key 'suffix'
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    #else return just the word
    return word

# print(combine_words("child", prefix="man"))  #//=> manchild
#_____________________________________________________________

# Parameter Ordering: 

# In function declarations:
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]

# print(display_info(1,2,3, last_name= "Steele", job="Instructor")) #//=> [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]
# a -1
# b - 2
# args - (3)
# instructor - "Colt"
# kwargs - {"last_name": "Steele", "job": "Instructor"}
#_____________________________________________________________

# Tuple Unpacking

def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

# sum_all_values(1,30,2,5,6)  #//=> 44

# nums = [1,2,3,4,5,6] # a list
# sum_all_values(nums)  #//=> TypeError: unsupported operand type(s) for +=: 'int' and 'list'  (because this function is not expecting a list); args is a one item tuple in this case --> ([1, 2, 3, 4, 5, 6],); therefore total += [1, 2, 3, 4, 5, 6] doesn't work

# nums2 = (1,2,3,4,5,6) # a tuple
# sum_all_values(nums2)  #//=> TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'  (same problem as above)

# tuple unpacking solution: adding the * says take each one of these elements in as a separate argument
nums = [1,2,3,4,5,6 ]
# sum_all_values(*nums)  #//=> 21
nums2 = (1,2,3,4,5,6) 
# sum_all_values(*nums2)   #//=> 21
#_____________________________________________________________

# Practice Example 3.
# Unpacking Exercise
# This time I've defined a function for you. It's called count_sevens ,and you need to call it twice.  
# First, call it with the arguments 1,4, and 7 and save the result to a variable called result1.  
# Next, call the same count_sevens function, passing in all the numbers contained in the nums list as individual arguments (unpack the list).  Save the result to a variable called result2.
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)
# print(result1)  #//=> 1
result2 = count_sevens(*nums)
# print(result2)  #//=> 14
#_____________________________________________________________

# Dictionary Unpacking

def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Tunisia", "second": "Buddy"}

# display_names(first="Charlie", second="Sue")  #//=> Charlie says hello to Sue
# display_names(names)  #//=> TypeError: display_names() missing 1 required positional argument: 'second'
# display_names(**names)  #//=> Tunisia says hello to Buddy

def add_and_multiply_numbers(a,b,c):
    print(a + b * c)

data = dict(a=1, b=2, c=3)

# add_and_multiply_numbers(data)  #//=> TypeError: add_and_multiply_numbers() missing 2 required positional arguments: 'b' and 'c'
# add_and_multiply_numbers(**data)  #//=> 7

def add_and_multiply_numbers2(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1, b=2, c=3, d=55, name="Tony")
# add_and_multiply_numbers2(**data)  #//=> 7
                                    # OTHER STUFF....
                                    # {'d': 55, 'name': 'Tony'}
add_and_multiply_numbers2(**data, cat="blue")  #//=> 7
                                                # OTHER STUFF....
                                                # {'d': 55, 'name': 'Tony', 'cat': 'blue'}
#_____________________________________________________________
