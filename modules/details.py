import requests
import json


settings_file_path = "settings.json"
merriam_webster_api_key = ""
deepl_api_key = ""
with open(settings_file_path) as json_file:
    settings = json.load(json_file)
    merriam_webster_api_key = settings["merriam-webster-api-key"]
    deepl_api_key = settings["deepl-api-key"]


def getDefinition(word):
    print(word)
    request = requests.get(
        f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={merriam_webster_api_key}")
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
            "auth_key": deepl_api_key,
            "target_lang": "DE",
            "text": word,
        },
    )
    translation = result.json()["translations"][0]["text"]
    return translation
