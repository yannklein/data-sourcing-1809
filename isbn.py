import requests

isbn = '0-7475-3269-9'
isbn_formatted = f"ISBN:{isbn}"

# https://openlibrary.org/api/books  ? bibkeys=ISBN:0-7475-3269-9 & format=json & jscmd=data

url = "https://openlibrary.org/api/books"

data = requests.get(url, params={
    "bibkeys": isbn_formatted,
    "format": "json",
    "jscmd": "data"
}).json()

print(data[isbn_formatted]["title"])