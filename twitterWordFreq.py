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
    
    search_term = "#climate+change -filter:retweets"

    tweets = tw.Cursor(api.search,
                    q=search_term,
                    lang="en",
                    since='2018-11-01').items(1000)

    all_tweets = [tweet.text for tweet in tweets]
    
    print(all_tweets[0:5])
    

#Remove URLs
def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())


#Remove URLs (links)
def SearchWithoutUrl():
    search_term = "#climate+change -filter:retweets"

    tweets = tw.Cursor(api.search,
                    q=search_term,
                    lang="en",
                    since='2018-11-01').items(1000)

    all_tweets = [tweet.text for tweet in tweets]
    all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
    print(all_tweets_no_urls[:5])


#Create List of Lower Case Words from Tweets
def WordSplitAndLowering():
    search_term = "#climate+change -filter:retweets"

    tweets = tw.Cursor(api.search,
                    q=search_term,
                    lang="en",
                    since='2018-11-01').items(1000)

    all_tweets = [tweet.text for tweet in tweets]
    all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]

    print(all_tweets_no_urls[0].lower().split())

    words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]
    print(words_in_tweet[:2])


def CountWord():
    search_term = "#climate+change -filter:retweets"

    tweets = tw.Cursor(api.search,
                    q=search_term,
                    lang="en",
                    since='2018-11-01').items(1000)

    all_tweets = [tweet.text for tweet in tweets]
    all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]

    #print(all_tweets_no_urls[0].lower().split())

    words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]

    # List of all words across tweets
    all_words_no_urls = list(itertools.chain(*words_in_tweet))

    # Create counter
    counts_no_urls = collections.Counter(all_words_no_urls)

    #print(counts_no_urls.most_common(15))

    #sitede dataframe yapildigini görmeden kendim yaptim :P
    clean_tweets_no_urls = pd.DataFrame(data=counts_no_urls.most_common(15), 
                        columns=['kelime', "sayisi"])
    print(clean_tweets_no_urls)

def DrawTweetPlot():

    search_term = "#climate+change -filter:retweets"

    tweets = tw.Cursor(api.search,
                    q=search_term,
                    lang="en",
                    since='2018-11-01').items(1000)

    all_tweets = [tweet.text for tweet in tweets]
    all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]

    #print(all_tweets_no_urls[0].lower().split())

    words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]

    # List of all words across tweets
    all_words_no_urls = list(itertools.chain(*words_in_tweet))

    # Create counter
    counts_no_urls = collections.Counter(all_words_no_urls)

    #print(counts_no_urls.most_common(15))

    #sitede dataframe yapildigini görmeden kendim yaptim :P
    clean_tweets_no_urls = pd.DataFrame(data=counts_no_urls.most_common(15), 
                        columns=['words', "count"])
    
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot horizontal bar graph
    clean_tweets_no_urls.sort_values(by='count').plot.barh(x='words',
                        y='count',
                        ax=ax,
                        color="purple")

    ax.set_title("Common Words Found in Tweets (Including All Words)")

    plt.show()
DrawTweetPlot()