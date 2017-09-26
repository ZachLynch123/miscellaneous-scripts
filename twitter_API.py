#Twitter API that draws tweets with the cooresponding search term
import tweepy
import textblob
consumer_Key = 'XXXX...'
consumer_Secret = 'XXXX...'

access_Key = 'XXXX....'
access_Secret = 'XXXX...'

auth = tweepy.OAuthHandler(consumer_Key,consumer_Secret)
auth.set_access_token(access_Key,access_Secret)

search_term = 'Trump'

API = tweepy.API(auth)

public_Tweets = API.search(search_term)

for tweet in public_Tweets:
	print tweet.text.encode('utf-8')

#Will make a small website with search bar as input and display the results on the page