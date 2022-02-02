import sqlite3


class Database():
    con = 0
    selectLookUps = []

    def connectToDatabase(self):
        self.con = sqlite3.connect("vocab2.db")
        c = self.con.cursor()

        table_list = [a for a in c.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'")]
        bookKey = "Crime_and_Punishment:F16273CD"

        self.selectLookUps = c.execute(
            'SELECT * FROM LOOKUPS WHERE book_key=?', (bookKey,))

    def boldText(self, word):
        return "<b>" + word + "</b>"

    def getData(self):
        self.connectToDatabase()
        cards = []
        for row in self.selectLookUps:
            word = row[1].split(":")[1]
            usage = row[5].replace(word, self.boldText(word))
            cards.append((word, usage))
        self.con.close()
        return cards
