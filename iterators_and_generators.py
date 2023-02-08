# Iterators and Iterables:

# Iterator: an object that can be iterated upon.  An object which returns data, one element at a time when next() is called on it. (Anything you can run a for loop on.)
# Iterable: an object which will return an Iterator when iter() is called on it.
# -"Hello" is an iterable, but it is not an iterator.
# -iter("Hello") returns an iterator.
# - summary:
#   -"Hello" is iterable, but not an iterator (can't be looped)
#   -new_iterator = iter("Hello") returns an iterator (can be looped when next() is called on it)
#   -next(new_iterator) returns the looped data until the StopIteration error runs

name = "Oprah"      # the string "Oprah" is iterable but it's not an iterator
# print(next(name)) #//=> TypeError: 'str' object is not an iterator
# it = iter(name) 
# print(it)  #//=> <str_ascii_iterator object at 0x10290ab60>   <--a string iterator is returns when we call iter(name)

# What a for loop does - for char in "Oprah" - behind the scenes is take the string/list and calls iter() on it that returns an iterator.  Then the for loop uses the next() function to go through each item in the iterator.

# Next: when next() is called on an iterator, the iterator returns the next item (one item at a time).  It keeps doing so until it raises a StopIteration error.

# next(it)  #//=> "O", "p", "r", "a", "h", StopIteration   <-- run in REPL

nums = [1,2,3,4,5]
# print(next(nums)) #//=>  TypeError: 'list' object is not an iterator
# it = iter(nums) #//=>
# print(it) #//=>  <list_iterator object at 0x10246dc60>
# next(it) #//=> 1, 2, 3, 4, 5, StopIteration <-- run in REPL

# Summary: an iterable is "Oprah" or [1,2,3,4,5], and it returns an iterator when iter() is called on it.  The iterator that is returned can be iterated on, one element at a time, when next() is called (like a for loop) until StopIteration error is reached.
#_____________________________________________________________

# Custom for loop:
# for num in [1,2,3]
# for char in "hi there"

# without try/except:
# def my_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         print(next(iterator))

# print(my_for("hello"))  #//=> h
#                         #//=> e
#                         #//=> l
#                         #//=> l
#                         #//=> o
#                         #//=> StopIteration

# with try/except:
# def my_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             print("END OF ITERATOR")
#             break

# print(my_for("hello"))  #//=> h
#                         #//=> e
#                         #//=> l
#                         #//=> l
#                         #//=> o
#                         #//=> END OF ITERATOR

# with function passed that prints the loop:
# pass in string and function
def my_for(iterable, func):
    # the string becomes an iterator
    iterator = iter(iterable)
    # while True
    while True:
        try:
            # thing becomes each element of the string ("l", "o", "l")
            thing = next(iterator)
        except StopIteration:
            break
        # func is call; it's was passed print as an argument, and it prints the letters one at a time
        else:
            func(thing)

# print(my_for("lol", print))  #//=> l
                            #//=> o
                            #//=> l
                            #//=> END OF ITERATOR

# def square(x):
#     print(x*x)

# print(my_for([1, 2, 3, 4, 5], square))  #//=> 1
                                        #//=> 4
                                        #//=> 9
                                        #//=> 16
                                        #//=> 25
#_____________________________________________________________

# Writing a Custom Iterator

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # we defined out own dunder method iter; iter returns self
    def __iter__(self):
        return self

    # define the behavior of next; it's called over and over until it reaches StopIteration
    def __next__(self):
        # as long as current is less than high
        if self.current < self.high:
            # assign current to num (num starts at 0 (reminder num is a different variable from current)) <-- repeat until StopIteration reached for each step of if statement
            num = self.current
            # add 1 to current (current becomes 1)
            self.current += 1
            # return num (return 0)
            return num
        raise StopIteration

# the for loop calls iter on Counter, the (0,10) instance of counter
# for x in Counter(0,10):
#     print(x)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#_____________________________________________________________

# See deck_of_cards_exercise.py file to see iter() in that exercise
#_____________________________________________________________

# Generators:
# - Generators are iterators; they are a subset of iterators (every generator is an iterator, but not every iterator is a generator)
# - They are a quick, easy, short way of creating iterators.

# - Can be created in two ways:
# - Generators can be created with generator functions; generator functions use the yield keyword.
# - Generators can be created with generator expressions.

# Generator functions are like regular functions, but instead of the return keyword, they use the yield keyword.  Instead of returning once, they yield keyword can be used multiple times.  When a regular function is invoked, it returns the return value.  When a generator function is invoked, it returns a generator.

# this is a generator function, it creates a generator when invoked
def count_up_to(max):
    count = 1
    while count <= max:
        # yield returns the value of count and it will pause; it will stay that way until next() is called on count_up_to()
        yield count
        count +=1

# print(count_up_to(5)) #//=>  <generator object count_up_to at 0x102a44110>  <--returns a generator object
counter = count_up_to(5)
# print(counter)  #//=>  <generator object count_up_to at 0x102b00110>
# # must call next() on it:
# print(next(counter)) #//=> 1
# print(next(counter)) #//=> 2
# print(next(counter)) #//=> 3
# print(next(counter)) #//=> 4
# print(next(counter)) #//=> 5
# print(next(counter)) #//=> StopIteration
#_____________________________________________________________

# Practice example 1.
# Week Generator Exercise
# Write a function called week, which returns a generator that yields each day of the week, starting with Monday and ending with Sunday.  After Sunday, the generator is exhausted.  It does not start over.
def week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        yield day

day = week()
# print(next(day))  #//=>  Monday
# print(next(day))  #//=>  Tuesday
# print(next(day))  #//=>  Wednesday
# print(next(day))  #//=>  Thursday
# print(next(day))  #//=>  Friday
# print(next(day))  #//=>  Saturday
# print(next(day))  #//=>  Sunday
# print(next(day))  #//=>  StopIteration
#_____________________________________________________________

# Practice exmaple 2.
# yes_or_no
# Write a function called yes_or_no, which returns a generator that first yields yes , then no , then yes , then no , and so on.
# def yes_or_no():
#     answer = 'yes'
#     while True:
#         yield answer
#         # similar to a ternary operator in JavaScript: set answer to 'no', if answer equals 'yes', else set answer to 'yes'
#         answer = 'no' if answer == 'yes' else 'yes'
#_____________________________________________________________

# Writing a Beat Making Generator:
#  Make a beat counter that gives one beat at a time to the count of 4:

# Not good approach:
# def current_beat():
#     # do this 100 times maximum
#     max = 100
#     # make a tuple
#     nums = (1,2,3,4)
#     # start a counter at zero
#     i = 0
#     # make a result list to return
#     result = []
#     # while the length of result is less than max
#     while len(result) < max:
#         # if i greater than or equal to the length of nums, reset it to 0
#         if i >= len(nums): i = 0
#         # append element to result
#         result.append(nums[i])
#         # increment the counter
#         i += 1
#     # return result
#     return result
# print(current_beat()) #//=> [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# Better approach:
def current_beat():
    # make a tuple
    nums = (1,2,3,4)
    # start a counter at zero
    i = 0
    # makes it an infinite loop because i resets to zero
    while True:
        # if i greater than or equal to the length of nums, reset it to 0
        if i >= len(nums): i = 0
        # yield one element at a time
        yield nums[i]
        # increment the counter
        i += 1
counter = current_beat()
# print(next(counter)) #//=>  1
# print(next(counter)) #//=>  2
# print(next(counter)) #//=>  3
# print(next(counter)) #//=>  4
# print(next(counter)) #//=>  1
# print(next(counter)) #//=>  2
# print(next(counter)) #//=>  3
# print(next(counter)) #//=>  4
#_____________________________________________________________

# Practice example 3.
# make_song
# Write a function called make_song, which takes a count and a beverage, and returns a generator that yields verses from a popular song about a the beverage. The number of verses in the song is determined by the count. 
# Each verse of the song should involve one fewer beverage, until there are no beverages remaining. (Check the examples for details on the structure of the lyrics.)
# The default count should be 99, and the default beverage should be soda.
# instructors solution:
# define function and pass parameters (give a default for verse count, and default for beverage type)
def make_song(verses=99, beverage="soda"):
    # for every number in range(start= starting number, stop= ending number(not inclusive), step= decrementation)(start at 99, end at 0, decrement by -1)
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)
song = make_song(5, "beer")
# print(next(song))  #//=>  5 bottles of beer on the wall.
# print(next(song))  #//=>  4 bottles of beer on the wall.
# print(next(song))  #//=>  3 bottles of beer on the wall.
# print(next(song))  #//=>  2 bottles of beer on the wall.
# print(next(song))  #//=>  Only 1 bottle of beer left!
# print(next(song))  #//=>  No more beer!
# print(next(song))  #//=>  StopIteration
#_____________________________________________________________

# Testing Memory Usage with Generators:
# fibonacci sequence: 0,1,1,2,3,5,8,13,21,34,55

# basic function to make fibonacci sequence
def fib_list(max):
    # make empty list to return
    nums = []
    # a = 0; b = 1
    a, b = 0, 1
    # while the length of nums is less than max
    while len(nums) < max:
        # append b to the end of nums
        nums.append(b)
        # a = b (b is 1); b = a+b (a is 0, and b is 1)
        a, b = b, a+b
    # return nums
    return nums
# print(fib_list(10)) #//=> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# generator function for fibnonacci sequence:
def fib_gen(max):
    # assign 0 to x; assign 1 to y
    x = 0
    y = 1
    # set counter to 0
    count = 0
    # while count is less than max
    while count < max:
        # x = y (y is 1); y = x+y (x is 0, and y is 1)
        x, y = y, x+y
        # use yield keyword to "return" x
        yield x
        # increment count
        count +=1

# for n in fib_gen(10):
    # print(n) #//=> 1
                # 1
                # 2
                # 3
                # 5
                # 8
                # 13
                # 21
                # 34
                # 55
#_____________________________________________________________

# Practice example 4.
# get_multiples
# Write a function called get_multiples, which accepts a number and a count, and returns a generator that yields the first count multiples of the number. 
# The default number should be 1, and the default count should be 10.
# instructors code:
def get_multiples(num=1, count=10):
    # set next numbe to num
    next_num = num
    # while the count is greater than 0
    while count > 0:
        # yield next_num
        yield next_num
        # decrement count
        count -= 1
        # update next_num to next_num + num
        next_num += num

evens = get_multiples(2,3)
# print(next(evens)) #//=> 2
# print(next(evens)) #//=> 4
# print(next(evens)) #//=> 6
# print(next(evens)) #//=> StopIteration

# for n in get_multiples():
#     print(n)  #//=> 1
#                 # 2
#                 # 3
#                 # 4
#                 # 5
#                 # 6
#                 # 7
#                 # 8
#                 # 9
#                 # 10

#_____________________________________________________________

# Practice example 5.
# get_unlimited_multiples
# Write a function called get_unlimited_multiples, which accepts a number and returns a generator that will yield an unlimited number of multiples of that number.
# The default number should be 1.
def get_unlimited_multiples(num= 1):
    # assign num to next_num
    next_num = num
    # infinite loop
    while True:
        # yield next_num
        yield next_num
        # update next_num to next_num + num
        next_num += num

sevens = get_unlimited_multiples(7)
# for n in range(10):
#     print(next(sevens))  #//=> 7
#                             # 14
#                             # 21
#                             # 28
#                             # 35
#                             # 42
#                             # 49
#                             # 56
#                             # 63
#                             # 70
#_____________________________________________________________

# Generator Expressions:
# -You can create generators from generator expressions
# - Generator expressions look a lot like list comprehensions
# - Generator expressions use () instead of []

# regular generator function:
def nums():
    for num in range(1,5):
        yield num

# g = nums()
# print(g) #//=> <generator object nums at 0x1045f9cb0>       <-- says generator object defined with generator function nums
# print(next(g)) #//=> 1
# print(next(g)) #//=> 2
# print(next(g)) #//=> 3
# print(next(g)) #//=> 4
# print(next(g)) #//=> StopIteration

# generator expression (works the same as above):
g2 = (num for num in range(1,5))
# print(g2)  #//=> <generator object <genexpr> at 0x104c95cb0>        <-- says generator object defined with generator expression
#_____________________________________________________________
