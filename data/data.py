import requests
url = ('https://newsapi.org/v2/everything?q=coronavirus&apiKey=41ff73330072433da7a7f9b8171e5989')
response = requests.get(url)
dico = response.json()
print(dico['articles'])
