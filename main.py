import requests

s = requests.session()
baptiste = 22
age_retraite = 62


def getAge(name):
    url = "https://api.agify.io?name=" + name
    r = s.get(url).json()
    age_api = r.get("age")
    return age_api


def diff(real_age):
    nom = "baptiste"
    diff_age = getAge(nom) - real_age
    return diff_age if diff_age > 0 else diff_age * -1

print(diff(baptiste))