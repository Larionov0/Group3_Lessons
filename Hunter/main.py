from os import system
import random

N = 14
M = 16


def clear():
    system('cls')


def create_field():
    matrix = []
    i = 0
    while i < N:
        row = []
        j = 0
        while j < M:
            row.append('-')
            j += 1
        matrix.append(row)
        i += 1
    return matrix


def print_field(field):
    text = ''
    for row in field:
        row_text = '|'
        for el in row:
            row_text += str(el) + " "
        text += row_text[:-1] + "|\n"
    print(text)


def draw_game_object(field, game_object):
    """
    Puts object`s face into matrix.2
    :param field: matrix
    :param game_object: some dict with 'coords' and 'face' keys
    """
    coords = game_object['coords']
    field[coords[0]][coords[1]] = game_object['face']


def draw_animals(field, animals):
    for animal in animals:
        draw_game_object(field, animal)


def create_data():
    hero = {
        'name': 'Alex',
        'hp': 10,
        'coords': [1, 2],
        'face': '+',
        'details': 0
    }

    animals = [
        {
            'type': 'курка',
            'name': 'Ryaba',
            'hp': 3,
            'coords': [5, 5],
            'face': 'k'
        },
        {
            'type': 'курка',
            'name': 'Biba',
            'hp': 3,
            'coords': [5, 6],
            'face': 'k'
        },
        {
            'type': 'курка',
            'name': 'Boba',
            'hp': 3,
            'coords': [6, 5],
            'face': 'k'
        },
    ]
    return hero, animals


def game_object_moves(game_object, direction):
    """
    Рухає ігровий об'єкт (гравця, тварину, інше)
    :param game_object: dict with 'coords' key
    """
    if direction == 'w':
        if game_object['coords'][0] != 0:
            game_object['coords'][0] -= 1
    elif direction == 'a':
        if game_object['coords'][1] == 0:
            game_object['coords'][1] = M - 1
        else:
            game_object['coords'][1] -= 1
    elif direction == 's':
        if game_object['coords'][0] != N - 1:
            game_object['coords'][0] += 1
    elif direction == 'd':
        if game_object['coords'][1] == M - 1:
            game_object['coords'][1] = 0
        else:
            game_object['coords'][1] += 1


def player_moves(hero):
    print("Герой", hero['name'])
    print("Деталі:", hero['details'])
    print('WASD - ходити')
    direction = input('Ваш вибір: ').lower()
    game_object_moves(hero, direction)


def kurka_makes_move(kurka):
    direction = random.choice(['w', 'a', 's', 'd'])
    game_object_moves(kurka, direction)


def animal_makes_move(animal):
    if animal['type'] == 'курка':
        kurka_makes_move(animal)
    elif animal['type'] == 'олень':
        pass


def animals_moves(animals):
    for animal in animals:
        animal_makes_move(animal)


def check_if_player_catches_kurka(animals, hero):
    # Перевіряємо, чи не спіймав курку
    catched_animals = []
    for animal in animals:
        if animal['type'] == 'курка':
            if hero['coords'] == animal['coords']:
                catched_animals.append(animal)

    for animal in catched_animals:
        animals.remove(animal)
        hero['details'] += 3


def main():
    hero, animals = create_data()
    round = 1
    while True:
        field = create_field()
        draw_game_object(field, hero)
        draw_animals(field, animals)
        clear()
        print_field(field)

        player_moves(hero)
        check_if_player_catches_kurka(animals, hero)
        animals_moves(animals)
        check_if_player_catches_kurka(animals, hero)

        round += 1


main()
