import logging
from logstash_formatter import LogstashFormatterV1
from main.helper import mining_push as push
from main.mining import twitter_in as TI

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = LogstashFormatterV1()

handler.setFormatter(formatter)
logger.addHandler(handler)

prezis = [
    TI.TwitterUser("realDonaldTrump"),
    TI.TwitterUser("PutinRF_Eng"),
    TI.TwitterUser("KremlinRussia_E"),
    TI.TwitterUser("odenathb"),
    TI.TwitterUser("erictg97")
    ]

for fuckhead in prezis:
    push.send(fuckhead.getJSON())
