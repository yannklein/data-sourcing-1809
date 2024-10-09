import requests

isbn = '0-7475-3269-9'
formatted_isbn = f"ISBN:{isbn}"

# url = f"https://openlibrary.org/api/books?bibkeys={formatted_isbn}&format=json&jscmd=data"
url = f"https://openlibrary.org/api/books"
print(url)

data = requests.get(url, params={
    'bibkeys': formatted_isbn,
    'format': 'json',
    'jscmd': 'data'
}).json()

print(data[formatted_isbn]["title"])