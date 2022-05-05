import requests

s = requests.session()

def getAge(name):
    url = "https://api.agify.io?name=" + name
    r = s.get(url).json()
    print(r.get("age"))

getAge("toto")
