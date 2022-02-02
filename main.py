from database import Database
from dictionary import Dictionary
from translator import Translator
import re
database = Database()
cards = database.getData()

dictionary = Dictionary()

translator = Translator()
print("Card Count:", len(cards))

lines = []
for data in cards:
    word = data[0]
    usage = data[1]
    definition = dictionary.getDefinition(word)
    translation = translator.getTranslation(word)
    card = word + "\t" + definition + "\t" + \
        usage + "\t" + translation + "\t \n"
    lines.append(card)

with open('vocab2.txt', 'w', encoding='utf8') as file:
    for line in lines:
        line = re.sub(u'[\u201c\u201d]', '"', line)
        line = re.sub(r"’", "'", line)
        file.write(line)
