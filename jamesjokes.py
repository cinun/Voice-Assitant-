##Create a file that tells a random joke

import requests, json


def joke():
    y = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke_dict = json.loads(y.text)
    joke = joke_dict['setup'] + " " + joke_dict['punchline']
    return joke

