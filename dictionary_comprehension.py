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