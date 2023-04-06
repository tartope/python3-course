# What are Regular Expressions? (not Python specific)
# A way of describing patterns within serach strings
# In Python, we can take a pattern that we define and test inputs

# Examples:
# - Validating Emails (rosa-98@meals.org)
#   Starts with 1 or more letter,number,+,_,-,. then
#       A single @ sign then
#   1 or more letter, number, or - then
#       A single dot then
#   ends with 1 or more letter, number,-, or.

# RegEx for above email example looks like:
# the "." means something in Regex so we have to escape before it (escape the special meaning of a character use "\") "\."
# (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

# Potential Use Cases:
# - Credit Card number validating
# - Phone number validating
# - Advanced find/replace in text
# - Formattting text/output
# - Syntax highlighting
#_______________________________________________________________

# RegEx Outside of Python:
# Cheat Sheet: http://www.rexegg.com/regex-quickstart.html
# Pythex RegEx Editor: https://pythex.org/

# Test String for Pythex RegEx Editor:
# hello wiorld aaabbbcccdddeeefffggghi
# I like cats and kittens :) 415 4129876
# PURPLE 415 412-9876
# kitten@gmail.com
# 310 467-9876
# She is 49 years old. I am 75 years old.  He is 3 3.

# Some RegEx Syntax:
# - Some Characters
#   \d      digit 0-9
#   \w      letter, digit, or underscore
#   \s      whitespace character
#   \D      not a digit
#   \W      not a word character
#   \S      not a whitespace character
#   .       any character except line break 

# Some RegEx Syntax:
# - Quantifiers
#   +       One or more
#   {3}     Exactly x times. {3} - 3 times
#   {3,5}   Three to five times
#   {4,}    Four or more times
#   *       Zero or more times
#   ?       Once or none (optional)
#_______________________________________________________________

# RegEx Basics: Character Classes and Sets (allows specifications of groups or ranges of characters)
# [aeiou] #//=> matches any characters that is one of these characters
# [aeiou]{2}  #//=> matches anytime there's two vowels next to each other
# [a-z]  #//=> matches any lowercase letter
# [A-Z]{2,}  #//=> matches if there's two or more uppercase characters in a row
# [^k]  #//=> matches anything that is not the letter 'k' (note the ^ character has a special meaning outside of the brackets)
#_______________________________________________________________

# RegEx Basics: Anchors and Boundaries:
# - ^       Start of string or line
# - $       End of string or line
# - \b      Word boundary

# Example with phone numbers:
# - ex: 818 765-6234
# without ^ and $ symbols, this matches: adfas818 765-6234adfda
# with ^ and $ symbols, only this matches: 818 765-6234
# ^\d{3} \d{3}-?\d{4}$  (makes sure the phone number begins and ends with the parameters listed)

# Example with words:
# - ex: hello world i am typing stuff
# \b\w+\b (matches all the words and not the spaces at the beginning, end, or between the sentence)
#_______________________________________________________________

# RegEx Basics: Logical Or and Capture Groups:
# | (pipe character)

# Example with phone numbers:
# - ex: 415 345 0998 or (415) 345 0998
# (\(\d{3}\)|\d{3}) \d{3} \d{4}  <-- regular parenthesis signifies that the content is a group
# parens or ^ no parens

# Example with prefix to names:
# - Mr. Luca Guadagnino or Mrs. Tilda Swinton
# (Mr\.|Mrs\.) ([A-Za-z]+ [A-Za-z]+)  <-- regular parens signifies that the content is a group; this has 2 groups
#mr. or^ mrs.
# # (Mr\.|Mrs\.) ([A-Za-z]+) ([A-Za-z]+))  <-- this has 3 groups

# Example with website domains:
# - https://pythex.org or http://google.com
# (https?://)([A-Za-z_-]+\.[A-Za-z]+)
#_______________________________________________________________

# Using RegEx in Python (practiced in Python REPL):

# import RegEx module
# import re

# define our phone number regex
# pattern = re.compile(r'\d{3} \d{3}-\d{4}')
#                      ^ stands for 'raw string'
#           ^ re.compile() creates the RegEx object for us; it contains a lot of methods and one of the methods is called 'search'
# pattern #//=> re.compile('\\d{3} \\d{3}-\\d{4}')
# type(pattern)  #//=> <class 're.Pattern'>

# search a string with our RegEx
# res = pattern.search('Call me at 415 555-4242!')  #//=> returns the match object  <re.Match object; span=(11, 23), match='415 555-4242'>
# res.group()  #//=> '415 555-4242'

# res = pattern.search('Call me at 415 555-4242 or 310 234-9999')  #//=> <re.Match object; span=(11, 23), match='415 555-4242'>
# res.group() #//=> '415 555-4242'

# res = pattern.findall('Call me at 415 555-4242 or 310 234-9999')  #//=> ['415 555-4242', '310 234-9999']
#_______________________________________________________________
