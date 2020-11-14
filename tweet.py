import requests
import json
import tweepy
import os

# Get joke info
req = requests.get("https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&type=twopart")
joke_json = req.json()
joke_setup = (joke_json['setup'])

twitter_auth_keys = {
    "consumer_key"        : "os.environ['consumer_key']",
    "consumer_secret"     : "os.environ['consumer_secret']",
    "access_token"        : "os.environ['access_token']",
    "access_token_secret" : "os.environ['access_token_secret']"
}

auth = tweepy.OAuthHandler(
    twitter_auth_keys['consumer_key'],
    twitter_auth_keys['consumer_secret']
)
auth.set_access_token(
    twitter_auth_keys['access_token'],
    twitter_auth_keys['access_token_secret']
)
api = tweepy.API(auth)

status = api.update_status(status=joke_setup) 