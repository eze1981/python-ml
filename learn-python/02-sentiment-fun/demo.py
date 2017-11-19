import tweepy
from textblob import TextBlob

# consumer key
consumer_key = 'xxx'
consumer_secret = 'xxx'

# access token
access_token = 'xxx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('iphone')
for tweet in public_tweets:
  print(tweet.text)
  analysis = TextBlob(tweet.text)
  print(analysis.sentiment)
  print('------------------------------------------------------------------------------------')
