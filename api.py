import requests

url = "https://api.github.com/users/yannklein"

response = requests.get(url)
print(response)
data = response.json()
print(data)
print(data['blog'])