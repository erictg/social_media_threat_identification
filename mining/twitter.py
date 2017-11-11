import tweepy as twp
from tweepy import Stream as _S
from tweepy.streaming import StreamListener as _SL

#auth = twp.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = twp.API(auth)

#sorted(set(list))

#TODO LIST (remove as programmed and completed)
#TwitterUser
#   Username
#   Text
#       Profile Desc
#       Tweets
#   Img[]
#       Profile img
#       Posted img
#   Followers
#   Followings

class TwitterUser:
    #Note the abbreviations if any
    def __init__(self, uName, text, imgs, followers, following):
        self.uName = getUName()
        self.text = getText()
        self.imgs = getImages()
        self.followers = getFollowers()
        self.following = getFollowings()

def getUName():
    #TODO write this
    return None

def getText():
    #TODO write this
    return None

def getImages():
    #TODO write this
    return None

def getFollowers():
    #TODO write this
    return None

def getFollowings():
    #TODO write this
    return None

#Order of operations
#   Get ya shit together
#   Gather the shit
#   Organize the shit
#   Reorganize the shit
#   Repeat for Facebook with dat liboyary



