import requests
import json
import string
from main.processing.language_processing.dto import sentence_dto as dto
url = "http://localhost:9000/api/v1"

def init():
    r = requests.get(url + "/use/English")
    print(r.status_code)


def sendSentence(sentences):
    query = {
        "strings": sentences.split("."),
        "tree": False
    }

    print(query)

    r = requests.post(url + "/query", json=query)
    return r.json()

