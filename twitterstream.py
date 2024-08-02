import tweepy
import configparser
import streamlit as st
from datetime import datetime
import pytz

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

def convert_utc_to_local(utc_dt):
    local_tz = pytz.timezone('Asia/Kolkata')  # Indian Time Zone (Asia/Kolkata)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_dt

def search_tweets(keyword, count):
    tweets = api.search_tweets(q=keyword, count=count, tweet_mode='extended')

    for tweet in tweets:
        created_at = tweet.created_at
        local_time = convert_utc_to_local(created_at)
        local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"Time: {local_time_str}")
        st.write(f"User: {tweet.user.screen_name}")
        st.write(f"Tweet: {tweet.full_text}")
        st.write(f"Link: https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
        st.write("---")

# Streamlit app
st.title("Twitter Search")
keyword = st.text_input("Enter the keyword to search for tweets")
count = st.number_input("Enter the number of tweets to retrieve", min_value=1, max_value=100, step=1, value=10)
if st.button("Search"):
    search_tweets(keyword, count)
