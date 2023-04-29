import requests
import json

def get_dog():
    dog = requests.get("https://random.dog/woof.json")

    return json.loads(dog.content)['url']
