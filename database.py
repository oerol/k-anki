import sqlite3


con = sqlite3.connect("vocab.db")
c = con.cursor()
table_list = [a for a in c.execute(
    "SELECT name FROM sqlite_master WHERE type = 'table'")]
print(table_list)
bookKey = "Crime_and_Punishment:F16273CD"
selectLookUps = c.execute('SELECT * FROM LOOKUPS WHERE book_key=?', (bookKey,))


def boldText(word):
    return "<b>" + word + "</b>"


cards = []
for row in selectLookUps:
    word = row[1].split(":")[1]
    usage = row[5].replace(word, boldText(word))
    cards.append((word, usage))
    print(cards)

con.close()
