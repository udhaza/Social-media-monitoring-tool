import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = 'qZvjrJELbPt0QcyXpoLzTrP64'
api_key_secret = 'Fjilw3PEMNqRLtyNB0CAfDnfWBMaXCAPGLCtWnm59Ar9JBU5wj'

access_token = '1423921567948427268-ZQIsssBCi7UffFPuJls0Tz1oER6zsg'
access_token_secret = 'bvZtxJzixY2BOTIq1eJxxnOZLAPChlwI9K5XBSK7hUKh9'

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def search_tweets(keyword):
    tweets = api.search_tweets(q=keyword,count = 10)

    for tweet in tweets:
        print(f"Time: {tweet.created_at}")
        print(f"User: {tweet.user.screen_name}")
        print(f"Tweet: {tweet.text}")
        print("---")

# Prompt the user to enter the keyword
keyword = input("Enter the keyword to search for tweets: ")
search_tweets(keyword)
