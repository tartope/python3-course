# See first_request.py file that describes get requests
import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "text/plain"})      #<-- "text/plain" doesn't give all the html, just the plain text (most websites aren't setup to give plain text)
# this print statement returns a string
# print(response.text)  #//=> A man is washing the car with his son. The son asks...... "Dad, canât you just use a sponge?"
# print(type(response.text))  #//=> <class 'str'>

# get a response from this url, that accepts json data
response = requests.get(url, headers={"Accept": "application/json"}) 
# the json() method takes the json and turns it into Python
# "data" will be a Python dictionary
data = response.json()
# print(type(data)) #//=> <class 'dict'>
# print(data)  #//=>  {'id': 'sHlqrjyPf', 'joke': 'How can you tell a vampire has a cold? They start coffin.', 'status': 200}
# print(data["joke"])  #//=> How can you tell a vampire has a cold? They start coffin.
# print(f"status: {data['status']}")  #//=>  status: 200