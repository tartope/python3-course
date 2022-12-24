# List Comprehension:
# syntax: [ ___ for ___ in ___ ]

nums = [1,2,3]
new_nums = [x * 10 for x in nums] #//=> [10, 20, 30]
# print(new_nums)

name = "colt"
new_name = [char.upper() for char in name] #//=> ['C', 'O', 'L', 'T']
# print(new_name)

friends = ["ashley", "matt", "michael"]
new_friends = [friend.upper() for friend in friends] #//=> ['ASHLEY', 'MATT', 'MICHAEL']
new_friends2 = [friend[0].upper() for friend in friends] #//=> ['A', 'M', 'M']
new_friends3 = [friend[0].upper() + friend[1:] for friend in friends] #//=> ['Ashley', 'Matt', 'Michael']
# print(new_friends3)

#takes in a number in the range and multiplies it by 10
[num * 10 for num in range(1,6)] #//=> [10, 20, 30, 40, 50]

#takes in a value and will return if truthy or falsy
[bool(val) for val in [0, [], ""]] #//=> [False, False, False]

numbers = [1,2,3,4,5]
string_list = [str(num) for num in numbers] #//=> ['1', '2', '3', '4', '5']
# print(string_list)
[str(num) + "HELLO" for num in numbers] #//=> ['1HELLO', '2HELLO', '3HELLO', '4HELLO', '5HELLO']

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
[color.upper() for color in colors] #//=> ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'VIOLET']


#List Comprehension with Conditional Logic:

numbers_new = [1,2,3,4,5,6]
# "if" goes at end if using just if keyword
evens = [num for num in numbers_new if num % 2 == 0] #//=> [2, 4, 6]
odds = [num for num in numbers_new if num % 2 != 0] #//=> [1, 3, 5]
# print(evens)
# print(odds)
#"if/else" goes at beginning if using if/else keywords
[num * 2 if num % 2 == 0 else num/2 for num in numbers_new] #//=> [0.5, 4, 1.5, 8, 2.5, 12]

with_vowels = "This is so much fun!"
# if the char is not in the "aeiou" string, add it to the new list
''.join(char for char in with_vowels if char not in "aeiou") #//=> 'Ths s s mch fn!'


# Nested Lists (AKA multi demensional lists):
nested_lists = [[1,2,3], [4,5,6], [7,8,9]]
nested_lists[0][1] #//=> 2
nested_lists[1][-1] #//=> 6
nested_lists[2][1] #//=> 8

# print values (or iterating through) nested lists
# for list in nested_lists:
#     for val in list:
#         print(val)


# Nested List Comprehension:
# [[print(val) for val in list] for list in nested_lists]

# board = [[num for num in range(1,4)] for val in range(1,4)] #//=> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
# print(board)

[["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]  #//=> [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]