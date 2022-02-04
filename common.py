class CommonWords():
    common = []

    def getCommonWords(self):
        with open('common.txt', 'r') as file:
            page = file.readlines()
            for line in page:
                if '#' not in line:
                    self.common.append(line.replace("\n", ""))
            return self.common

# commonWords = CommonWords().getCommonWords()


