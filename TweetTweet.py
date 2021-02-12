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
    # as soon as we hit the rate limit, we pause for a few milliseconds, then continue
    # this is because of Twitter's rate limit
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000) # stay on this line for 1000 milliseconds

    
# Generous bot that follows back when someone follows us
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    pass
    # if follower.followers_count > 100:
    #     follower.follow()

    # if follower.name == 'dindin': # name of follower
    #     follower.follow()
    #     break

    # print(follower.name) # prints the followers


# Narcissist Bot that loves your own tweets and others weets

search_string = 'python'
numbersOfTweets = 2

for tweet in limit_handle(tweepy.Cursor(api.search, search_string).items(numbersOfTweets)):
    pass
    # try:
    #     tweet.favorite()
    #     tweet.retweet()
    #     print('I liked that tweet.')
    # except tweepy.TweepError as e:
    #     print(e.reason)
    # except StopIteration:
    #     break


