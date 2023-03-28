# https://quotes.toscrape.com/

# import this so we can make requests to the site above
import requests
# use BeautifulSoup to webscrape
from bs4 import BeautifulSoup
# this is used to slow the request down when scrapping websites; it halts the code so not to overload their server; it is polite to scrap slowly
from time import sleep
# to save to csv file
from csv import writer
from random import choice

# Steps:
# - make the request and get the response back
# - take the html received and send it to BeautifulSoup
# - navigate through the html, extract the information wanted, and save it to a list in dictionary form
# - set up base url and page url
# - put all steps inside while loop (the page url will change at end of while loop)
# - use sleep() method to slow down requests to server; standard protocol when scrapping

# set base url (this helps naviate through all the pages; all caps shows that it's a constant)
BASE_URL = "https://quotes.toscrape.com/"

def scrape_quotes():
    # make a list of all quotes
    all_quotes = []
    # set url (this starts at page 1)
    url = "/page/1/"

    # while url is True, do all the steps below
    while url:
        # combine the two urls (url is what gets changed to progress through each page)
        response = requests.get(f"{BASE_URL}{url}")
        # print(f"Now scrapping {base_url}{url}...")
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
    return all_quotes
# print(all_quotes)


def start_game(quotes):
    # grab a quote randomly using the choice method
    quote = choice(quotes)
    # start total number of guesses at 4
    remaining_guesses = 4
    # print statements to display quote
    print("Here's a quote: ")
    print(quote["text"])
    # test print statement so we can test code (to be removed once the code functions)
    print(quote["author"])
    # set guess to empty string (an empty string is true which supports the while loop)
    guess = ""
    # while loop: while the guess is not equal to the quote AND the remaining guesses is greater than 0
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        # grab the guess as an input and show remaining guesses
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
        # if guess is correct, print a success statement and break out of the loop
        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT!")
            break
        # otherwise decrement remaining guesses
        remaining_guesses -= 1
        # if first guess is wrong, find the birth date/place using BS and the bio link
        if remaining_guesses == 3:
            response = requests.get(f"{BASE_URL}{quote['bio_link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").text
            birth_place = soup.find(class_="author-born-location").text
            print(f"Here's a hint: The author was born {birth_date} {birth_place}.")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"Here's a hint: The author's last name starts with {last_initial}")
        else:
            print(f"Sorry, you ran out of guesses.  The answer was {quote['author']}.")
    # test print statement to test when we are out of the loop (to be removed oncc the code functions)
    # print("After while loop")

    again = ""
    while again.lower() not in ('y', 'yes', 'n', 'no' ):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("OK, GOODBYE!")

# first scrape with scrape_quotes function
quotes = scrape_quotes()
# then start the game by calling start_game and passing in "quotes"
start_game(quotes)