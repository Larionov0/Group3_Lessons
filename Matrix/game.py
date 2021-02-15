from os import system
import random


N = 14
M = 16


hero_name = 'Bob'
hero_coords = [2, 4]
hero_face = '+'
hero_details = 0

animals = [
   #[type, name, hp, coords, face]
    ['курка', 'Ряба', 3, [5, 5], 'k'],
    ['курка', 'Біба', 3, [6, 6], 'k'],
    ['курка', 'Боба', 3, [4, 5], 'k'],
    ]


round = 1
while True:
    # створення матриці
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

    # малюємо об'єкти
    # малюємо героя
    matrix[hero_coords[0]][hero_coords[1]] = hero_face
    # малюємо тварин
    for animal in animals:
        animal_coords = animal[3]
        animal_face = animal[4]
        matrix[animal_coords[0]][animal_coords[1]] = animal_face

    system('cls')
    # виведення матриці
    for row in matrix:
        row_text = '|'
        for el in row:
            row_text += str(el) + " "
        print(row_text[:-1] + "|")

    # хід гравця
    print("Герой", hero_name)
    print("Деталі:", hero_details)
    direction = input('WASD: ')
    if direction == 'w':
        if hero_coords[0] != 0:
            hero_coords[0] -= 1
    elif direction == 'a':
        if hero_coords[1] == 0:
            hero_coords[1] = M - 1
        else:
            hero_coords[1] -= 1
    elif direction == 's':
        if hero_coords[0] != N - 1:
            hero_coords[0] += 1
    elif direction == 'd':
        if hero_coords[1] == M - 1:
            hero_coords[1] = 0
        else:
            hero_coords[1] += 1

    # Перевіряємо, чи не спіймав курку
    catched_animals = []
    for animal in animals:
        if animal[0] == 'курка':
            if hero_coords == animal[3]:
                catched_animals.append(animal)

    for animal in catched_animals:
        animals.remove(animal)
        hero_details += 3

    # хід тварин
    for animal in animals:
        if animal[0] == 'курка':
            kurka_coords = animal[3]
            direction = random.choice(['w', 'a', 's', 'd'])
            if direction == 'w':
                if kurka_coords[0] != 0:
                    kurka_coords[0] -= 1
            elif direction == 'a':
                if kurka_coords[1] == 0:
                    kurka_coords[1] = M - 1
                else:
                    kurka_coords[1] -= 1
            elif direction == 's':
                if kurka_coords[0] != N - 1:
                    kurka_coords[0] += 1
            elif direction == 'd':
                if kurka_coords[1] == M - 1:
                    kurka_coords[1] = 0
                else:
                    kurka_coords[1] += 1

    # Перевіряємо, чи не спіймав курку
    catched_animals = []
    for animal in animals:
        if animal[0] == 'курка':
            if hero_coords == animal[3]:
                catched_animals.append(animal)

    for animal in catched_animals:
        animals.remove(animal)
        hero_details += 3

    # поява нових тварин
    if round % 20 == 0:
        animals.append(
                ['курка', random.choice(['Олена', "Маруся", "Льоша", "Вася"]), 3, [random.randint(0, N-1), random.randint(0, M-1)], 'k']
            )

    round += 1
