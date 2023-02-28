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