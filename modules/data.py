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

    number_of_books = 0
    print("\nBooks:")
    for index, row in enumerate(books):
        number_of_books += 1

        book_keys.append(row[0])
        book_name = row[0].split(":")[0].replace("_", " ")
        print(f"{index + 1}. {book_name} with {row[1]} words")

    first_input_text = "\nEnter the corresponding number left from the book or leave blank to select all books: "
    subsequent_input_text = f"Please enter a number between 1 and {number_of_books} (or leave empty to select all books): "

    selected_book = -1
    while selected_book < 0 or selected_book > number_of_books - 1:
        if selected_book == -1:
            selected_book_input = input(first_input_text)
        else:
            selected_book_input = input(subsequent_input_text)

        if selected_book_input == "":
            return -1
        else:
            selected_book = int(selected_book_input) - 1

    return selected_book


def style_card(card):
    word = card[0]
    usage = card[1]

    usage = usage.replace(word, "<u>" + word + "</u>")
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
    if book_index == -1:
        kindle_look_ups = cursor.execute("SELECT * FROM LOOKUPS")
    else:
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
