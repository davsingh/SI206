# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.
# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")


import tweepy
from textblob import TextBlob

# Unique code from Twitter
twit_id = "4777211295"
access_token = "4777211295-b0EzLQuPyL68ZCJhxe5PTmZVjwV5wpGhfUFHOI4" #may need to add "id-" in front
access_token_secret = "lYVpTNH1LY9HuOBGFOqxhWL2iiGkYLCcqKwdfCPDWG6FB"
consumer_key = "cEUWMmiQJ3pZjzkGxtETlADgA"
consumer_secret = "EnqNijErzB5syABvJ7YQEws2qydkSVGfSvb1qh77AZQUmi3qwS"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

message = '#UMSI-206 #Proj3'
fname = '206more.jpg'

api.update_with_media(fname, status=message)

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
