# -*- coding: utf-8 -*-
import tweepy as tw

#lendo o arquivo com as credenciais do Twitter
with open('twitter-credencials.txt', 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_token_secret = tfile.readline().strip('\n')


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)


#Publicando tweets da minha timeline
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

query_search = "#openbanking"
query_search = "#remediation"
query_search = "#devops"
query_search = "#sre"
query_search = "#microservices"
query_search = "#observability"
query_search = "#oauth"
query_search = "#metrics"
query_search = "#logmonitoring"
query_search = "#opentracing"


cursor_tweets = tw.Cursor(api.search,q=query_search).items(100)

for tweet in cursor_tweets:
    print(tweet.created_at)
    print(tweet.id)
    print(tweet.text)


