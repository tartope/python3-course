# def product(a, b):
#     """ return the product of a * b
#     >>> product(2, 3)
#     6
#     >>> product(100, 200)
#     20000
#     """
#     return a * b


# The Python interpreter ignores None return values, so doctests do the same.
# Test for is None instead:
# def return_day(num):
#     """ 
#     >>> return_day(2)
#     'Monday'

#     >>> return_day(7)
#     'Saturday'

#     >>> return_day(8) is None
#     True

#     >>> return_day('9')
#     Traceback (most recent call last):
#         ...
#     TypeError: '<' not supported between instances of 'str' and 'int'
#     """
#     days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
#     days = days.get(num)
#     if num < 1 or num > 7:
#         return None
#     return days


# def last_element(list):
#     """
#     >>> last_element([1,2,3])
#     3

#     >>> last_element([]) is None
#     True

#     >>> last_element(8)
#     Traceback (most recent call last):
#         ...
#     TypeError: object of type 'int' has no len()
#     """
#     if len(list) == 0:
#         return None
#     return list[-1]


# def number_compare(num1, num2):
#     """
#     >>> number_compare(10,2)
#     'First is greater'

#     >>> number_compare(2,10)
#     'Second is greater'

#     >>> number_compare(2,2)
#     'Numbers are equal'

#     >>> number_compare('a',2)
#     Traceback (most recent call last):
#         ...
#     TypeError: '>' not supported between instances of 'str' and 'int'

#     >>> number_compare()
#     Traceback (most recent call last):
#         ...
#     TypeError: number_compare() missing 2 required positional arguments: 'num1' and 'num2'
#     """
#     if num1 > num2:
#         return "First is greater"
#     elif num2 > num1:
#         return "Second is greater"
#     else:
#         return "Numbers are equal"


# def single_letter_count(word, letter):
#     """
#     >>> single_letter_count('Hello World', 'h')
#     1

#     >>> single_letter_count('Hello World', 'z')
#     0

#     >>> single_letter_count('Hello World', 'l')
#     3

#     >>> single_letter_count('Hello World', 1)
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'int' object has no attribute 'lower'
#     """
#     return word.lower().count(letter.lower())


# def multiple_letter_count(str):
#     """
#     >>> multiple_letter_count('awesome')
#     {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}

#     >>> multiple_letter_count('hello')
#     {'h': 1, 'e': 1, 'l': 2, 'o': 1}

#     >>> multiple_letter_count(1)
#     Traceback (most recent call last):
#         ...
#     TypeError: 'int' object is not iterable
#     """
#     return {letter: str.count(letter) for letter in str}


# def list_manipulation(list, command, location, value=None):
#     """
#     >>> list_manipulation([1,2,3], "remove", "end")
#     3

#     >>> list_manipulation([1,2,3], "remove", "beginning")
#     1

#     >>> list_manipulation([1,2,3], "add", "beginning", 20)
#     [20, 1, 2, 3]

#     >>> list_manipulation([1,2,3], "add", "end", 30)
#     [1, 2, 3, 30]

#     >>> list_manipulation([], "remove", "end")
#     Traceback (most recent call last):
#         ...
#     IndexError: pop from empty list
#     """
#     if(command == "remove" and location == "end"):
#         return list.pop()
#     elif(command == "remove" and location == "beginning"):
#         return list.pop(0)
#     elif(command == "add" and location == "beginning"):
#         list.insert(0, value)
#         return list
#     elif(command == "add" and location == "end"):
#         list.append(value)
#         return list


# def is_palindrome(str):
#     """
#     >>> is_palindrome("testing")
#     False

#     >>> is_palindrome("tacocat")
#     True

#     >>> is_palindrome("10")
#     False

#     >>> is_palindrome(10)
#     Traceback (most recent call last):
#         ...
#     TypeError: 'int' object is not subscriptable
#     """
#     if(str == str[::-1]):
#         return True
#     return False


# def frequency(collection, search_term):
#     """
#     >>> frequency([1,2,3,4,4,4], 4)
#     3

#     >>> frequency([True, False, True, True], False)
#     1

#     >>> frequency([True, False, True, True])
#     Traceback (most recent call last):
#         ...
#     TypeError: frequency() missing 1 required positional argument: 'search_term'
#     """
#     return collection.count(search_term)


# def multiply_even_numbers(collection):
#     """
#     >>> multiply_even_numbers([2,3,4,5,6])
#     48

#     >>> multiply_even_numbers([1,22,33,44])
#     968

#     >>> multiply_even_numbers(44)
#     Traceback (most recent call last):
#         ...
#     TypeError: 'int' object is not iterable
#     """
#     total = 1
#     for num in collection:
#         if(num % 2 == 0):
#             total *= num
#     return total


# def capitalize(str):
#     """
#     >>> capitalize("tim")
#     'Tim'

#     >>> capitalize("matt")
#     'Matt'

#     >>> capitalize(10)
#     Traceback (most recent call last):
#         ...
#     TypeError: 'int' object is not subscriptable
#     """
#     return str[0].upper() + str[1:]


# def compact(collection):
#     """
#     >>> compact([0,1,2,"",[], False, {}, None, "All done"])
#     [1, 2, 'All done']

#     >>> compact([True, "hi", None])
#     [True, 'hi']

#     >>> compact(True)
#     Traceback (most recent call last):
#         ...
#     TypeError: 'bool' object is not iterable
#     """
#     new_collection = []
#     for char in collection:
#         if char:
#             new_collection.append(char)
#     return new_collection


# def intersection(lst1, lst2):
#     """
#     >>> intersection([1,2,3], [2,3,4])
#     [2, 3]

#     >>> intersection(['a','b','z'], ['x','y','z'])
#     ['z']

#     >>> intersection([1,2,3])
#     Traceback (most recent call last):
#         ...
#     TypeError: intersection() missing 1 required positional argument: 'lst2'
#     """
#     set1 = set(lst1)
#     set2 = set(lst2)
#     new_list = list(set1 & set2)
#     return new_list

def isEven(num):
    """
    >>> isEven(1)
    False

    >>> isEven(2)
    True

    >>> isEven("hi")
    Traceback (most recent call last):
        ...
    TypeError: not all arguments converted during string formatting
    """
    return num % 2 == 0

def partition(lst, fn):
    """
    >>> partition([1,2,3,4], isEven)
    [[2, 4], [1, 3]]

    >>> partition(22, isEven)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]