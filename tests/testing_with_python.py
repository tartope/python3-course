# Why test?
# - reduce bugs in existing code
# - ensure bugs that are fixed stay fixed
# - ensure that new features don't break old ones
# - ensure that cleaning up code (refactoring) doesn't introduce new bugs
# - some people think it makes development more fun!

# Test Driven Development (TDD):
# - development begins by writing tests
# - once test are written, write code to make tests pass
# - once tests pass, a feature is considered complete

# A work flow for TDD: Red, Green, Refactor:
# 1. Red: write a test that fails
# 2. Green: write the minimal amount of code necessary to make the test pass 
# 3. Refactor: clean up the code, while ensuring that tests still pass
#_______________________________________________________________

# Assertions:
# - we can make simple assertions with the "assert" keyword
# - assert accepts an expression (assert is not a function; it's a statement)
# - returns None if the expression is truthy
# - raises an AssertionError if the expression is falsy
# - accepts an optional error message as a second argument
# - think of assert as, if not some_expression: raise an AssertionError()

# def add_positive_numbes(x,y):
#     #if x and y are NOT positive numbers, return the AssertionError "Both numbers must be positive!"
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y

# print(add_positive_numbes(1,1))  #//=> 2
# print(add_positive_numbes(1,-1))  #//=> AssertionError: Both numbers must be positive!

# run in REPL:
# assert 4 == 4  #//=> returns nothing
# assert 4 == 2  #//=> AssertionError
# assert 4 == 2, "4 should not equal 2"  #//=> AssertionError: 4 should not equal 2

# write a test to make sure that "food" is an actual junk food
# def eat_junk(food):
#     # if food is NOT in list, return AssertionError "food must be a junk food"
#     assert food in [
#         "pizza", 
#         "ice cream", 
#         "candy", 
#         "fried butter"
#     ], "food must be a junk food"
#     return f"NOM NOM NOM I am eating {food}"

# food = input("Enter a food please: ")
# print(eat_junk(food))

# Assertions Warning:
# if a Python file is run with the -O (stands for optimized/optimization mode) flag, assertions will not be evaluated; all assertions will be ignored
# YOU CANNOT COUNT ON ASSERT STATEMENTS TO RUN because of optimized mode
# Don't write code like this! If you run your code with -O, or someone else did than the AssertionError will not run; it will be ignored.
# def do_something_bad(user):
#     assert user.is_admin, "Only admins can do bad things!"
#     destroy_a_bunch_of_stuff()
#     return "Mua ha ha ha!"
#_______________________________________________________________

# doctests:
# - we can write tests for functions inside of the docstring
# - write code that looks like it's inside of a REPL
# - just like REPL, must be written with single quotes (doc tests expect all things to have single quotes, not double quotes) and spaces between elements, or tests will show errors)
# - run this special command: python3 -m doctest -v <filename>

# def add(a,b):
#     """
#     >>> add(2,3)
#     5
#     >>> add(100,200)
#     300
#     """
#     return a*b  #<-- this fails the test on purpose so we can see the test failing output; don't forget to run: python3 -m doctest -v testing_with_python.py)


# def add(a,b):
#     """
#     >>> add(2,3)
#     5
#     >>> add(100,200)
#     300
#     """
#     return a+b  #<-- fixed so we can see passing test


# Practice TDD; Red, Green, Refactor:

# 1. write our tests first and then run the code to make sure we're in the red (see example of what to write in test for 'double([True, None])', if you want to test to make sure that you get an error); you have to write exactly what you'd see in the REPL
# 2. write the easiest code to make some pass like, 'return []'  <-- this is one of the tests to pass
# 3. write code to make the rest of the tests pass 'return [2 * element for element in values]  <-- this gets the remainder of the tests to pass

# def double(values):
#     """ double the values in a list

#     >>> double([1,2,3,4])
#     [2, 4, 6, 8]

#     >>> double([])
#     []

#     >>> double(['a', 'b', 'c'])
#     ['aa', 'bb', 'cc']

#     >>> double([True, None])
#     Traceback (most recent call last):
#         ...
#     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
#     """
#     return [2 * element for element in values]
#_______________________________________________________________

# Examples of doctests with small mistakes that throw errors when you expect it to pass:

# def say_hi():
#     """
#     >>> say_hi()
#     "hi"
#     """
#     return "hi"

# Part of the failed test output from above; change "hi" to 'hi' (change double quotes to single quotes) and test will pass
# Failed example:
#     say_hi()
# Expected:
#     "hi"
# Got:
#     'hi'


# def true():
#     """
#     >>> true()
#     True
#     """
#     return True

# if there's a trailing whitespace after "True" that's under the arrows, the tests will pass; make sure there's no whitespace after the cursor.


# def make_dict(keys):
#     """
#     >>> make_dict(['a', 'b'])
#     {'b': True, 'a': True}
#     """
#     return {key: True for key in keys}

# Part of the failed test output from above; it's expecting the dict to be in the same order, even though dict's have no order
# Failed example:
#     make_dict(['a', 'b'])
# Expected:
#     {'b': True, 'a': True}
# Got:
#     {'a': True, 'b': True}
#_______________________________________________________________

# Issues with doctests:
# - syntax is a little strange
# - clutters up our function code
# - lacks many features of larger testing tools
# - doctests can be brittle/finicky
#_______________________________________________________________

# Unit Testing:
# - test smallest parts of an application in isolation (eg. units)
# - good candidates for unit testing: individual classes, modules, or functions
# - bad candidates for unit testing: an entire applictaion, dependencies across several classes or modules

# unittest:
# - comes with built-in assertions. See table on site: https://docs.python.org/3/library/unittest.html
# - Python comes with a built-in module called unittest
# - you can write unit tests encapsulated as classes that inherit from unittest.TestCase
# - this inheritance gives you access to many assertion helpers that let you test the behavior of your functions
# - you can run tests by calling unittest.main() at end of file
# - to run tests, in tests file run: python3 <filename>

# For examples: see activities.py and tests.py files

# Commenting in Tests (see activities.py and tests.py files):
# - add a docstring to the test 
# - to see the comments run command: python3 <filename> -v

# Example
# class SomeTests(unittest.TestCase):
#     def first_test(self):
#         """testing a thing"""
#         self.assertEqual(thing(), "something")

#     def second_test(self):
#         """testing another thing"""
#         self.assertEqual(another_thing(), "something else")
#_______________________________________________________________

# Types of Assertions with unit tests:
# - self.assertEqual(x, y)  (are the values equal)
# - self.assertNotEqual(x, y)  (are the values not equal)
# - self.assertTrue(x)  (is the value Truthy)
# - self.assertFalse(x)  (is the value Falsey)
# - self.assertIsNone(x)  (make sure the value you get back is None)
# - self.assertIsNotNone(x)  (make sure the value you get back is Not None)
# - self.assertIn(x, y)  (make sure the value is IN range/list of values)
# - self.assertNotIn(x, y)  (make sure the value is NOT IN a range/list of values)
# - ...and more (See table on site: https://docs.python.org/3/library/unittest.html)
#_______________________________________________________________

# Testing for Errors:
# - can use self.assertRaises to make sure we get an error in a certain situation; can also guarantee the type of that error

# Example
# class SomeTests(unittest.TestCase):
#     def testing_for_error(self):
#         """testing for an error"""
#         with self.assertRaises(IndexError):
#             # the parameter should be a list like below
#             l = [1,2,3]
#             # this is an example of an error below
#             l[100]
#_______________________________________________________________

# Before and Afer Hooks:

# setUp and tearDown:
# - for larger applications, you may want similar application state before running tests
# - setUp runs before each test method
# - tearDown runs after each test method
# - common use cases: adding/removing data from a test database, creating instances of a class

# Example
# class SomeTests(unittest.TestCase):
#     def setUp(self):
#         #do setup here
#         pass

#     def test_first(self):
#         # setUp runs before
#         # tearDown runs after
#         pass

#     def test_second(self):
#         # setUp runs before
#         # tearDown runs after
#         pass

#     def tearDown(self):
#         # do teardown here
#         pass

# For examples: see robot.py and robot_tests.py files