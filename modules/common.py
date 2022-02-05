import win32api
import os
from pathlib import Path


class CommonWords():
    common = []
    current = []

    all = []

    def getCommonWords(self):
        with open('common.txt', 'r') as file:
            page = file.readlines()
            for line in page:
                if '#' not in line:
                    self.common.append(line.replace("\n", ""))
            return self.common

    def getCurrentWords(self):
        with open('anki.txt', 'r') as file:
            page = file.readlines()
            for line in page:
                self.current.append(line.split("\t")[2])
                self.all.append(line.split("\t"))

            return self.current


# commonWords = CommonWords().getCommonWords()
# print(CommonWords().getCurrentWords())


    def getVocabFile(self):
        drives = [chr(x) + ":" for x in range(65, 91)
                  if os.path.exists(chr(x) + ":")]
        for drive in drives:
            if win32api.GetVolumeInformation(drive + "\\")[0] == "Kindle":
                vocabFile = Path(drive + "\\system\\vocabulary\\vocab.db")
                if vocabFile.is_file():
                    print("Located vocab.db file!")
                    return vocabFile
                else:
                    print("Couldn't find the vocab.db file..")
                    return None
