import requests
from main.processing.language_processing.dto import sentence_dto as dto
url = "http://localhost:9000/api/v1"

def init():
    r = requests.get(url + "/use/English")
    print(r.status_code)

def sendSentence(sentence):
    r = requests.post(url + "/query", data=dto.createDto(sentence))
    print(r.status_code)
    print(r.json())

init()
sendSentence("fuck this shit")