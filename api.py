import requests

url = "https://api.github.com/users/yannklein"

raw_data = requests.get(url)
# print(raw_data.content)
data = raw_data.json()
print(data['blog'])