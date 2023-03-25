from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup)  #//=> you get the entire html document
# print(type(soup))  #//=>  <class 'bs4.BeautifulSoup'>

# Navigating with CSS Selectors:

# print(soup.body)  #//=>  you get the entire body document
# print(soup.body.div)  #//=>  there are two divs in the body but you only get the first div
# print(soup.find("div"))  #//=>  there are two divs in the body but you only get the first div
# d = soup.find("div")
# print(type(d)) #//=>  <class 'bs4.element.Tag'>
# print(soup.find_all("div"))  #//=>  you get a list with all of the divs
# print(soup.find(id="first"))  #//=> finds the element with id="first"
# print(soup.find_all(class_="special"))  #//=> you get a list with all of the elements with this class; you are always given a list; (when using BeautifulSoup use "class_" because otherwise it thinks you're defining a "class")

# can also select based off of attributes (see line 11); you are always given a list with select:
# data1 = soup.find_all(attrs={"data-example": "yes"})
# print(data1)  #//=>  you get a list of all elements with this attribute

# to select id:
# data2 = soup.select("#first")
# print(data2) #//=> you get a list of all elements with this attribute

# to select id with first element of list:
# data3 = soup.select("#first")[0]
# print(data3) #//=> you get the first element in the list

# to select class:
# data4 = soup.select(".special")
# print(data4) #//=> you get a list of elements with a class of "special"

# to select tag:
# data5 = soup.select("div")
# print(data5) #//=> you get a list of all the divs

# to select based off of an attribute
# data = soup.select("[data-example]")
# print(data)  #//=>  you get a list of all elements with this attribute
#_______________________________________________________________

# Accessing Data in Elements:

# el = soup.select(".special")[0]
# print(el)   #//=>  <li class="special super-special">This list item is special.</li>
# print(el.get_text())   #//=>  This list item is special.
# for el in soup.select(".special"):
#     print(el.get_text())  #//=> This iterates through all the text and prints them

# for el in soup.select(".special"):
#     print(el.name)  #//=> iterates through the element and prints the name of the tag "li"
#     print(el.attrs)  #//=> iterates through and returns a dictionary of key/value pairs for the attributes on each item
#                             # {'class': ['special', 'super-special']}  <-- the value is a list because elements can have more than one class
#                             # {'class': ['special']}
#     print(el.attrs["class"])  #//=> ['special', 'super-special']
#                                     # ['special']

# Technically don't need ".attrs" if trying to access an attribute; can do below
# attr1 = soup.find("h3").attrs["data-example"]
# attr2 = soup.find("h3")["data-example"]
# print(attr1)  #=> yes
# print(attr2)  #=> yes

# attr3 = soup.find("div")["id"]
# print(attr3) #=> first
#_______________________________________________________________

# Navigating with Beautiful Soup via Tags:

# data = soup.body.contents
# # print(data) #//=> returns a list with \n (new lines) throughout
# data1 = soup.body.contents[1]
# # print(data1) #//=> returns the first div
# data2 = soup.body.contents[1].contents
# # print(data2) #//=> returns a list of the contents of the first div
# data3 = soup.body.contents[1].next_sibling.next_sibling
# # print(data3) #//=> returns the next item that isn't empty; returns the ol that's after the first div, after the \n (new line)
# data4 = soup.find(class_="super-special").parent
# # print(data4) #//=> returns the parent of this element which is the entire ol
# data5 = soup.find(class_="super-special").parent.parent
# print(data5) #//=> returns the parent of this element which is the entire body

# Navigating with Beautiful Soup via Searching:

# this method skips over the empty \n (new line) until it finds a element
# data6 = soup.find(id="first").find_next_sibling()
# # print(data6) #//=> returns the ol which is the next sibling of the tag with an id="first"
# data7 = soup.find(id="first").find_next_sibling().find_next_sibling()
# # print(data7) #//=> returns the div which is the next sibling of ol, which is the next sibling of the tag with an id="first"
# data8 = soup.select("[data-example]")[1].find_previous_sibling()
# # print(data8) #//=> returns the tag previous to the tag with an attribute of "data-example"
# data9 = soup.find(class_="special").find_next_sibling()
# # print(data9) #//=> returns the next sibling element
# data10 = soup.find(class_="special").find_next_sibling(class_="special")
# # print(data10) #//=> returns the next sibling element with a class of "special"
# data11 = soup.find("h3").find_parent()
# print(data11) #//=> returns the parent tag with all of its contents

# help(data11)  #//=> to show all the search methods possible