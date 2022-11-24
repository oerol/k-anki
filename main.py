from modules.data import getLookUps
from modules.details import getDefinition, getTranslation
from modules.filter import getExistingWords, getCommonWords
import re
from time import sleep
cards = getLookUps()
print(f"{len(cards)} cards found!\n")

commonWords = getCommonWords()
existingWords = getExistingWords()
duplicateWords = []

commonCounter = 0
existingCounter = 0
newCounter = 0
duplicateCounter = 0

lines = []

for data in cards:
    word = data[0]
    usage = data[1]

    if word in existingWords:
        print("Existing word:", word)
        existingCounter += 1
        continue

    if word.lower() in commonWords:
        print("Common word:", word)
        commonCounter += 1
        continue

    if word in duplicateWords:
        print("Duplicated word:", word)
        duplicateCounter += 1
        continue

    definition = getDefinition(word)
    translation = getTranslation(word)

    if translation == word:  # should be moved to the method
        translation = ""

    newCounter += 1

    card = word + "\t" + definition + "\t" + \
        usage + "\t" + translation + "\n"

    duplicateWords.append(word)
    lines.append(card)

if __name__ == "__main__":
    with open("anki.txt", "a", encoding='utf8') as file:
        for line in lines:
            line = re.sub(u'[\u201c\u201d]', '"', line)
            line = re.sub(r"’", "'", line)
            file.write(line)

print("\n*** RESULTS:")
print("Common words:", commonCounter)
print("Existing words:", existingCounter)
print("Duplicated words:", duplicateCounter)
print("New words:", newCounter)
