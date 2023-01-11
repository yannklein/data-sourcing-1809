import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url, headers={"Accept-Language": "en-US"})

# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")

# h1 = soup.find("h1")
# print(h1)

movies = soup.find_all("div", class_="lister-item-content")
for movie in movies:
    title = movie.find("a").string
    duration = int(movie.find("span", class_="runtime").string.strip(" min"))
    print(title, duration)