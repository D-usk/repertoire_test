import requests

s = requests.session()
baptiste = 22
age_retraite = 62


def getage(name):
    url = "https://api.agify.io?name=" + name
    r = s.get(url).json()
    age_api = r.get("age")
    return age_api


def diff(real_age):
    nom = "baptiste"
    diff_age = getage(nom) - real_age
    return diff_age if diff_age > 0 else diff_age * -1


def retraite(real_age):
    jours_av_retraite = (age_retraite - real_age) * 365
    return jours_av_retraite


print(diff(baptiste), "ans de différence entre age API et age réel")
print("Nombre de jours avant la retraite :", retraite(baptiste))
