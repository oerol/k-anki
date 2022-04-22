with open('output/vocab.txt', 'r', encoding='utf8') as file:
    originalLines = file.readlines()
    with open('output/new-vocab.txt', 'r+') as file2:
        newLines = file2.readlines()
        for line in newLines:
            if line not in originalLines:
                file2.write(line)
