import requests 


def getTranslation(word):
  result = requests.get( 
    "https://api-free.deepl.com/v2/translate", 
    params={ 
      "auth_key": "ca38b5b0-0c93-0b09-2e1c-2b10d4fd8742:fx", 
      "target_lang": "DE", 
      "text": word, 
    }, 
  )   
  translation = result.json()["translations"][0]["text"]
  return translation
print(getTranslation("word"))