import json
from random import randint
 
def randomPhrases():
    phrases = open('morningPhrases.json')

    data = json.load(phrases)
    selectedPhrase = randint(0, len(data))
    print(selectedPhrase)

    for phrase in data:
        if phrase['id'] == selectedPhrase:
            return phrase['quote']

randomPhrases()