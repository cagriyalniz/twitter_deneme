#dt = deneme tahtası :P

import datetime
import nltk
from nltk.util import pr
from nltk.corpus import stopwords
from datetime import date
import os
from nltk.util import pr
import tweepy as tw
import apiKeyAccess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import nltk
from nltk.corpus import stopwords
import re
import networkx
import warnings
#https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/
#WithoutStopWordsDrawTweetPlot // DrawTweetPlot // CountWord

keyim = apiKeyAccess.bilgiler()
    # # #Creating the authentication object
auth = tw.OAuthHandler(keyim.consumerKey, keyim.consumerSecretKey)
    # # #Setting your access token and secret
auth.set_access_token(keyim.accessToken, keyim.accessTokenSecret)
    # # #Creating the API object while passing in auth information
api = tw.API(auth, wait_on_rate_limit=True)

warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

# "iklimdegisikligi" kelimesini iceren 1000 tiviti alip listeleyeceğiz

def SimpleSearch():
    
    #search_term = "#climate+change -filter:retweets"

    alinan_search_term = input("aranacak kelimeyi yazin")
    search_term = str(alinan_search_term) + " -filter:retweets"
    
    alinan_since = input("""baslangic tarihini 
                            yıl-ay-gün formatında giriniz""")
    since1 = str(alinan_since)
    
    tweets = tw.Cursor(api.search,
                    q=search_term,
                    lang="tr",
                    since=since1).items(1000)

    all_tweets = [tweet.text for tweet in tweets]
    
    print(all_tweets[0:5])

SimpleSearch()


# my_list = ["ayı", 1 , 1, 1, 2, "kaya", "ayı"]
# print(set(my_list))

# search_term = "#climate+change -filter:retweets"
# print(type(search_term))

# def KelimeGonderme():

#     x =input("aranacak kelimeyi yazin: ")
#     print(x)

#KelimeGonderme()

# nltk.download('stopwords')
# stop_words = set(stopwords.words('turkish'))

#View a few words from the set
#print(list(stop_words)[0:100])

# alinan_tarih = input("hangi tarihten itibaren bakilsin")
# since = alinan_tarih
# print(type(since))
# if type(since) != datetime:
#     print("tarih değil")
# else:
#     print(since)