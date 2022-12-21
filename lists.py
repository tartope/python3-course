# create a list:
# my_list = [1, 2, 3]
# print(my_list); # //=> [1, 2, 3]

# make a list a string:
# my_list_as_a_string = str(my_list)
# print(my_list_as_a_string) # //=> '[1, 2, 3]'

# get length of list:
# print(len(my_list)); #length of list (similar to JS .length)

# create range and convert to list:
# r = range(1,10)
# print(r)  # //=> ramge(1,10)
# print(list(r)) # //=> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# access elements in a list (forwards and backwards):
colors = ["purple", "teal", "orange", True, 8.9, 99]
# print(colors[0]) # //=> purple
# print(colors[1]) # //=> teal
# print(colors[2]) # //=> orange
# # print(colors[3]) # //=> IndexError: list index out of range
# print(colors[-1])  # //=> orange (gives last index in list)
# print(colors[-2])  # //=> teal  (gives second to last index in list)
# print(colors[-3])  # //=> purple (gives third to last index in list)
# print(colors[-4])  # //=> IndexError: list index out of range

#check if value is in a list:
# "purple" in colors # //=> True (not working in VSCode repl; works in replit)

# if "purple" in colors:
#     print("you have good taste in colors!")

# print all items in colors with for loop:
# for item in colors:
#     print(item)

# print all items in colors with while loop:
# i = 0
# while i < len(colors):
#     print(colors[i])
#     i += 1

# prints index with color using an interpolated string:
i = 0
while i < len(colors):
    print(f"{i}: {colors[i]}")
    i += 1


numbers = [1, 2, 3, 4, 5, 6, 7]

# print numbers squared with for loop:
# for num in numbers:
#     print(num * num)

# print numbers with while loop:
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i +=1
