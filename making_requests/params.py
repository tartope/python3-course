# See first_request.py file that describes get requests
# See headers.py file that describes get requests with headers to get json data

import requests
url = "https://icanhazdadjoke.com/search"

# get a response from this url, that accepts json data
response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
    ) 
# the json() method takes the json and turns it into Python
# "data" will be a Python dictionary
data = response.json()

# returns the entire json object (before limit was set to 1):
# print(data)  #//=>  {'current_page': 1, 'limit': 20, 'next_page': 1, 'previous_page': 1, 'results': [{'id': 'daaUfibh', 'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}, {'id': '8UnrHe2T0g', 'joke': '‘Put the cat out’ … ‘I didn’t realize it was on fire'}, {'id': 'iGJeVKmWDlb', 'joke': 'My cat was just sick on the carpet, I don’t think it’s feline well.'}, {'id': 'AQn3wPKeqrc', 'joke': 'It was raining cats and dogs the other day. I almost stepped in a poodle.'}, {'id': 'O7haxA5Tfxc', 'joke': 'Where do cats write notes?\r\nScratch Paper!'}, {'id': '1wkqrcNCljb', 'joke': "Did you know that protons have mass? I didn't even know they were catholic."}, {'id': 'BQfaxsHBsrc', 'joke': 'What do you call a pile of cats?  A Meowtain.'}, {'id': '39Etc2orc', 'joke': 'Why did the man run around his bed? Because he was trying to catch up on his sleep!'}, {'id': 'TS0gFlqr4ob', 'joke': 'What do you call a group of disorganized cats? A cat-tastrophe.'}, {'id': '0wcFBQfiGBd', 'joke': 'Did you hear the joke about the wandering nun? She was a roman catholic.'}], 'search_term': 'cat', 'status': 200, 'total_jokes': 10, 'total_pages': 1}

# returns the value of the "results" key in the json data; a list of dictionaries where each joke has an id and the joke (before limit was set to 1)
# print(data["results"])  #//=>  [{'id': 'daaUfibh', 'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}, {'id': '8UnrHe2T0g', 'joke': '‘Put the cat out’ … ‘I didn’t realize it was on fire'}, {'id': 'iGJeVKmWDlb', 'joke': 'My cat was just sick on the carpet, I don’t think it’s feline well.'}, {'id': 'AQn3wPKeqrc', 'joke': 'It was raining cats and dogs the other day. I almost stepped in a poodle.'}, {'id': 'O7haxA5Tfxc', 'joke': 'Where do cats write notes?\r\nScratch Paper!'}, {'id': '1wkqrcNCljb', 'joke': "Did you know that protons have mass? I didn't even know they were catholic."}, {'id': 'BQfaxsHBsrc', 'joke': 'What do you call a pile of cats?  A Meowtain.'}, {'id': '39Etc2orc', 'joke': 'Why did the man run around his bed? Because he was trying to catch up on his sleep!'}, {'id': 'TS0gFlqr4ob', 'joke': 'What do you call a group of disorganized cats? A cat-tastrophe.'}, {'id': '0wcFBQfiGBd', 'joke': 'Did you hear the joke about the wandering nun? She was a roman catholic.'}]

#returns the value of the "results" key in the json data (after the limit was set to 1)
# print(data["results"])  #//=> [{'id': 'daaUfibh', 'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}]

# print(data["joke"])  #//=>
# print(f"status: {data['status']}")  #//=>