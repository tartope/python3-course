from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import choice

# make title function (no parameters needed)
def print_ascii_title():
    # create title and assign to variable
    title = "DAD JOKE 3000"
    # make title ascii using figlet_format import and assign to variable
    ascii_title = figlet_format(title)
    # give ascii_title color using colored import and assign to variable
    colored_title = colored(ascii_title, color="blue")
    print(colored_title)
print_ascii_title()

url = "https://icanhazdadjoke.com/search"

# grab user input
user_input = input("Let me tell you a joke! Give me a topic: ")

# grab json response in variable
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    # to search for jokes, use search term "term" as a key (from API documentation), and set it's value to user_input
    params={"term": user_input}
)
# convert the json data into Python readable code
data = response.json()

# make dad_jokes function that accepts a parameter
def dad_jokes(input):
    # grab number of jokes (a key in the json data)
    num_jokes = data["total_jokes"]
    # grab results with dictionary of jokes (a key in the json data)
    results = data["results"]
    if num_jokes > 1:
        print(f"I've got {num_jokes} about {input}. Here's one:")
        # use choice import to randomly grab a joke
        print(choice(results)["joke"])
    elif num_jokes == 1:
        print(f"I've got {num_jokes} about {input}. Here it is:")
        # grab the first dictionary in the list and the value of its "joke" key
        print(results[0]["joke"])
    else:
        print(f"Sorry, I don't have any jokes about {input}. Please try again.")

dad_jokes(user_input)