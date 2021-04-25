def test1():
    names = ['Sasha', 'Bob', 'Vasya', 'Katia']

    # i = 0
    # for name in names:
    #     names[i] = name + '!'
    #     i += 1

    for i, name in enumerate(names):
        names[i] = name + '!'

    print(names)


def test2():
    letters = ['a', 'g', 'e', 'y', 'h', 'w']
    marks = [4, 1, 6, 3, 2, 3]

    for letter, mark in zip(letters, marks):
        print(letter, mark)


def test3():
    numbers = [5, 1, 7, 3, 7, 3, 6, 2]

    # new_numbers = []
    # for number in numbers:
    #     new_numbers.append(number * 2)

    new_numbers = [number * 2 for number in numbers]
    print(new_numbers)


def print_matrix(matrix):
    text = ''
    for row in matrix:
        row_text = '|'
        for el in row:
            row_text += str(el) + " "
        text += row_text[:-1] + "|\n"
    print(text)


def test4():
    print_matrix([['-' for j in range(14)] for i in range(10)])


def test5():
    numbers = [5, 1, 7, 3, 7, 3, 6, 2]

    if all([number % 2 == 1 for number in numbers]):
        print('Всі числа парні) Продовжеємо')
    else:
        print('Не всі числа парні. Спробуйте ще')


def test6():
    names = ['Bob', 'Alina', 'Katia', 'Lusi', 'Bobby']

    if any(['i' in name for name in names]):
        print('Ще є надія ')
    else:
        print('Надії немає ')


test6()
