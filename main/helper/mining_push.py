import requests
import json
index_name = "mine"

def send(doc):
    res = requests.post(url="http://104.196.181.214:9200/" + index_name + "/pre/", data=json.dumps(doc))
    print(res.status_code)
    print(res.text)


doc = {
    "true": "seven",
    "87": "test"
}

send(doc)