# https://www.scrapingbee.com/blog/

# import this so we can make requests to the site above
import requests
# use BeautifulSoup to webscrape
from bs4 import BeautifulSoup
# to save to csv file
from csv import writer

# Steps:
# - make the request and get the response back
# - take the html received and send it to BeautifulSoup
# - navigate through the html, extract the information wanted, and write it to a file using csv

response = requests.get("https://www.scrapingbee.com/blog/")
# print(response.text)  #//=> returns the html
soup = BeautifulSoup(response.text, "html.parser")
# blogs = soup.find_all(class_="shadow-card")
blogs = soup.find_all(class_="p-10")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "date", "link"])

    # loop through blogs to find each elements text
    for blog in blogs:
        # grab "a" tag inside the div with class="p-10"
        a_tag = blog.find("a")
        # title (gets the child tag then the text)
        title = a_tag.h4.text
        # date (gets the child tag then the text)
        date = a_tag.time.text
        # href/url for article (gets the attribute of the "a" tag by using the square bracket syntax)
        url = a_tag["href"]
        # write to csv (important to follow the same order as headers)
        csv_writer.writerow([title, date, url])