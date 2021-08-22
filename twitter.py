import tweepy
import apiKeyAccess
    
keyim = apiKeyAccess.bilgiler()
    
        
    # # #Creating the authentication object
auth = tweepy.OAuthHandler(keyim.consumerKey, keyim.consumerSecretKey)
    # # #Setting your access token and secret
auth.set_access_token(keyim.accessToken, keyim.accessTokenSecret)
    # # #Creating the API object while passing in auth information
api = tweepy.API(auth) 




# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets

def Timeline():
    public_tweets = api.home_timeline()
    # foreach through all tweets pulled
    for tweet in public_tweets:
        # printing the text stored inside the tweet object
        print(tweet.text)   

#Timeline()


#Tweets from a Specific User

def UsersTweet():
    # The Twitter user who we want to get tweets from
    name = "cagriyalniz"
    # Number of tweets to pull
    tweetCount = 20

    # Calling the user_timeline function with our parameters
    results = api.user_timeline(id=name, count=tweetCount)
    
    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        print(tweet.text)

#UsersTweet()

#Finding Tweets Using a Keyword

def KeywordTweets():
 
    
    # The search term you want to find
    query = "çağrı yalnız"
    # Language code (follows ISO 639-1 standards)
    language = "tr"

    # Calling the user_timeline function with our parameters
    results = api.search(q=query, lang=language)
    
    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        print(tweet.user.screen_name,"Tweeted:",tweet.text)

#KeywordTweets()


def FriendshipDetails():

    screen_names = ["ecole42kocaeli",
                "42born2code"]
  
    # getting the friendship details
    friendships = api.lookup_friendships(screen_names = screen_names)
    
    for friendship in friendships:
        print("Is the authenticated user following " + friendship.screen_name, end = "? : ")
        print(friendship.is_following)

FriendshipDetails()