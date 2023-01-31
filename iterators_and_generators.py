# Iterators and Iterables:

# Iterator: an object that can be iterated upon.  An object which returns data, one element at a time when next() is called on it. (Anything you can run a for loop on.)
# Iterable: an object which will return an Iterator when iter() is called on it.
# -"Hello" is an iterable, but it is not an iterator.
# -iter("Hello") returns an iterator.

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
