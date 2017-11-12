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
        self.usr = api.get_user(id)

    def getUName(self):
        return self.usr.screen_name

    def getRName(self):
        return self.usr.name

    def getText(self):
        stuff = []; strText = self.usr.description + " "
        tweets = api.user_timeline(screen_name = self.getUName(), count=200)
        for txt in stuff:
            strText += (txt + ' ')
            strText = noSillyTrump(strText)
        return strText

    def getAssociations(self):
        stuff = self.getData(self.usr.friends, "screen_name")
        return stuff

    # #Refactoring bullshit
    # def getData(self, location, jsonProperty):
    #     stuff = []
    #     for data in tweepy.Cursor(location).items():
    #         stuff.append(data._json[jsonProperty])
    #     return stuff


######## bullshit #####

def noSillyTrump(stuff):  # Will be implemented better eventually
    stuff.replace("...", "")
    stuff.replace("…", "")
    return stuff

######## /bullshit #####

prezi = TwitterUser("realDonaldTrump")
print(prezi.getUName())
print(prezi.getRName())
#print(prezi.getAssociations())
print(prezi.getText())
