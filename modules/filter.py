from pathlib import Path

common_words_file_path = "assets/common-words.txt"


def getCommonWords():
    common = []
    with open(common_words_file_path, 'r', encoding='utf-8') as file:
        page = file.readlines()
        for line in page:
            if '#' not in line:
                common.append(line.replace("\n", ""))
        return common


def getExistingWords():
    existing = []
    existing_anki_output_path = "output/anki.txt"
    if Path(existing_anki_output_path).is_file():
        with open(existing_anki_output_path, 'r', encoding='utf-8') as file:
            page = file.readlines()
            for line in page:
                existing.append(line.split("\t")[0])
    return existing
