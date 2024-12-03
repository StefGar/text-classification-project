import tweepy
import csv

API_KEY = 'tu_api_key'
API_SECRET = 'tu_api_secret'
ACCESS_TOKEN = 'tu_access_token'
ACCESS_TOKEN_SECRET = 'tu_access_token_secret'

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def recolectar_tweets(query, num_tweets, output_file):
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="es", tweet_mode="extended").items(num_tweets):
        tweets.append([tweet.user.screen_name, tweet.created_at, tweet.full_text])
    
    with open(output_file, mode='w', encoding='utf-8', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["usuario", "fecha", "texto"])  # Cabecera
        escritor.writerows(tweets)

recolectar_tweets("tecnología", 1000, "data/raw/tweets.csv")
