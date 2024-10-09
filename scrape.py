import requests
from bs4 import BeautifulSoup 

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'session-id=133-0219319-4854613; session-id-time=2082787201l; ad-oo=0; ubid-main=135-1403587-6009451; gpc-cache=1; ci=e30; session-token=uAzFw2J401pY0dY9WfO/404rbpI4sH26cRnlOfUfi6G+jvvDYNbbigCWnqmyNXtni6/GhxpY/aZ7PPQZmQWUDR3RGc0wRPRWb7l49TKqJAU4puM5joqrkcxx15tCRNZ1oBR9PGDES1h9FKquJcU7zlNOpMkeJc8L5Ui/C5u+LrFuhzJwWF8fc99Ns1rMhhTtUW/b/uRH3C7pYP4MbUtjSHScmw6/dLPLnT6fW/KXkm6tNT8TOtRREE3p2KaPTYUPoRLYlf/64LqKxz4DuMVh1W+yb0srPCzAvxJwWmVKaeYln6iAHd2wXm+HFgcD00YKNwm+VbzOrXmxrqt3GsqnJOaTW/AThtJx; csm-hit=tb:7DK032W7S3XC3WK09ZY6+s-7DK032W7S3XC3WK09ZY6|1728437573829&t:1728437573829&adb:adblk_yes',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url, headers=headers)
html_doc = response.content
# print(html_doc)

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup)

movies = soup.find_all(class_="sc-59c7dc1-2")

for movie in movies:
    title = movie.find("h3").string.split(". ")[1]
    duration = movie.find_all(class_="sc-ab348ad5-8")[1].string
    print(title, duration)