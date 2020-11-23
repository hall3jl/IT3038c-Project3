# IT3038c-Project3

## Description
The purpose of this script is to retrieve jokes from [SV443](https://sv443.net/jokeapi/v2/) and create a tweet that only contains the setup of the joke. 

It's really dumb, but I thought it was entertaining :).

## Running the Script
The recommended way of running this bot is in Heroku since this involves API keys. There is currently a demo instance of this bot posting to [@NotReallyaJoke](https://twitter.com/NotReallyAJoke).

If you wish to setup your own instance of this bot, please see the following basic steps:
1. Clone this repo
2. [Create a Twitter application](https://docs.inboundnow.com/guide/create-twitter-application/) and make note of the API keys you get
3. Create a new app in Heroku
4. Deploy this repo to Heroku
5. Fill in the following Config Vars with the API keys provided by Twitter
	- access_token
	- access_token_secret
	- consumer_key
	- consumer_secret
6. Use the "Heroku Scheduler" add-on to run the script on an interval of your choosing. The run command will be "python tweet.py"
