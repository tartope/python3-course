import re 

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

# Validating Phone Numbers with Python

# use import statement at top of page
# take a big string and extracts a single phone number
def extract_phone(input):
    # define the pattern with compile() method (use boundaries to get the exact number)
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    # compare it to the input
    match = phone_regex.search(input)
    # if it's a match, return the number; else return None
    if match:
        return match.group()
    else:
        return None

# print(extract_phone("my number is 415 555-4242"))  #//=> 415 555-4242
# print(extract_phone("my number is 415 555-424211"))  #//=> None
# print(extract_phone("my number is 415 555-4242 sdfaf"))  #//=> 415 555-4242
# print(extract_phone("415 555-4242"))                    #//=> 415 555-4242

# take a big string and extracts all phone numbers found
def extract_all_phones(input):
    # define the pattern with compile() method (use boundaries to get the exact number)
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    # compare it to the input
    match = phone_regex.findall(input)
    # if it's a match, return the list; else return None
    if match:
        return match
    else:
        return None

# print(extract_all_phones("my number is 415 555-4242 or call me at 345 666-7899"))  #//=> ['415 555-4242', '345 666-7899']
# print(extract_all_phones("my number is 415 55"))  #//=> None


# checks if entire string is a phone number; returns True, otherwise returns False
def is_valid_phone(input):
    # define the pattern with compile() method (use ^ and $ to define start and end)
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    else:
        return False

# print(is_valid_phone("415 555-4242"))  #//=> True
# print(is_valid_phone("415 555-4242 jgjjh"))  #//=> False
# print(is_valid_phone("uiuh 415 555-4242 jgjjh"))  #//=> False

# another option:
def is_valid_phone_two(input):
    # define the pattern with compile() method
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    # use fullmatch() method (only returns a match if the entire input string is a match)
    match = phone_regex.fullmatch(input)
    if match:
        return True
    else:
        return False
    
# print(is_valid_phone_two("415 555-4242"))  #//=> True
# print(is_valid_phone_two("415 555-4242 jgjjh"))  #//=> False
# print(is_valid_phone_two("uiuh 415 555-4242 jgjjh"))  #//=> False
#_______________________________________________________________

# Practice Exercise 1:

# Time Validating
# Write a function called is_valid_time  that accepts a single string argument.  It should return True  if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise.  Note that times can start with a single number (2:30) or two (11:18).  

# is_valid_time("10:45")       #True
# is_valid_time("1:23")        #True
# is_valid_time("10.45")       #False
# is_valid_time("1999")        #False
# is_valid_time("145:23")      #False
# In order to return True, the string should ONLY contain the time, and no other characters

# is_valid_time("it is 12:15") #False
# is_valid_time("12:15")       #True
# Don't worry about impossible times like 88:76, just focus on the formatting!

# is_valid_time("34:55") #True

# import re at top of page
def is_valid_time(input):
    time_regex = re.compile(r'^\d\d?:\d{2}$')
    match = time_regex.search(input)
    if match:
        return True
    return False

# print(is_valid_time("10:45"))  #//=> True
# print(is_valid_time("145:23")) #//=> False
#_______________________________________________________________

# Parsing URLs with Python
# The example below matches the url and returns it by groups in a tuple.  Can use this to parse through URLs if you only need a piece of it.

url_regex = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
# match = url_regex.search("http://www.youtube.com/videos/dfasd/adff")
match = url_regex.search("https://www.my-website.com/bio?data=blah&cat=yes")
# print(match.group())  #//=> http://www.youtube.com/videos/dfasd/adff
# print(match.group(0))  #//=> http://www.youtube.com/videos/dfasd/adff  <-- passing in 0 gives the entire match
# print(match.group(1))  #//=> http  <-- passing in 1 gives the first group
# print(match.group(2))  #//=> www.youtube.com  <-- passing in 2 gives the second group
# print(match.group(3))  #//=> /videos/dfasd/adff  <-- passing in 3 gives the third group
# print(match.groups())  #//=> ('http', 'www.youtube.com', '/videos/dfasd/adff')  <-- returns a tuple with all groups


# print(f"Protocol: {match.group(1)}")
# print(f"Domain: {match.group(2)}")
# print(f"Everything Else: {match.group(3)}")
#_______________________________________________________________

# Practice Exercise 2:

# Parsing Bytes Exercise
# Write a function called parse_bytes  that accepts a single string.  It should return a list of the binary bytes contained in the string.  Each byte is just a combination of eight 1's or 0's. For example:

# parse_bytes("11010101 101 323")    # ['11010101']

# parse_bytes("my data is: 10101010 11100010")    # ['10101010', '11100010']

# parse_bytes("asdsa")   # []

# Hints: take advantage of \b Not all bytes will have a space before and after, some come at the beginning of a file or at the end.  Use findall!

# import re at top of page
def parse_bytes(input):
    result = []
    binary_regex = re.compile(r'[1+|0+]{8}')
    match = binary_regex.findall(input)
    for byte in match:
        result.append(byte)
    return result

# print(parse_bytes("11010101 101 323"))  #//=>  ['11010101']
# print(parse_bytes("my data is: 10101010 11100010"))  #//=> ['10101010', '11100010']
# print(parse_bytes("asdsa"))                             #//=> []

# Instructors Solution:
def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results
#_______________________________________________________________

# Symbolic Group Names

def parse_name(input):
    # this line below has not label for the first name and can be used with print statement "matches.group(2)"
    # name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) ([A-Za-z]+) ([A-Za-z]+)$')

    # this line belwo has a label (?P<first>) for the first name and can be used with print statement "matches.group("first")"
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')

    matches = name_regex.search(input)

    # print(matches.group(2))  #//=> Tilda
    # print(matches.group(3))  #//=> Swinton
    # OR
#     print(matches.group("first"))  #//=> Tilda
#     print(matches.group("last"))  #//=> Swinton

# parse_name("Mrs. Tilda Swinton")
#_______________________________________________________________

# Practice Exercise 3:

# Date Parsing Exercise
# Define a function called parse_date  that accepts a single string.  Your code should check to see if the string matches a date format.  We're going to use the DMY format of "dd/mm/yyyy", but it should also work with "dd.mm.yyyy" and "dd,mm,yyyy". If you are American, note that Day if before Month!  However, rather than simply returning True or False if the string matches...you should instead return a dictionary containing the three parts of the date with the keys "d" , "m" , and "y"  like so:

# parse_date("01/22/1999") # {'d': '01', 'm': '22', 'y': '1999'}
#  Note: the string should be an EXACT match, containing the date and nothing else. If there is no match, return None

# parse_date("12,04,2003")  #{'d': '12', 'm': '04', 'y': '2003'}
# parse_date("12.11.2003")  #{'d': '12', 'm': '11', 'y': '2003'}
# parse_date("12.11.200312") #None

# import re at top of page
def parse_date(input):
    date_regex = re.compile(r'^(?P<day>\d{2})[/,.](?P<month>\d{2})[/,.](?P<year>\d{4})$')
    match = date_regex.search(input)
    if match:
        day = match.group('day')
        month = match.group('month')
        year = match.group('year')
        result = dict(d= day, m= month, y= year)
        return result
    else:
        return None
    
# print(parse_date("12,04,2003"))  #//=> {'d': '12', 'm': '04', 'y': '2003'}
# print(parse_date("12.11.2003"))  #//=> {'d': '12', 'm': '11', 'y': '2003'}
# print(parse_date("12.11.200312"))  #//=> None

# Instructors Solution:
def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None
#_______________________________________________________________

# RegEx Compliation Flags

# below pattern is for emails
# pat = re.compile('r^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

# VERBOSE (can use re.VERBOSE or re.X): allows us to break up the RegEx on different lines and comment for easy reading (it ignores the whitespace created by each new line)
pattern = re.compile(r"""
    ^([a-z0-9_\.-]+)    # first part of email
    @                   # single @ sign
    ([0-9a-z\.-]+)      # email provider
    \.                  # single period
    ([a-z\.]{2,6})$     # com, org, net, etc.
""", re.VERBOSE | re.IGNORECASE)

match_lower = pattern.search("thomas123@yahoo.com")
match_upper = pattern.search("Thomas123@Yahoo.com")
# print(match_lower.groups())  #//=> ('thomas123', 'yahoo', 'com')
# print(match_lower.group())  #//=> thomas123@yahoo.com

# IGNORECASE (can use re.IGNORECASE or re.I): adding IGNORECASE allows RegEx to ignore casing in input
# print(match_upper.groups())  #//=> ('Thomas123', 'Yahoo', 'com')
# print(match_upper.group())  #//=> Thomas123@Yahoo.com
#_______________________________________________________________

# Regex Substitution Basics

# Example of classified document
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) [a-z]+", re.I)
# print(pattern.findall(text))  #//=> ['Mrs.', 'Mr.', 'Ms.']  <-- looks like it's not finding the full name because this is the way findall() works
# print(pattern.search(text).group())  #//=> Mrs. Daisy  <-- search returns the first pattern

# the whole name is redacted
result = pattern.sub("REDACTED", text)
# print(result)  #//=>  Last night REDACTED and REDACTED murdered REDACTED

# just the name is redacted
result1 = pattern.sub("\g<1> REDACTED", text)
# print(result1)  #//=> Last night Mrs. REDACTED and Mr. REDACTED murdered Ms. REDACTED

# this pattern helps to redact part of the name
pattern1 = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+", re.I)
result2 = pattern1.sub("\g<1> \g<2>", text)
# print(result2)  #//=> Last night Mrs. D and Mr. W murdered Ms. C
#_______________________________________________________________

# Practice Exercise 4:

# Regex Profanity Filter
# Define a function called censor  that accepts a single string. Rather than censoring any real profanity, we're going to censor any words that start with "frack".  This includes "fracking", "fracker", "frack", etc.  Replace the entire word with the string "CENSORED".  Your regex should be case insensitive. For example:

# censor("Frack you")                #"CENSORED you"
# censor("I hope you fracking die")  #"I hope you CENSORED die"
# censor("you fracking Frack")       #"You CENSORED CENSORED"

# see import re at top of page

def censor(input):
    pattern = re.compile(r"[frack][a-z]+", re.IGNORECASE)
    result = pattern.sub("CENSORED", input)
    return result

# print(censor("Frack you"))  #//=> CENSORED you
# print(censor("I hope you fracking die"))  #//=> I hope you CENSORED die
# print(censor("you fracking Frack"))  #//=> you CENSORED CENSORED
#_______________________________________________________________

# Swapping File Names

titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

# sorts alphabetically based off the first character
titles.sort()
# print(titles)  #//=> ['Babycakes (1984)', 'Futher Tales of the City (1982)', 'Mary Ann in Autumn (2010)', 'Michael Tolliver Lives (2007)', 'More Tales of the City (1980)', 'Significant Others (1987)', 'Sure of You (1989)', 'Tales of the City (1978)', 'The Days of Anna Madrigal (2014)']

# created new titles list
fixed_titles = []

# create pattern to sort based on date then title (ie. "1978 - Tales of the City")
pattern = re.compile(r"^([\w ]+) \((\d{4})\)$")  #<-- the parentheses are only around the numbers in order to grab it without the parentheses
# loop through titles
for book in titles:
    # create the new order for every book
    result = pattern.sub("\g<2> - \g<1>", book)
    # append the result to the new titles list
    fixed_titles.append(result)
# sort the new titles list
fixed_titles.sort()
print(fixed_titles)  #//=>  ['1978 - Tales of the City', '1980 - More Tales of the City', '1982 - Further Tales of the City', '1984 - Babycakes', '1987 - Significant Others', '1989 - Sure of You', '2007 - Michael Tolliver Lives', '2010 - Mary Ann in Autumn', '2014 - The Days of Anna Madrigal']