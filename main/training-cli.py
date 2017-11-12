import requests
import json
print("you will be verifying mined data for threats")
print("y = threat")
print("n = not threat")
print("q = quit")


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

while True:
    query = {
        "from": 0,
        "size": 1,
        "query": {
            "term" : {
                "processed" : "false"
            }
        }
    }

    result = requests.request(method="get", url="http://104.196.181.214:9200/mine/pre/_search", data=json.dumps(query))
    data = result.json()
    if len(data["hits"]["hits"]) == 0:
        print("no more data -- try again later")
        quit(0)
    print(data["hits"]["hits"][0]["_source"])
    print()
    index = data["hits"]["hits"][0]["_id"]

    while True:
        res = input("what is this? y|n|q")
        if res is "y":
            answer(index, True, data)
            break
        elif res is "n":
            answer(index, False, data)
            break
        elif "res" is "q":
            quit(0)
        else:
            print("invalid input, try again")
    print("next...")
