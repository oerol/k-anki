import re

from modules.data import get_words
from modules.details import get_definition_for_word, get_translation_for_word
from modules.filter import getExistingWords, getCommonWords

look_ups = get_words()

commonWords = getCommonWords()
existingWords = getExistingWords()
duplicateWords = []

commonCounter = 0
existingCounter = 0
newCounter = 0
duplicateCounter = 0

lines = []

for data in look_ups:
    word = data[0]
    usage = data[1]

    if word in existingWords:
        print("[k-anki] Existing word:", word)
        existingCounter += 1
        continue

    if word.lower() in commonWords:
        print("[k-anki] Common word:", word)
        commonCounter += 1
        continue

    if word in duplicateWords:
        print("[k-anki] Duplicated word:", word)
        duplicateCounter += 1
        continue

    print(f"[k-anki] {word}")

    definition = get_definition_for_word(word)
    translation = get_translation_for_word(word)

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

print("\n[k-anki] Results:")
print("> Common words:", commonCounter)
print("> Existing words:", existingCounter)
print("> Duplicated words:", duplicateCounter)
print("> New words:", newCounter)
