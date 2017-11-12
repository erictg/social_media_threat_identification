import tweepy
from tweepy import Stream as _S
from tweepy.streaming import StreamListener as _SL
from tweepy import OAuthHandler

consumer_key = 'LENjmBsK2AhttoeGCidENnWqh'
consumer_secret = 'zkNjS3bdPek8q5NVfTSIqFRhW4ib7ra0OM824RZKpbZORQlv9W'
access_token = '929498542166757379-lwcclANVjo07hC5uUWC9ZEhZLpGbtdg'
access_secret = 'cDOV82556X9RkwoqTFxRitYPWx2TuvdTHB5K97BOxnuv8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# sorted(set(list)) just a reference to myself, reviving python syntax.

# TODO LIST (remove as programmed and completed)
# TwitterUser
#   Username
#   Realname
#   Text
#       Profile Desc
#       Tweets
#   Img[]
#       Profile img
#       Posted img
#   Followers
#   Followings

class TwitterUser:
    # Note the abbreviations if any
    def __init__(self, uName, text, imgs, followers, following):
        self.uName = getUName()
        self.text = getText()
        self.imgs = getImages()
        self.followers = getFollowers()
        self.following = getFollowings()


def getUName():
    # TODO write this
    return None

def getGName():
    return None

def getText():
    stuff = getData("text")
    strText = ""
    for txt in stuff:
        strText += (txt + ' ')
    strText = noSillyTrump(strText)
    return strText


def getImages():
    # TODO write this
    return None


def getFollowers():
    # TODO write this
    return None


def getFollowings():
    # TODO write this
    return None


def getData(jsonProperty):
    stuff = []
    for tweet in tweepy.Cursor(api.user_timeline).items():
        stuff.append(tweet._json[jsonProperty])
        print(stuff)
    return stuff

def gJS():
    stuff = []
    for tweet in tweepy.Cursor(api.user_timeline).items():
        stuff.append(tweet._json)
        print(stuff)
    return stuff


def noSillyTrump(stuff):  # Will be implemented better eventually
    stuff.replace('...', '')
    stuff.replace('…', '')
    return stuff

print(gJS())

print(getText())

# Order of operations
#   Get ya shit together
#   Gather the shit
#   Organize the shit
#   Reorganize the shit
#   Repeat for Facebook with dat liboyary
