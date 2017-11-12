import tweepy
import time
#from tweepy import Stream
#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import template_in as TI
import mining_push as push
from time import sleep

consumer_key = 'LENjmBsK2AhttoeGCidENnWqh'
consumer_secret = 'zkNjS3bdPek8q5NVfTSIqFRhW4ib7ra0OM824RZKpbZORQlv9W'
access_token = '929498542166757379-lwcclANVjo07hC5uUWC9ZEhZLpGbtdg'
access_secret = 'cDOV82556X9RkwoqTFxRitYPWx2TuvdTHB5K97BOxnuv8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

#List
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

    def getText(self, *stuff):
        return self.usr.description

    def getTweets(self):
        stuff = []
        tweets = api.user_timeline(screen_name=self.getUName(), count=200)
        for twee in tweets:
            stuff.append(noSillyTrump(twee._json["text"]))
        return stuff

    def getAssociations(self): #Does not work
        stuff = []
        for follower in api.followers_ids(self.getUName()):
            print(follower)
            time.sleep(0.25)
            stuff.append(api.get_user(follower).screen_name)
            if len(stuff) >= 200:
                break
        print(stuff)
        return stuff #TODO fix this

    def getIdDump(self):
        stuff = self.getAssociations()
        print("got all the stuff")
        for thing in stuff:
            try:
                print("starting to push")
                TI = TwitterUser(thing)
                TI.pushAllTweets()
                print("yay2")
            except tweepy.TweepError() as err:
                print("User not available, next!")
        print(self.getUName() + "has been torn apart :)")

    def getJSON(self, tweet):
        return {
            "platform": 1,
            "username": str(self.getUName()),
            "realname": str(self.getRName()),
            "text": self.getText(),
            "tweet": tweet,
            "hyperlink": "https://twitter.com/"+self.getUName(),
            "associations": [], #self.getAssociations()
            "processed": False
        }

    def pushAllTweets(self):
        sleep(0.07)
        tweets = self.getTweets()
        for tweet in tweets:
            push.send(self.getJSON(tweet))
        print("yay")
        self.getIdDump()

def noSillyTrump(stuff):  # Upon your request, ignore the bad look for now
    return stuff.replace("...", "").replace("..", ".").replace("…", "")

#print(TwitterUser("erictg97").getAssociations())
