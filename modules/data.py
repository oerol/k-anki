import sqlite3
import win32api
import os
from pathlib import Path


def getLookUps():
    con = 0
    drives = [chr(x) + ":" for x in range(65, 91)
              if os.path.exists(chr(x) + ":")]

    for drive in drives:
        if win32api.GetVolumeInformation(drive + "\\")[0] == "Kindle":
            vocabFile = Path(drive + "\\system\\vocabulary\\vocab.db")
            if vocabFile.is_file():
                print("Located vocab.db file!")
                con = sqlite3.connect(vocabFile)

    if con == 0:
        try:
            print("Using local vocab.db file!")
            con = sqlite3.connect("vocab.db")
        except:
            print("Couldn't find local vocab.db file..")

    c = con.cursor()

    table_list = [a for a in c.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table'")]
    bookKey = "The_Millionaire_Fastlane:38BFB202"
    bookKey = "The_Millionaire_Fastlane:38BFB202"

    bookList = c.execute(
        "SELECT book_key, COUNT(book_key) FROM LOOKUPS GROUP BY book_key HAVING COUNT(book_key) > 1 ORDER BY COUNT(book_key) desc")
    print("\nBooks:")
    bookKeys = []
    for x, row in enumerate(bookList):
        bookKeys.append(row[0])
        bookName = row[0].split(":")[0].replace("_", " ")
        print(f"{x + 1}. {bookName} with {row[1]} words")

    chosenIndex = int(input(
        "\nEnter the corresponding number left from the book: ")) - 1

    lookUps = c.execute(
        'SELECT * FROM LOOKUPS WHERE book_key=?', [bookKeys[chosenIndex]])

    cards = []

    for row in lookUps:
        word = row[1].split(":")[1]
        usage = row[5].replace(word, "<u>" + word + "</u>")
        cards.append((word, usage))
    con.close()
    return cards
