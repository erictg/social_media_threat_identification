import tweepy
#from tweepy import Stream
#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from main.mining import template_in as TI

consumer_key = 'LENjmBsK2AhttoeGCidENnWqh'
consumer_secret = 'zkNjS3bdPek8q5NVfTSIqFRhW4ib7ra0OM824RZKpbZORQlv9W'
access_token = '929498542166757379-lwcclANVjo07hC5uUWC9ZEhZLpGbtdg'
access_secret = 'cDOV82556X9RkwoqTFxRitYPWx2TuvdTHB5K97BOxnuv8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Get more data based on data?  Pulled from web.

# class MyListener(StreamListener):
#     def on_data(self, data):
#         try:
#             with open('python.json', 'a') as f:
#                 f.write(data)
#                 return True
#         except BaseException as e:
#             print("Error on_data: %s" % str(e))
#         return True
#
#     def on_error(self, status):
#         print(status)
#         return True

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

    def getTweets(self):
        stuff = []
        stuff.append(self.usr.description)
        tweets = api.user_timeline(screen_name=self.getUName(), count=200)
        for twee in tweets:
            stuff.append(noSillyTrump(twee._json["text"]))
        return stuff

    @property
    def getAssociations(self): #Does not work
        stuff = []
        for friend in tweepy.Cursor(api.user_timeline(self.getUName())).items():
            stuff.append(friend._json)
        return stuff
        # stuff = []
        # friends = self.usr.friends
        # for fri in friends:
        #     stuff.append(fri)
        # return stuff

    def getJSON(self):
        return {
            "platform": "1",
            "username": str(self.getUName()),
            "realname": str(self.getRName()),
            "text": self.getTweets(),
            "hyperlink": "https://twitter.com/"+self.getUName(),
            "associations": [] #self.getAssociations
        }

def noSillyTrump(stuff):  # Upon your request, ignore the bad look for now
    return stuff.replace("...", "").replace("..", ".").replace("…", "")

# def getTheJ(*stuff):
#     sub_stuff = []
#     try:
#         for thing in stuff:
#             sub_stuff.append(thing._json.getJSON())
#     except TypeError as err:
#         print("Wrong shit")
#     return sub_stuff

prezis = [
    TwitterUser("realDonaldTrump"),
    TwitterUser("PutinRF_Eng"),
    TwitterUser("odenathb"),
    TwitterUser("erictg97")
    ]

dumpableShit = []

for fuckhead in prezis:
    dumpableShit.append(fuckhead.getJSON())

print(dumpableShit[0])

# def getTwitterStream(searchterm): #Need to test
#     twitter_stream = Stream(auth, MyListener())
#     twitter_stream.filter(track=[searchterm])
#     return twitter_stream
#
