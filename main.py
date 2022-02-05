import shutil
from modules.database import Database
from modules.dictionary import Dictionary
from modules.translator import Translator
from modules.common import CommonWords
import re
from pathlib import Path

wordHelper = CommonWords()

commonWords = wordHelper.getCommonWords()
currentWords = wordHelper.getCurrentWords()

currentCards = wordHelper.all

database = Database()
cards = database.getData(wordHelper.getVocabFile())


dictionary = Dictionary()

translator = Translator()
print("Card Count:", len(cards))


lines = []
for data in cards:
    word = data[0]
    if word.lower() in commonWords:
        print("Common word:", word)
        continue

    usage = data[1]

    if usage in currentWords:
        print("Existing usage:", word)
        continue

    occurence = [card for card in currentCards if card[0] == word]

    if len(occurence) > 0:
        print("Existing word:", word)
        definition = occurence[0][1]
        translation = occurence[0][3]
    else:
        definition = dictionary.getDefinition(word)
        translation = translator.getTranslation(word)
    card = word + "\t" + definition + "\t" + \
        usage + "\t" + translation + "\t \n"

    lines.append(card)

Path("output").mkdir(parents=True, exist_ok=True)

with open('output/vocab.txt', 'w', encoding='utf8') as file:
    for line in lines:
        line = re.sub(u'[\u201c\u201d]', '"', line)
        line = re.sub(r"’", "'", line)
        file.write(line)

shutil.copy("output/vocab.txt", "anki.txt")
