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
Знайти середню оцінку всіх студентів по Пітону.
"""
sum_python_mark = 0
students_count = 0

for group_name in students:  # 'A'
    group = students[group_name]
    for student in group:
        python_mark = student['marks']['Python']
        sum_python_mark += python_mark
        students_count += 1

print(sum_python_mark / students_count)
