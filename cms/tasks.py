from hpcweb.celery import app
from newsapi import NewsApiClient

@app.task
def get_news_headline():
    newsapi = NewsApiClient(api_key='162e22aa0e4340ea8f34c61cba34749a')
    top_headlines = newsapi.get_top_headlines(category='science',
                                              language='en',
                                            )
    return top_headlines