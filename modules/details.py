import requests
import json


settings_file_path = "settings.json"
merriam_webster_api_key = ""
deepl_api_key = ""

with open(settings_file_path) as json_file:
    settings = json.load(json_file)
    merriam_webster_api_key = settings["merriam-webster-api-key"]
    deepl_api_key = settings["deepl-api-key"]


def get_definition_for_word(word):
    if merriam_webster_api_key == "":
        return ""

    request = requests.get(
        f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={merriam_webster_api_key}")

    response = json.loads(request.text)

    try:
        definition = response[0]["shortdef"][0]
    except (TypeError, IndexError) as e:
        definition = ""
        print(f"[k-anki] No definition found for: {word}")

    return definition


def get_translation_for_word(word):
    if deepl_api_key == "":
        return ""

    request = requests.get(
        "https://api-free.deepl.com/v2/translate",
        params={
            "auth_key": deepl_api_key,
            "target_lang": "DE",
            "text": word,
        },
    )
    translation = request.json()["translations"][0]["text"]

    if translation == "":
        print(f"[k-anki] No translation found for: {word}")

    return translation
