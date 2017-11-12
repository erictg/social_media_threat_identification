from main.helper import mining_push as push
from main.mining import twitter_in as TI

prezis = ["nathandaschle", "fivethirtyeight", "ppppolls",
          "MysteryPollster", "senatus", "SwingState", "nprpolitics"]

for peep in prezis:
    TI.TwitterUser(peep).pushAllTweets()
