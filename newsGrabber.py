from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key= "Enter API Key Here")
top_headlines = newsapi.get_top_headlines(country='us')
print(top_headlines)
