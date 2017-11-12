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
#   Tweets
#   Retweets
#   Associations

class TwitterUser:
    # Note the abbreviations if any
    def __init__(self, id):
        self.identification = id

    def getAPI(self):
        #TODO get actual user data
        return tweepy.API(auth)

    def getUName(self):
        return tweepy.Cursor(self.getAPI().user_timeline).items[1]._json["screen_name"]

    def getRName(self):
        return self.getAPI() #what a pie

    def getText(self):
        stuff = self.getData("text")
        strText = ""
        #append applied text
        strText += (api.me().description + ' ')
        #append tweets
        for txt in stuff:
            strText += (txt + ' ')
        strText = noSillyTrump(strText)
        return strText

    def getImages(self):
        # TODO write this
        return None

    def getData(self, jsonProperty):
        stuff = []
        for data in tweepy.Cursor(self.getAPI().user_timeline).items():
            stuff.append(data._json[jsonProperty])
        return stuff


    def getAssociations(self):
        stuff = []
        for friend in tweepy.Cursor(api.friends).items():
            stuff.append(friend._json["screen_name"])
        return stuff


######## bullshit #####

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

######## /bullshit #####

prezi = TwitterUser(0)