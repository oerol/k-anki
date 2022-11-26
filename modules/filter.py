import json
from pathlib import Path

common_words_file_path = "assets/common-words.txt"
existing_anki_output_path = "output/anki.json"


def get_common_words():
    common = []
    with open(common_words_file_path, 'r', encoding='utf-8') as file:
        page = file.readlines()
        for line in page:
            if '#' not in line:
                common.append(line.replace("\n", ""))
        return common


def get_existing_cards():
    if Path(existing_anki_output_path).is_file():
        with open(existing_anki_output_path) as json_file:
            words = json.load(json_file)
            return words
