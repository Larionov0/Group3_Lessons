students = {
    'A': [
        {
            'name': 'Bob',
            'surname': 'Bobenko',
            'date_of_birth': [10, 10, 2000],
            'hobbies': ['рибалка', "кемпінг", "футбол", "велосипед"],
            'marks': {
                'Python': 7,
                'math': 6,
                'English': 9
            },
            'city': 'Kyiv'
        },
        {
            'name': 'Alina',
            'surname': 'Rudenko',
            'date_of_birth': [1, 4, 1999],
            'hobbies': ['велосипед', "танці", "спів", "мовознаство", "їсти"],
            'marks': {
                'Python': 10,
                'math': 9,
                'English': 12
            },
            'city': 'Kyiv'
        },
        {
            'name': 'Alex',
            'surname': 'Didenko',
            'date_of_birth': [15, 9, 2000],
            'hobbies': ["футбол", "відеоігри", "шахи", "програмування", "їсти", "книги"],
            'marks': {
                'Python': 11,
                'math': 10,
                'English': 8
            },
            'city': 'Kharkiv'
        },
    ],
    'B': [
        {
            'name': 'Roman',
            'surname': 'Kholodenko',
            'date_of_birth': [2, 11, 1998],
            'hobbies': ['відеоігри', "рибалка", "спортивна ходьба", "гітара"],
            'marks': {
                'Python': 6,
                'math': 9,
                'English': 12
            },
            'city': 'Lublin'
        },
        {
            'name': 'Oksana',
            'surname': 'Oksenko',
            'date_of_birth': [28, 3, 1999],
            'hobbies': ["подоржі", "шахи", "танці", "виїздка"],
            'marks': {
                'Python': 6,
                'math': 11,
                'English': 12
            },
            'city': 'Kyiv'
        },
    ],
    "C": [
        {
            'name': 'Alan',
            'surname': 'Alenko',
            'date_of_birth': [5, 6, 2001],
            'hobbies': ['футбол', "баскетбол", "відеоігри", "гітара"],
            'marks': {
                'Python': 4,
                'math': 7,
                'English': 6
            },
            'city': 'Lviv'
        },
        {
            'name': 'Anna',
            'surname': 'Anko',
            'date_of_birth': [8, 11, 2000],
            'hobbies': ['шахи', "гітара", "спів", "подорожі", "шопінг", "книги", "їсти"],
            'marks': {
                'Python': 11,
                'math': 12,
                'English': 11
            },
            'city': 'Kharkiv'
        },
    ]
}

"""
Знайти хобі, яке зустрічається частіше за інші
(найпопулярніше хобі)
"""

hobbies_count = {}

for group_name in students:
    group = students[group_name]
    for student in group:
        for hobby in student['hobbies']:
            if hobby in hobbies_count:
                hobbies_count[hobby] += 1
            else:
                hobbies_count[hobby] = 1

max_count = max(hobbies_count.values())

for hobby in hobbies_count:
    if hobbies_count[hobby] == max_count:
        print(hobby)
