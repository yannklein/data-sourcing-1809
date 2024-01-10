import requests

isbn = '0-7475-3269-9'
isbn_formatted = f"ISBN:{isbn}"

url = f"https://openlibrary.org/api/books?bibkeys={isbn_formatted}&format=json&jscmd=data"
print(url)

data = requests.get(url).json()

print(data[isbn_formatted]["title"])