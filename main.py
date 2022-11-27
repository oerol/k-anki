import json
from modules.data import get_words
from modules.details import get_definition_for_word, get_translation_for_word
from modules.filter import get_existing_cards, get_common_words
from modules.generate import generate_apkg


def write_copy_to_json(cards):
    cards_json = {}
    for card in cards:
        word = card
        definition = cards[card]["definition"]
        usage = cards[card]["usage"]
        translation = cards[card]["translation"]

        cards_json[word] = {"definition": definition, "usage": usage, "translation": translation}

    with open('output/anki.json', 'w', encoding='utf-8') as f:
        json.dump(cards_json, f, indent=4)


if __name__ == "__main__":
    print("[k-anki] Starting Program!")

    look_ups = get_words()

    common_words = get_common_words()
    existing_cards = get_existing_cards()
    if existing_cards != None:
        existing_words = existing_cards.keys()
    else:
        existing_cards = {}
        existing_words = []
    duplicate_words = []

    common_counter = 0
    existing_counter = 0
    new_counter = 0
    duplicate_counter = 0

    lines = {}

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

        duplicate_words.append(word)
        lines[word] = {"definition": definition, "usage": usage, "translation": translation}

    print("\n[k-anki] Results:")
    print("> Common words:", common_counter)
    print("> Existing words:", existing_counter)
    print("> Duplicated words:", duplicate_counter)
    print("> New words:", new_counter)

    print("\n[k-anki] Writing cache file to output/anki.json.")
    write_copy_to_json(existing_cards | lines)
    print("[k-anki] Writing output file to output.apkg.")
    generate_apkg(existing_cards | lines)
    print("[k-anki] Done!")
