# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
import statistics
from textblob import TextBlob

term = 'Cubs'

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

public_tweets = api.search(term)

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment.polarity)
	print(analysis.sentiment.subjectivity)

p_list = [TextBlob(tweet.text).sentiment.polarity for tweet in public_tweets]
s_list = [TextBlob(tweet.text).sentiment.subjectivity for tweet in public_tweets]

p_avg = statistics.mean(p_list)
s_avg = statistics.mean(s_list)

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data


print("Average subjectivity is", s_avg)
print("Average polarity is", p_avg)