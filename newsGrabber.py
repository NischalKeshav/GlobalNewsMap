from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='4bb8b4df3f1a4b92925eafa0c4b22845')
top_headlines = newsapi.get_top_headlines(country='us')
print(top_headlines)
