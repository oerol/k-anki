import requests
import json


def getDefinition(word):
    print(word)
    request = requests.get(
        "https://dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=9af79d50-77cd-4a8a-8b2d-ed565d048f13")
    response = json.loads(request.text)
    try:
        definition = response[0]["shortdef"][0]
    except (TypeError, IndexError) as e:
        definition = ""
        print("No Definition found for: ", word)
    return definition


def getTranslation(word):
    result = requests.get(
        "https://api-free.deepl.com/v2/translate",
        params={
            "auth_key": "ca38b5b0-0c93-0b09-2e1c-2b10d4fd8742:fx",
            "target_lang": "DE",
            "text": word,
        },
    )
    translation = result.json()["translations"][0]["text"]
    return translation
