import re

from modules.data import get_words
from modules.details import get_definition_for_word, get_translation_for_word
from modules.filter import get_existing_words, get_common_words
from modules.generate import generate_apkg


if __name__ == "__main__":
    print("[k-anki] Starting Program!")

    look_ups = get_words()

    common_words = get_common_words()
    existing_words = get_existing_words()
    duplicate_words = []

    common_counter = 0
    existing_counter = 0
    new_counter = 0
    duplicate_counter = 0

    lines = []

    for data in look_ups:
        word = data[0]
        usage = data[1]

        if word in existing_words:
            print("[k-anki] Existing word:", word)
            existing_counter += 1
            continue

        if word.lower() in common_words:
            print("[k-anki] Common word:", word)
            common_counter += 1
            continue

        if word in duplicate_words:
            print("[k-anki] Duplicated word:", word)
            duplicate_counter += 1
            continue

        print(f"[k-anki] {word}")

        definition = get_definition_for_word(word)
        translation = get_translation_for_word(word)

        if translation == word:  # should be moved to the method
            translation = ""

        new_counter += 1

        card = [word, definition, usage, translation]

        duplicate_words.append(word)
        lines.append(card)
        generate_apkg(lines)

print("\n[k-anki] Results:")
print("> Common words:", common_counter)
print("> Existing words:", existing_counter)
print("> Duplicated words:", duplicate_counter)
print("> New words:", new_counter)
