import requests
import json


def getDefinition(word):
    print(word)
    request = requests.get(
        "https://dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=9af79d50-77cd-4a8a-8b2d-ed565d048f13")
    response = json.loads(request.text)
    try:
        definition = response[0]["shortdef"][0]
    except TypeError:
        definition = ""
        print("Skipped: ", word)
    return definition
