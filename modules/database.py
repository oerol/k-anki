import sqlite3


class Database():
    con = 0
    selectLookUps = []

    def connectToDatabase(self, vocabFile):
        if vocabFile != None:
            self.con = sqlite3.connect(vocabFile)
        else:
            try:
                print("Using local vocab.db file!")
                self.con = sqlite3.connect("vocab.db")
            except:
                print("Couldn't find local vocab.db file..")

        c = self.con.cursor()

        table_list = [a for a in c.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'")]
        bookKey = "Crime_and_Punishment:F16273CD"

        self.selectLookUps = c.execute(
            'SELECT * FROM LOOKUPS WHERE book_key=?', (bookKey,))

    def boldText(self, word):
        return "<b>" + word + "</b>"

    def getData(self, vocabFile):
        self.connectToDatabase(vocabFile)
        cards = []
        for row in self.selectLookUps:
            word = row[1].split(":")[1]
            usage = row[5].replace(word, self.boldText(word))
            cards.append((word, usage))
        self.con.close()
        return cards
