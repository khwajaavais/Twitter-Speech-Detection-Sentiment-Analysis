## Importing Packages
import tweepy
import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 1000)
import time

## Setting KEYS
# API KEY
# Refer My girhub profile for creating Tokens and Keys
api_key = "AK"
api_key_secret = "AKS"
# Access Token
access_token = "AT"
access_token_secret = "ATS"

## API Aithentication
authentication = tweepy.OAuthHandler(api_key, api_key_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

## Getting Tweets related to words entered
def get_related_tweets(text):
    '''
    This function will help you to fetch real-time data from Twitter Using Python via Tweepy.
    This function requires one parameter i.e. the text. 
    This will be searched in the Twitter to fetch the tweets related to entered keyword.
    
    Returns the data in the form of Pandas DataFrame which include the Tweet Time, Tweet ID and the Actual Tweet.
    '''
    
    ## Setting KEYS
    # API KEY
    api_key = "fcJESZ5sIhOyJ36Gtb34xKOiI"
    api_key_secret = "yLTe2IxT9csyRUl0FbdwlKy77AOXmpliIlYOxFnZB6aaslVLUv"
    # Access Token
    access_token = "1442924034266521602-7zmGLoz2zrEfNL6ahTCYPSnVUlExyc"
    access_token_secret = "3kfnme3pFiPfrRXlH6DuYFSByu0ZZqtWeZmJQHeBmqpac"

    ## API Aithentication
    authentication = tweepy.OAuthHandler(api_key, api_key_secret)
    authentication.set_access_token(access_token, access_token_secret)
    api = tweepy.API(authentication, wait_on_rate_limit=True)
    
    # List to store the tweets
    tweet_list = []    
    # No of tweet to be searched
    n = 50

    try:
        for tweet in api.search_tweets(q=text, count=n, lang="en"):
            ## Adding the tweets to the list
            tweet_list.append(
            {
                'Created_At':tweet.created_at,
                'Tweet_Id': tweet.id,
                'Tweet_Text': tweet.text
            })
            
        return pd.DataFrame.from_dict(tweet_list)
    
    except BaseException as e:
        print(f'Failed On_Status {e}')
        time.sleep(3)