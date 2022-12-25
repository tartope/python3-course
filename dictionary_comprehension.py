# Dictionary Comprehension:
# syntax: { ___:___ for ___ in ___ } 
# - it iterates over keys by default
# - to iterate over keys and values using .items()

numbers = dict(first= 1, second= 2, third= 3)
# for each key-value in numbers, keep the key the same and square the value
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
# print(squared_numbers) #//=> {'first': 1, 'second': 4, 'third': 9}

# for each number in num, set the value to squared but the key to 'num'
{num: num ** 2 for num in [1,2,3,4,5]} #//=> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))} 
# print(combo) #//=> {'A': '1', 'B': '2', 'C': '3'}

instructor = dict(name= "colt", city= "san francisco", color="purple")
# print(instructor) #//=> {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}
yelling_instructor = {key.upper(): value.upper() for key, value in instructor.items()}
# print(yelling_instructor)  #//=> {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}
yelling_instructor = {(key.upper() if key is "color" else key): value.upper() for key, value in instructor.items()}
print(yelling_instructor)  #//=> {'name': 'COLT', 'city': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}


# conditional logic with dictionaries
num_list = [1,2,3,4]
{num: ("even" if num % 2 == 0 else "odd") for num in num_list} #//=> {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
{num: ("even" if num % 2 == 0 else "odd") for num in range(1,21)} #//=> {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even', 11: 'odd', 12: 'even', 13: 'odd', 14: 'even', 15: 'odd', 16: 'even', 17: 'odd', 18: 'even', 19: 'odd', 20: 'even'}
#____________________________________________

# Practice examples:
# example 1
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {key: value for key, value in person}  #//=> {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

# example 2
# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.  Do this programmatically (using a dict comprehension or dict method) rather than hard coding the answer!
answer = {}.fromkeys("aeiou", 0)  #//=> {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}  (or answer = {char:0 for char in 'aeiou'})

#example 3
# This is a bit different. Every character has an ASCII code (basically, a number that represents it).  Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code.  For example:
# chr(65)  will return  'A'
# chr(66)  will return  'B'
# All the way up to:
# chr(90)  will return  'Z'
# Your task is to create dictionary that maps ASCII keys to their corresponding letters.  Use a dictionary comprehension and chr() . Save the result to the answer variable. You only need to care about capital letters (65-90).

# The end result will look like this:
# {65: 'A',66: 'B',67: 'C',68: 'D',69: 'E',70: 'F',71: 'G',72: 'H',73: 'I',74: 'J',75: 'K',76: 'L',77: 'M',78: 'N',79: 'O',80: 'P',81: 'Q',82: 'R',83: 'S',84: 'T',85: 'U',86: 'V',87: 'W',88: 'X',89: 'Y',90: 'Z'}

answer = {num: chr(num) for num in range(65,91)} #//=> {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}