import requests

url = "https://api.github.com/users/yannklein"

response = requests.get(url)
# print(response.content)
data = response.json()
print(data["blog"])