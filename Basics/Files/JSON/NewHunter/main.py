from os import system
import random
import json

N = 14
M = 16
SAVINGS_FILENAME = 'savings.json'


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


def player_moves(hero, animals):
    print("Герой", hero['name'])
    print("Деталі:", hero['details'])
    print('Боєприпаси: ', hero['ammo'])
    print('WASD - ходити')
    print('x - вистріл')
    print('q - зберігти')
    choice = input('Ваш вибір: ').lower()
    if choice in ['w', 'a', 's', 'd']:
        game_object_moves(hero, choice)
    elif choice == 'x':
        player_shoots(hero, animals)
    elif choice == 'q':
        save_data(hero, animals)
        input('Успішно збережено!')


def player_shoots(hero, animals):
    weapon_type = hero['main_weapon']['type']
    if weapon_type == 'bow':
        bow_shoots(hero, animals)
    elif weapon_type == 'slingshot':
        pass


def bow_shoots(hero, animals):
    direction = input('Виберіть напрям пострілу: ')
    if direction in ['w', 'a', 's', 'd']:
        arrow = {
            'type': 'arrow',
            'energy': hero['main_weapon']['range'],
            'coords': hero['coords'].copy(),
            'direction': direction,
            'face': 'x',
            'damage': hero['main_weapon']['damage']
        }
        arrow_fly(arrow, animals, hero)


def arrow_fly(arrow, animals, hero):
    while True:
        game_object_moves(arrow, arrow['direction'])

        for animal in animals:
            if arrow['coords'] == animal['coords']:
                animal_loose_hp(animals, animal, arrow['damage'], hero)
                return

        if arrow['energy'] == 0:
            return

        arrow['energy'] -= 1


def animal_loose_hp(animals, animal, damage, hero):
    animal['hp'] -= damage
    if animal['hp'] <= 0:
        animals.remove(animal)
        if animal['type'] == 'курка':
            hero['details'] += 3


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


def spawn_kurka(animals):
    kurka = {
        'type': 'курка',
        'name': random.choice(['Ryaba', 'Koko', 'Kekkek', 'Petya', 'Alice', 'Katia']),
        'hp': 3,
        'coords': [random.randint(0, N - 1), random.randint(0, M - 1)],
        'face': 'k'
    }
    animals.append(kurka)


def animals_respawn(animals, round_):
    if round_ % 15 == 0:
        spawn_kurka(animals)
    if round_ % 30 == 0:
        pass


def create_data():
    hero = {
        'name': 'Alex',
        'hp': 10,
        'coords': [1, 2],
        'face': '+',
        'details': 0,
        'ammo': {
            'arrow': 10,
            'rock': 10
        },
        'main_weapon': {
            'type': 'bow',
            'range': 4,
            'damage': 3,
            'price': 10
        }
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


def save_data(hero, animals):
    data = {'hero': hero, 'animals': animals}
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open(SAVINGS_FILENAME, 'wt', encoding='utf-8') as file:
        file.write(json_data)


def load_data():
    with open(SAVINGS_FILENAME, 'rt', encoding='utf-8') as file:
        json_data = file.read()
    data = json.loads(json_data)
    return data['hero'], data['animals']


def try_to_load_data():
    try:
        hero, animals = load_data()
        print('Дані загружено успішено!')
    except Exception as error:
        print(f'Під час відкриття файлу сталася помилка:\n{error}')
        hero, animals = create_data()
    input()
    return hero, animals


def main():
    hero, animals = try_to_load_data()
    round_ = 1
    while True:
        field = create_field()
        draw_game_object(field, hero)
        draw_animals(field, animals)
        clear()
        print_field(field)

        player_moves(hero, animals)
        check_if_player_catches_kurka(animals, hero)
        animals_moves(animals)
        check_if_player_catches_kurka(animals, hero)

        animals_respawn(animals, round_)

        round_ += 1


main()
