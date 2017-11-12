import requests
import json
index_name = "mine/pre/"

def send(doc):
    res = requests.post(url="http://104.196.181.214:9200/" + index_name, data=json.dumps(doc))
    print(res.status_code)
    print(res.text)


doc = {
    "true": "seven",
    "87": "test",
    "processed": False
}

send(doc)

def sendWithIndex(doc, index):
    res = requests.post(url="http://104.196.181.214:9200/" + index, data=json.dumps(doc))
    print(res.status_code)
    print(res.text)