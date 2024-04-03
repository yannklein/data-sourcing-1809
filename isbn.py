import requests

isbn = '0-7475-3269-9'
formatted_isbn = f'ISBN:{isbn}'
# formatted_isbn ==> 'ISBN:0-7475-3269-9'

# https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&callback=mycallback
# url = "https://openlibrary.org/api/books?bibkeys=ISBN:0-7475-3269-9&format=json&jscmd=data"
url = "https://openlibrary.org/api/books"

response = requests.get(url, params={
    'bibkeys': formatted_isbn,
    'format': 'json',
    'jscmd': 'data'
})
data = response.json()
print(data[formatted_isbn]["title"])