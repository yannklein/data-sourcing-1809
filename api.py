import requests

url = "https://api.github.com/users/yannklein"

response = requests.get(url)
data = response.json()
print(data['blog'])