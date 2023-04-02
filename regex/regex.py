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