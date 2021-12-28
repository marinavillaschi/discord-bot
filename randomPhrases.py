import json
from random import randint
 
def randomPhrases():
    phrases = open('morningPhrases.json', encoding = 'utf8')

    data = json.load(phrases)
    selectedPhrase = randint(0, len(data))

    for phrase in data:
        if phrase['id'] == selectedPhrase:
            return phrase['quote'] + '\n- ' + phrase['author']

randomPhrases()