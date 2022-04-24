
from pathlib import Path


def getCommonWords():
    common = []
    with open('common.txt', 'r', encoding='utf-8') as file:
        page = file.readlines()
        for line in page:
            if '#' not in line:
                common.append(line.replace("\n", ""))
        return common


def getExistingWords():
    existing = []
    if Path("./anki.txt").is_file():
        with open('anki.txt', 'r', encoding='utf-8') as file:
            page = file.readlines()
            for line in page:
                existing.append(line.split("\t")[0])
    return existing
