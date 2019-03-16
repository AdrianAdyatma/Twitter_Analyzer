import json
import tweepy

import credentials_var as cred

# User credentials to access Twitter API
ACCESS_TOKEN = "94752564-BvP4ZNJawmbcBbZfl9V9fVxCMqBEw3C3XfspEZFbZ"
ACCESS_TOKEN_SECRET = "tXyHXu7vJt6k3YlnPNm5JI8gBbfqIfQzOVWhlKzH1GNMS"
CONSUMER_KEY = "VDUHKifMgzsf0z98tEeaqgBkU"
CONSUMER_SECRET = "ukVf6fqYeqUeZ10WeMjv0a35DfZw79INqgzEM8Rat9y2pxncr5"

# Twitter authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    count = 0

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.db = cred.TwitterDB

    def on_data(self, tweet):
        full_data = json.loads(tweet)
        print(full_data)
        cred.tweets_0.insert_one(full_data)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

    def on_timeout(self):
        return True


tweetStream = tweepy.Stream(auth, CustomStreamListener(api))

# The list of keywords for filtering tweets
keywordList = ['jokowi']

# Start streaming tweets
tweetStream.filter(track=keywordList)
