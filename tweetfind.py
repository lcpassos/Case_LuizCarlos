# -*- coding: utf-8 -*-
import tweepy as tw

#Lendo o arquivo com as credenciais do Twitter
#As credênciais deverão estar no arquivo twitter-credencials.txt
with open('twitter-credencials.txt', 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_token_secret = tfile.readline().strip('\n')

#Lendo o arquivo de Autenticação
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)


#Publicando tweets da minha timeline
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

#Definindo as palavras a serem buscadas
query_busca = "#openbanking"
query_busca = "#remediation"
query_busca = "#devops"
query_busca = "#sre"
query_busca = "#microservices"
query_busca = "#observability"
query_busca = "#oauth"
query_busca = "#metrics"
query_busca = "#logmonitoring"
query_busca = "#opentracing"

#Criando um cursor para acessar uma determinada quantidade de tweets
cursor_tweets = tw.Cursor(api.search,q=query_busca).items(100)

for tweet in cursor_tweets:
    print(tweet.created_at)
    print(tweet.user.name)
    print(tweet.text)




