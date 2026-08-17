import requests

API_KEY = "824b635728e749a7815b995df5a4ff61"

url = "https://newsapi.org/v2/everything"

params = {
    "q": "Apple stock",
    "language": "en",
    "sortBy": "publishedAt",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)

data = response.json()

# (['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'])
for i, article in enumerate(data["articles"]):
    print(article["publishedAt"])
    print(article["title"])
    print(article["url"])
    
    print("----------")
    if i == 4:
        break
