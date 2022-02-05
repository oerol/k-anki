class CommonWords():
    common = []
    current = []

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
                
            return self.current


# commonWords = CommonWords().getCommonWords()
# print(CommonWords().getCurrentWords())


