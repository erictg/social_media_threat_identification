import requests
import json
index_name = "mine"

def send(doc):
    res = requests.post(url="http://172.24.0.3:9201/" + index_name + "/pre/", data=json.dumps(doc))
    print(res.status_code)
    print(res.text)


