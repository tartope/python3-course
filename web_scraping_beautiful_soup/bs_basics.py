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
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup)  #//=> you get the entire html document
# print(type(soup))  #//=>  <class 'bs4.BeautifulSoup'>
# print(soup.body)  #//=>  you get the entire body document
# print(soup.body.div)  #//=>  there are two divs in the body but you only get the first div
# print(soup.find("div"))  #//=>  there are two divs in the body but you only get the first div
d = soup.find("div")
# print(type(d)) #//=>  <class 'bs4.element.Tag'>
# print(soup.find_all("div"))  #//=>  you get a list with all of the divs
# print(soup.find(id="first"))  #//=> finds the element with id="first"
# print(soup.find_all(class_="special"))  #//=> you get a list with all of the elements with this class; (when using BeautifulSoup use "class_" because otherwise it thinks you're defining a "class")
# can also select based off of attributes (see line 11):
data1 = soup.find_all(attrs={"data-example": "yes"})
# print(data1)  #//=>  you get a list of all elements with this attribute
data = soup.select("[data-example]")
print(data)  #//=>  you get a list of all elements with this attribute
