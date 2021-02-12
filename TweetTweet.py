'''
This is still in progress because I haven't yet made a developer account for my Twitter.
'''

import tweepy
import time

# from https://docs.tweepy.org/en/latest/getting_started.html

# verifies our account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

# public_tweets = api.home_timeline()

# cursor is a generator
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000) # stay on this line for 1000 milliseconds

    
# Generous bot that follows back when someone follows us
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)