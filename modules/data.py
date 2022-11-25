import sqlite3
import win32api
import os
from pathlib import Path
import sys

kindle_drive = ""


def kindle_is_connected():
    global kindle_drive
    drives = [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]

    for drive in drives:
        if win32api.GetVolumeInformation(drive + "\\")[0] == "Kindle":
            print("[k-anki] Kindle is connected!")

            kindle_drive = drive
            return True
    return False


kindle_vocab_file_path = ""


def kindle_has_vocab_file():
    kindle_vocab_file_path = kindle_drive + "\\system\\vocabulary\\vocab.db"
    vocabFile = Path(kindle_vocab_file_path)

    if vocabFile.is_file():
        print(f"[k-anki] Located vocab.db file in {kindle_vocab_file_path}")
        return True

    print(f"[k-anki] Coudln't find the Kindle vocab.db file in {kindle_vocab_file_path}")
    return False


local_vocab_file_path = "vocab.db"


def has_local_vocab_file():
    print("[k-anki] Kindle is not connected. Trying again with local vocab.db file..")

    vocabFile = Path(local_vocab_file_path)

    if vocabFile.is_file():
        print("[k-anki] Using the local vocab.db file!")
        return True

    print("[k-anki] Couldn't find a local vocab.db file! Exiting the program..")
    return False


book_keys = []


def selected_book_index(cursor):
    books = cursor.execute(
        "SELECT book_key, COUNT(book_key) FROM LOOKUPS GROUP BY book_key HAVING COUNT(book_key) > 1 ORDER BY COUNT(book_key) desc")

    print("\nBooks:")
    for x, row in enumerate(books):
        book_keys.append(row[0])
        book_name = row[0].split(":")[0].replace("_", " ")
        print(f"{x + 1}. {book_name} with {row[1]} words")

    selected_book = (
        int(input("\nEnter the corresponding number left from the book: ")) - 1
    )

    return selected_book


def style_card(card):
    word = card[0]
    usage = card[1]

    usage.replace(word, "<u>" + word + "</u>")
    return (word, usage)


def get_words():
    if kindle_is_connected() and kindle_has_vocab_file():
        con = sqlite3.connect(kindle_vocab_file_path)
    else:
        if has_local_vocab_file():
            con = sqlite3.connect(local_vocab_file_path)
        else:
            sys.exit()

    cursor = con.cursor()

    book_index = selected_book_index(cursor)
    kindle_look_ups = cursor.execute("SELECT * FROM LOOKUPS WHERE book_key=?", [book_keys[book_index]])

    cards = []
    for row in kindle_look_ups:
        word = row[1].split(":")[1]
        usage = row[5]

        card = (word, usage)
        card = style_card(card)

        cards.append(card)
    con.close()

    print(f"\n[k-anki] {len(cards)} words found!")
    return cards
