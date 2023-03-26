# https://quotes.toscrape.com/

# import this so we can make requests to the site above
import requests
# use BeautifulSoup to webscrape
from bs4 import BeautifulSoup
# this is used to slow the request down when scrapping websites; it halts the code so not to overload their server; it is polite to scrap slowly
from time import sleep
# to save to csv file
from csv import writer

# Steps:
# - make the request and get the response back
# - take the html received and send it to BeautifulSoup
# - navigate through the html, extract the information wanted, and save it to a list in dictionary form
# - set up base url and page url
# - put all steps inside while loop (the page url will change at end of while loop)
# - use sleep() method to slow down requests to server; standard protocol when scrapping

# set base url (this helps naviate through all the pages)
base_url = "https://quotes.toscrape.com/"
# set url (this starts at page 1)
url = "/page/1/"

# make a list of all quotes
all_quotes = []

# while url is True, do all the steps below
while(url):
    # combine the two urls (url is what gets changed to progress through each page)
    response = requests.get(f"{base_url}{url}")
    print(f"Now scrapping {base_url}{url}...")
    # parse the html with BeautifulSoup
    soup =  BeautifulSoup(response.text, "html.parser")
    # find the tag with the text, author name, and bio link
    quotes = soup.find_all(class_="quote")

    # loop through quotes to grab each text, author name, and bio link
    for quote in quotes:
        span = quote.find_all("span")
        text = span[0].text
        name = span[1].find(class_="author").text
        bio_link = span[1].find("a")["href"]

        # append all found data to all_quotes list in dictionary form
        all_quotes.append({
            "text": text,
            "author": name,
            "bio_link": bio_link
        })

    # find the tag with the next page button
    next_btn = soup.find(class_="next")
    # at the end of the while loop, update the url to the next page:
    # update url, if next page button is True, else None
    url = next_btn.find("a")["href"] if next_btn else None
    # sleep is standard protocol when scrapping; it's used to slow down the scrapping at end of each loop by waiting 2 seconds
    # sleep(2)
print(all_quotes)
