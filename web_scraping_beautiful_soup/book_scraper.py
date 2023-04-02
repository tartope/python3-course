# https://books.toscrape.com/

# https://scrapy.org/
# General Docs:
# - https://docs.scrapy.org/en/latest/
# Docs for Spiders to web crawl
# https://docs.scrapy.org/en/latest/topics/spiders.html
# - will be using the spider to "crawl" from one page to another while scraping

# To run this file: scrapy runspider -o books.csv book_scraper.py
# Or run as Json: scrapy runspider -o books.json book_scraper.py

# import scrapy after installing it using pip
import scrapy

# create a class that inherits from scrapy
class BookSpider(scrapy.Spider):
    # define a name
    name = "bookspider"
    # define a list with the urls to start from
    start_urls = ["https://books.toscrape.com"]

    # define the parse method (it makes the request automatically)
    def parse(self, response):
        # css() is similar to BeautifulSoup's select(); grab all articles with the class of product_pod
        for article in response.css("article.product_pod"):
            # use yield instead of return because it's going to go over and over
            yield {
                # grab the class with that text
                "price": article.css(".price_color::text").extract_first(),
                # grab the h3, then inside move to the a tag with the attribute of title
                "title": article.css("h3 > a::attr(title)").extract_first()
            }
            # grab the link for the next page
            next = response.css(".next > a::attr(href)").extract_first()
            # if next is True
            if next:
                # follow() and pass parameters next and self.parse (the method using recursion)
                yield response.follow(next, self.parse)

