# -*- coding: utf-8 -*-
import tweepy as tw
import pandas as pd

#lendo o arquivo com as credenciais do Twitter
with open('twitter-credencials.txt', 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_token_secret = tfile.readline().strip('\n')


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

public_tweets = api.home_timeline()

#for tweet in public_tweets:
#    print(tweet.text)

print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x")

query_search = "#openbanking" + " -filter:retweets"
query_search = "#remediation" + " -filter:retweets"
query_search = "#devops" + " -filter:retweets"
query_search = "#sre" + " -filter:retweets"
query_search = "#microservices" + " -filter:retweets"
query_search = "#observability" + " -filter:retweets"
query_search = "#oauth" + " -filter:retweets"
query_search = "#metrics" + " -filter:retweets"
query_search = "#logmonitoring" + " -filter:retweets"
query_search = "#opentracing" + " -filter:retweets"

#cursor_tweets = tw.Cursor(api.search,since="2020-04-01",until="2020-06-07", q=query_search).items(100)
cursor_tweets = tw.Cursor(api.search,q=query_search).items(10)

for tweet in cursor_tweets:
    print(tweet.created_at)
    print(tweet.id_str)
    print(tweet.text)
    



