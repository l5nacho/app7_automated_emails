# api key - d1b9ee17a8e44b23b72a3ac33d12aad2

import requests

class NewsFeed:
    api_key = 'd1b9ee17a8e44b23b72a3ac33d12aad2'

    def __init__(self, topic, date_from, date_to, lang='en'):
        self.topic = topic
        self.date_from = date_from
        self.date_to = date_to
        self.lang = lang

    def get(self):
        url = f'https://newsapi.org/v2/everything?' \
              f'q={self.topic}&' \
              f'from={self.date_from}&' \
              f'to={self.date_to}&' \
              f'language={self.lang}&' \
              f'apiKey={self.api_key}'

        req = requests.get(url)
        json = req.json()
        email_body = ''
        for article in json['articles']:
            email_body = email_body + article['title'] + ' - ' + article['url'] + '\n'

        return email_body
