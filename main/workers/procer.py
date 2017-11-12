import main.processing.language_processing.syntax_analyzer as sa
import json
from main.processing.language_processing.language_data.words import  getSwearWords, getLexicon, getBigotWords
import time
import requests
from main.helper.mining_push import sendWithIndex
from main.processing.main import determineThreat
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

swear_words = getSwearWords()
lexicon = getLexicon()
bigot = getBigotWords()
pos = "positive"
neg = "negitive"


def processSentences(sentences):
    return sa.sendSentence(sentences)

def answer(id, yes, data):

    result = requests.delete(url="http://104.196.181.214:9200/mine/pre/" + id )
    print(result.status_code)
    print(result.json())

    if yes:
        result = requests.post(url="http://104.196.181.214:9200/proc/training_manual_yes",
                               data=json.dumps(data["hits"]["hits"][0]["_source"]))
        print(result.status_code)
        print(result.text)
    else:
        result = requests.post(url="http://104.196.181.214:9200/proc/training_manual_no", data=json.dumps(data["hits"]["hits"][0]["_source"]))
        print(result.status_code)
        print(result.text)

def scorePositivity(sentences):
    posScore = 0
    print(sentences)
    #verb match pos or neg
    for word in sentences:
        print(word)
        for words in word["output"]:
            if words["word"] in lexicon:
                res = lexicon[words["word"]]
                if res != None:
                    if word["VerbForm"] != None:
                        if res is pos:
                            posScore += 1
                        elif res is neg:
                            posScore -= 1
    return posScore

def swearCount(sentences):
    c = 0
    for i in sentences:
        for word in i["output"]:
            res = word["word"]
            if res in swear_words:
                c += 1
    return c

def excitementLevel(sentences):
    eCount = 0
    # verb match pos or neg
    for i in sentences:
        for word in i["output"]:
            res = word["word"]
            if res is "!":
                eCount += 1

    return eCount


def bigotCount(sentences):
    bCount = 0
    # verb match pos or neg
    for i in sentences:
        for word in i["output"]:
            res = word["word"]
            if res in bigot:
                bCount += 1

    return bCount

def addUserNameIfExists(username, real_name = None):
    query = {
        "from": 0,
        "size": 1,
        "query": {
            "term": {
                "username": record["username"]
            }
        }
    }

    req = requests.request(method="get", url="http://104.196.181.214:9200/mine/pre/_search",
                                  data=json.dumps(query))

    rqObj = req.json()

    if rqObj["_shards"]["total"] > 0:
        return

    toSend = {
        "username": username,
        "real_name": real_name,
        "hit_count": 0
    }

    sendWithIndex("found_names")

def calculateText(text):

    sentences = processSentences(text)

    _positivity = sigmoid(scorePositivity(sentences))
    _excitement = sigmoid(excitementLevel(sentences))
    _bigot = sigmoid(bigotCount(sentences))
    _swear = sigmoid(swearCount(sentences))

    return [_positivity, _excitement, _bigot, _swear]

sa.init()

while True:
    time.sleep(10)
    for i in range (10):
        query = {
            "from": 0,
            "size": 1,
            "query": {
                "term": {
                    "processed": "false"
                }
            }
        }

        result = requests.request(method="get", url="http://104.196.181.214:9200/mine/pre/_search",
                                  data=json.dumps(query))
        data = result.json()
        if len(data["hits"]["hits"]) == 0:
            print("no more data -- try again later")
            quit(0)
        record = data["hits"]["hits"][0]["_source"]
        text = record["text"]

        ml_arr = calculateText(text)

        #img shit here
        #unitl its here, use this:

        ml_arr.append(sigmoid(9))

        #run through the ml
        threat = determineThreat(ml_arr)



        #check if name exists, if not add it
        if threat:
            addUserNameIfExists(record["username"], record["realname"])


