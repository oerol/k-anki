import unicodedata
print(unicodedata.normalize(
    'NFKD', "\u02ccte-st\u0259-\u02c8bi-l\u0259-t\u0113").encode('ascii', 'ignore'))
