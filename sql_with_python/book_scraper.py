import sqlite3
import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/catalogue/category/books/history_32/index.html"
    
# scrapes the books using other functions made, and calls the save_books to make and push to the db
def scrape_books(url):
    # Request URL
    response = requests.get(url)

    # Initialize BS
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract Data we want
    # this finds all article tags in the html (the article tags contain the book titles)
    books = soup.find_all("article")
    # make a list of all books
    all_books = []
    # loop through the books list, and pass each function
    for book in books:
        # store in a tuple the title, price, and rating
        book_data = (get_title(book), get_price(book), get_rating(book))
        # push the data into the all books list
        all_books.append(book_data)
    
    # after making save_books db function, call it here
    save_books(all_books)

# creates the db, and saves the books to the db
def save_books(all_books):
    # connect to db
    connection = sqlite3.connect("books.db")

    # create cursor
    c = connection.cursor()

    # use triple quotes to use multiple lines
    # create the db table (easiest to set up in the order of the data in the all_books list)
    # better to put this in another function so it's not called/re-created everytime
    c.execute('''CREATE TABLE books
        (title TEXT, price REAL, rating INTEGER)''')
    
    # bulk insert values using executemany()
    c.executemany("INSERT INTO books VALUES (?, ?, ?)", all_books)

    # commit changes
    connection.commit()

    # at very end, close connection
    connection.close()

# gets the title of books
def get_title(book):
    # get the book title: for each book find the h3 tag (child of article), within that h3 find the a tag (child of h3), within that a tag find the title
    return book.find("h3").find("a")["title"]

# gets the price of books
def get_price(book):
    # get the price: for each book select class= "price_color", it prints a list so grab the first element, grab the inner text
    price = book.select(".price_color")[0].get_text()
    # remove the currency symbol, and change to float
    return float(price.replace("£","").replace("Â",""))

# gets the ratings of books
def get_rating(book):
    # create a dictionary to convert string ratings to ints
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    # get the star ratings: for each book select class= "star-rating", it prints a list so grab the first element
    paragraph = book.select(".star-rating")[0]
    word = paragraph.get_attribute_list("class")[-1]
    # find the integer value of the string "word" from the dictionary "ratings"
    return ratings[word]

# call scrape_books to run it all
scrape_books(url)

# Save data to db