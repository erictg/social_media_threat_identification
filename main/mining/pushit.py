import mining_push as push
import twitter_in as TI
#
# prezis = ["nathandaschle", "fivethirtyeight", "ppppolls",
#           "MysteryPollster", "senatus", "SwingState", "nprpolitics"]
#
# for peep in prezis:
#     for follower in TI.TwitterUser(peep):

TI.TwitterUser("realDonaldTrump").pushAllTweets()
