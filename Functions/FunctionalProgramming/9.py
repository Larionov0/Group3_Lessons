animals = [
    {
        'type': 'kurka',
        'name': 'Ryaba',
        'coords': [1, 4]
    },
    {
        'type': 'kurka',
        'name': 'Biba',
        'coords': [8, 7]
    },
    {
        'type': 'kurka',
        'name': 'Boba',
        'coords': [2, 7]
    },
    {
        'type': 'kurka',
        'name': 'Kryakva',
        'coords': [9, 2]
    },
]


down_animals = filter(lambda animal: animal['coords'][0] > animal['coords'][1], animals)
print(list(down_animals))
