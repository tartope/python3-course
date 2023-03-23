# Introduction to Web Scraping
# - web scraping involves programmatically grabbing data from a web page
# - three steps: download, extract data, do something with the data

# Why Scrape?
# - there's data on a site that you wan tto store or analyze
# - you can't get it by other means (eg. an API)
# - you want to programmatically grab the data (instead of lots of manual copying/pasting)

# Is it ok? (yes and no; it depends)
# - some websites don't want people scrapping them
# - best practice: consult the robots.txt file
# - if making many requests, time them out (be polite and not make a lot of calls to the server)
# - if you're too aggressive, you IP can be blocked
#_______________________________________________________________

# Intro to Beautiful Soup
# - to extract data from HTML, we'll use Beautiful Soup
# install it with pip; to download Beautiful Soup, run: python3 -m pip install bs4
# - Beautiful Soup lets us navigate through HTML with Python
# - Beautiful Soup does NOT download HTML - for this, we need the "requests" module

# Parsing and Navigating HTML:

# initialize Beautiful Soup
# import BeautifulSoup
# BeautifulSoup(html_string, "html.parser") - parse HTML (because HTML will come back as a giant string)
# - Once parsed, there are several ways to navigate:
#   - By Tag Name
#   - Using a method called "find" - returns one matching tag
#   - Using "find_all" - returns a list of matching tags

# Navigating with CSS Selectors
# - use a method called "select" - returns a list of elements matching a CSS selector

# see bs_basics.py file example
