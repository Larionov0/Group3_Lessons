animal1 = ['курка', 'Ряба', 3, [1, 5], 'k']

animal2 = {
    'type': 'курка',
    'name': 'Ряба',
    'hp': 3,
    'coords': [1, 5],
    'face': 'k'
}

test_dict = {
    'lol': 2,
    'kek': [1, 2, 3, 4],
    10: 'poop',
    True: ['1', '2', []],
    'dict': {
        '1': '2',
        'wow': False,
        'list': [1, 2, 3, 4, 5]
    }
}

st = input()
print(test_dict[st])

