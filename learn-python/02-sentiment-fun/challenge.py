import csv
import tweepy
from textblob import TextBlob

def analyze_sentiment(text):
  sentiment = TextBlob(text)
  
  if sentiment.polarity > 0.1 and sentiment.subjectivity <= 0.5:
    return 'pos' 
  else:
    return 'neg'


# consumer key
consumer_key = 'xxx'
consumer_secret = 'xxx'

# access token
access_token = 'xxx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

filename = 'export.csv'
topic = 'iphone'
public_tweets = api.search(q=topic, count=1000)

tweets = [[w.author.name, w.created_at, w.text, analyze_sentiment(w.text)] for w in public_tweets]

# exporting the list of twets into a csv file
with open(filename, 'w') as csv_file:
  wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
  for t in tweets:
    wr.writerow(t)

