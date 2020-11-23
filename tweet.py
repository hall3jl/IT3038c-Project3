import requests
import json
import tweepy
import os

# Get joke info
req = requests.get("https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&type=twopart")
joke_json = req.json()
joke_setup = (joke_json['setup'])

# Create object to hold API keys
twitter_auth_keys = {
    "consumer_key"        : os.environ.get('consumer_key'),
    "consumer_secret"     : os.environ.get('consumer_secret'),
    "access_token"        : os.environ.get('access_token'),
    "access_token_secret" : os.environ.get('access_token_secret')
}

# Create object to handle OAuth 
auth = tweepy.OAuthHandler(
    twitter_auth_keys['consumer_key'],
    twitter_auth_keys['consumer_secret']
)

# Add access tokens to object
auth.set_access_token(
    twitter_auth_keys['access_token'],
    twitter_auth_keys['access_token_secret']
)

# Auth with Twitter
api = tweepy.API(auth)

# Tweet the "joke"
status = api.update_status(status=joke_setup)