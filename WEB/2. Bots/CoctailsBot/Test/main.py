import requests
import json


def print_dict(dct):
    print(json.dumps(dct, indent=4, ensure_ascii=False))


response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=Smashed')
data = response.json()
print_dict(data)
