# install the requests module: python3 -m pip install requests
# Lines below practiced in Python3 REPL:
import requests  # import the installed module
# res = requests.get("https://news.ycombinator.com/")  (get request of this site saved to a variable)
# res #//=> <Response [200]>
# res.ok #//=> True                 <-- returns a boolean about the response
# res.headers #//=> {'Server': 'nginx', 'Date': 'Thu, 26 Jan 2023 00:28:38 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Cache-Control': 'private; max-age=0', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'origin', 'Strict-Transport-Security': 'max-age=31556900', 'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.google.com/recaptcha/ https://www.gstatic.com/recaptcha/ https://cdnjs.cloudflare.com/; frame-src 'self' https://www.google.com/recaptcha/; style-src 'self' 'unsafe-inline'; img-src 'self' https://account.ycombinator.com; frame-ancestors 'self'", 'Content-Encoding': 'gzip'}          <-- includes all the metadata
# res.text  (the main part of the response that comes back; returns a giant block of html; basically the "view source" html seen in the browser using our dev tools)

url = "http://www.google.com"
response = requests.get(url)

# with correct url "http://www.google.com"
print(f"your request to {url} came back with status code {response.status_code}")  #//=> your request to http://www.google.com came back with status code 200
# with incorrect url "http://www.google.com/asdasd/asd"
print(f"your request to {url} came back with status code {response.status_code}")  #//=> your request to http://www.google.com/asdasd/asd came back with status code 404
# with "http://" remove from request
print(f"your request to {url} came back with status code {response.status_code}")  #//=> requests.exceptions.MissingSchema: Invalid URL 'www.google.com': No scheme supplied. Perhaps you meant https://www.google.com?

# print(response.text)          <-- returns a giant block of html from google