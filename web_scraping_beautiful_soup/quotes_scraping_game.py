# import this so we can make requests to the site above
import requests
# use BeautifulSoup to webscrape
from bs4 import BeautifulSoup
# this is used to slow the request down when scrapping websites; it halts the code so not to overload their server; it is polite to scrap slowly
from random import choice
from csv import DictReader


# set base url (this helps naviate through all the pages; all caps shows that it's a constant)
BASE_URL = "https://quotes.toscrape.com/"

def read_quotes(filename):
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        quotes = list(csv_reader)
        return quotes

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


quotes = read_quotes("quotes.csv")
# then start the game by calling start_game and passing in "quotes"
start_game(quotes)

# This file has game logic:
# - first it reads the csv file
# - then the game logic is written and the read_quotes function is passed to the game function