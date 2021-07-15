import json


books = [
    {
        'name': 'The the of the',
        'author': 'Theko',
        'sections': ['the', 'The'],
        'price': 1000,
        'availability': True
    },
    {
        'name': 'Light',
        'author': 'Bobby',
        'sections': ['the light', 'the darkness'],
        'price': 450,
        'availability': False
    },
]

string = json.dumps(books)
new_books = json.loads(string)
print(new_books == books)
