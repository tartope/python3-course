# append (adds an item to the end of a list; similar to JS push()):
first_list = [1,2,3,4]  #//=> [1,2,3,4]
first_list.append(5)    #//=> [1,2,3,4,5]
# print(first_list)
#______________________________________________________________________________________

# extend (adds multiple items to the end of a list):
first_list.extend([6,7,8,9])    #//=> [1,2,3,4,5,6,7,8,9]
# print(first_list)
#______________________________________________________________________________________

# insert (insert an item at a given index):
first_list.insert(2, "Hi")  #//=> [1, 2, 'Hi', 3, 4, 5, 6, 7, 8, 9]
# print(first_list)
# inserts at last index prior to the insert
first_list.insert(-1, "The end!")   #//=> [1, 2, 'Hi', 3, 4, 5, 6, 7, 8, 'The end!', 9]
# print(first_list)
# inserts at very end after caluculating the length
first_list.insert(len(first_list), "LAST")  #//=> [1, 2, 'Hi', 3, 4, 5, 6, 7, 8, 'The end!', 9, 'LAST']
# print(first_list)
#______________________________________________________________________________________

# clear (removes all items from a list):
new_list = [1,2,3,4]
new_list.clear()    #//=> []
# print(new_list)
#______________________________________________________________________________________

# pop (removes an item from a given index in a list and returns it; if no index is specified, it removes and returns the last item in the list):
items = ["socks", "mug", "tea pot", "cat food"]
# print(items.pop()) #//=> 'cat food'
# print(items.pop(1))    #//=> 'mug'
#______________________________________________________________________________________

# remove (remove the first item from the list whose value is x (not index); throws a ValueError if the item is not found):
num_list = [1,2,3,4,4,4]
num_list.remove(2)  #//=> [1, 3, 4, 4, 4]
# print(num_list) 
num_list.remove(4)  #//=> [1, 3, 4, 4] (because multiple 4's, it only removes the first one)
# print(num_list)
#______________________________________________________________________________________

# index (returns the index of the specified item in the list):
numbers = [5,6,7,8,9,10]
numbers.index(6)    #//=> 1 (this is the index)
numbers.index(9)    #//=> 4 (this is the index)
#can specify a start and end:
names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
names.index("colt")    #//=> 0 (gives the first index where it finds "colt")
names.index("colt",1)  #//=> 4 (find the index of value "colt", after the index of 1 (it's inclusive of 1))
names.index("colt",2)  #//=> 4 (find the index of value "colt", after the index of 2 (it's inclusive of 2))
names.index("colt",4,6)  #//=> 4 (find the index of value "colt", between the index of 4 - 6 (it's inclusive of 4))
#______________________________________________________________________________________

# count (accepts one input, and returns the number of times x appears in the list):
names.count("colt") #//=> 2
names.count("buddy") #//=> 0
names.count("blue") #//=> 1
#______________________________________________________________________________________

# reverse (reverse the elements of the list (in-place)):
first_list = [1,2,3,4]
first_list.reverse()    #//=> [4, 3, 2, 1]
#______________________________________________________________________________________

# sort (sort the items of the list (in-place)):
another_list = [6,4,1,2,5]
another_list.sort() #//=> 
# print(another_list) #//=> [1, 2, 4, 5, 6]
#______________________________________________________________________________________

# join:
# -technically a STRING METHOD that takes an iterable argument
# -concatenates a copy of the base string BETWEEN each item of the iterable
words = ["Coding", "Is", "Fun!"]
" ".join(words) #//=> 'Coding Is Fun!'
name = ["Mr", "Steele"]
". ".join(name) #//=> 'Mr. Steele'
#______________________________________________________________________________________

# Slicing (makes a new list using slices of the old list) Ex: some_list[start:end:step]:

# -first parameter of slice ([start:])
first_list = [1,2,3,4]
# what index to start the slice from (if you give a negative number, it will start the slice that many back from the end)
first_list[1:]  #//=> [2,3,4]
first_list[3:]  #//=> [4]
first_list[-1:]  #//=> [4]
first_list[-3:]  #//=> [2,3,4]
# [:] gives a COPY of the entire list (does not give us the same list)
first_list[:]   #//=> [1, 2, 3, 4]
# [0:] gives a COPY of the entire list (does not give us the same list)
first_list[0:]  #//=> [1, 2, 3, 4]

# -second parameter of slice ([:end]); the index of copy up to (exclusive counting; does not include the last index provided)
#(with negative numbers, how many items to exclude from the end (ie. indexing by counting backwards))
first_list = [1,2,3,4]
first_list[:2]  #//=> [1,2]
first_list[:4]  #//=> [1, 2, 3, 4]
first_list[1:3] #//=> [2,3]
first_list[:-1] #//=> [1,2,3]
first_list[1:-1] #//=> [2,3]

# -third parameter os slice ([::step])
    # -in Python, the number to count at a time (AKA how many to skip; a step of 2 counts every other number (1,3,5))
    # -same as step with range
first_list = [1,2,3,4,5,6]
#    [start::step] (no end parameter)
first_list[1::2]    #//=> [2,4,6]
first_list[::2]    #//=> [1,3,5]
# with negative numbers, reverse the order (starts at value 2 and goes backwards to value 1)
first_list[1::-1]   #//=> [2,1]
# the end is exclusive, so it does not include index 1(value 2) (starts at value 6 and goes backwards up UNTIL value 2)
first_list[:1:-1]   #//=> [6,5,4,3]
# starts at value 3 and goes backwards to value 1
first_list[2::-1]   #//=> [3,2,1]

# Tricks with slices:

# -reversing lists/strings
string = "This is fun!"
string[::-1]    #//=> '!nuf si sihT'
# -modifying portions of a list
numbers = [1,2,3,4,5]
numbers[1:3] = ["a","b","c"]   #//=> [1,"a", "b", "c", 4, 5]
#______________________________________________________________________________________

# swapping values:
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names)    #//=> ['Michelle', 'James']
# when do you need to swap?
# -shuffling
# -sorting a list in-place
# -algorithms