import requests

url = "https://api.github.com/users/MyoungchulK"

response = requests.get(url)
# print(response.content)
data = response.json() # parse the json (= converting the json text into some python code)
print(data['bio'])