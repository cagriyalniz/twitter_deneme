import tweepy as tw
import apiKeyAccess
import pandas as pd
keyim = apiKeyAccess.bilgiler()
    
        
    # # #Creating the authentication object
auth = tw.OAuthHandler(keyim.consumerKey, keyim.consumerSecretKey)
    # # #Setting your access token and secret
auth.set_access_token(keyim.accessToken, keyim.accessTokenSecret)
    # # #Creating the API object while passing in auth information
api = tw.API(auth) 

search_words = "odyoloji"
date_since1 = "2016-06-16"
date_since2 = "2018-06-16"
date_since3 = "2021-06-16"

# tweets1 = tw.Cursor(api.search,
#               q=search_words,
#               lang="tr",
#               since=date_since1).items(1)

# tweets2 = tw.Cursor(api.search,
#               q=search_words,
#               lang="tr",
#               since=date_since2).items(1)

# tweets3 = tw.Cursor(api.search,
#               q=search_words,
#               lang="tr",
#               since=date_since3).items(1)


# for tweet in tweets1:
#     print(tweet.text)

# for tweet in tweets2:
#     print(tweet.text)

# for tweet in tweets3:
#     print(tweet.text)

def UserLocation():
    new_search = search_words + " -filter:retweets"

    tweets = tw.Cursor(api.search, 
                        q=search_words,
                        lang="tr",
                        since=date_since2).items(15)

    users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
    print(users_locs)

    tweet_text = pd.DataFrame(data=users_locs, 
                        columns=['user', "location"])
    print(tweet_text)
