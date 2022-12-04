<div align="center">

# k-anki: Import your Kindle flashcards to Anki
![image](https://user-images.githubusercontent.com/74826613/204369691-743b245a-20b7-4aa9-a9f4-713d72c90cfe.png)
</div>




## Prerequisites

- Python (3.9.6)
- genanki: `pip install genanki`

## Installation

If you have git installed, clone the repository with `git clone https://github.com/oerol/k-anki.git` and if you don't, click [here](https://github.com/oerol/k-anki/archive/refs/heads/main.zip).

## Usage

To get started, either connect your Kindle to your PC or place a `vocab.db` file in the `k-anki` directory. Next, start the program by running:

```
python main.py
```

The program will then guide you to the process. If you don't define any API keys, the program will skip the translation/definition fields.

The program then produces an `output.apkg` file that you can import into Anki!

## Translation and Definition Feature

To add a translation or a definition to your vocab list, you would have to acquire an API key from [Merriam-Webster](https://dictionaryapi.com/register/index) and [DeepL](https://www.deepl.com/pro-api?cta=header-pro-api/) (both include free versions!). Please mind that DeepL requires you to add a credit card for authentification.

This step might seem daunting at first, but it shouldn't take you more than 10 minutes.

After you're done, make sure to copy your API key from [Merriam-Webster](https://dictionaryapi.com/account/my-keys) and [DeepL](https://www.deepl.com/account/summary) and paste them to the corresponding fields in the `settings.json` file.

## Features

- Detecs connected Kindle devices automatically
- Filters out common words that you may have added to your flashcards like "the" or "and"
- Includes the passage of the book where the flashcard was first recorded
- Supports adding translation and definitions to words
- Can be configured to run with a single command
