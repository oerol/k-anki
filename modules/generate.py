import genanki

card_style = """.card {
    font-family: "Charter BT";
    font-size: 20px;

    color: black;
    background-color: white;
}

#translation {
 font-size: 5px;
}
"""


def generate_apkg(cards):
    anki_model = genanki.Model(1607392318, 'k-anki',
                               fields=[
                                   {'name': 'Word'},
                                   {'name': 'Definition'},
                                   {'name': 'Usage'},
                                   {'name': 'Translation'},
                               ],
                               templates=[
                                   {
                                       'name': 'Card 1',
                                       'qfmt': '{{Word}}',
                                       'afmt': '{{FrontSide}}<hr id="answer">{{Usage}}<br/><br/><i>{{Definition}}</i><br/><br/><div id="translation">{{Translation}}</div>',
                                   },
                               ], css=card_style)

    anki_deck = genanki.Deck(
        2059400111,
        'k-anki')  # Deck name

    for card in cards:
        anki_note = genanki.Note(model=anki_model, fields=card)
        anki_deck.add_note(anki_note)

    genanki.Package(anki_deck).write_to_file('output.apkg')
