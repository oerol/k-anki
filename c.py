filepath = "anki.txt"
with open(filepath) as fp:
    lines = fp.read().splitlines()
with open("anki-new.txt", "w") as fp:
    for line in lines:
        print(line + "\t", file=fp)
