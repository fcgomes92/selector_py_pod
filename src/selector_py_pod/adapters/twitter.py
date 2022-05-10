import requests
import twitter
from selector_py_pod.models.episode import Episode
from selector_py_pod.models.selection import Selection


TEMPLATE = """{name}

{description}

"""


def short_url(url):
    r = requests.get(f'http://tinyurl.com/api-create.php?url={url}')
    return r.text


def generate_tweet(selection: Selection) -> str:
    text = TEMPLATE.format(name=selection.name,
                           description=selection.description)
    text += '\n'.join(map(lambda e: f'{e.title[0:24]}: {short_url(e.link)}',
                      selection.episodes))
    return text + '\n\n---'


class TwitterAdapter:
    def __init__(self, config) -> None:
        keys = [
            'TWITTER_CONSUMER_KEY',
            'TWITTER_CONSUMER_SECRET',
            'TWITTER_ACCESS_KEY',
            'TWITTER_ACCESS_SECRET'
        ]
        (consumer_key,
         consumer_secret,
         access_token_key,
         access_token_secret) = [config.get(key) for key in keys]
        self.client = twitter.Api(consumer_key=consumer_key,
                                  consumer_secret=consumer_secret,
                                  access_token_key=access_token_key,
                                  access_token_secret=access_token_secret)

    def post(self, selection: Selection):
        tweet = generate_tweet(selection)
        print(tweet)
        print(len(tweet))
        status = self.client.PostUpdate(tweet)
        print(status)
