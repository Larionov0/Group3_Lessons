SAVINGS_FILENAME = 'savings.csv'


def statistics(data):
    all_available_guests = 0
    all_real_guests = 0
    sum_square = 0
    all_items = {}
    sum_price = 0
    for room in data['комнаты']:
        all_available_guests += room['посетителей допустимо']
        all_real_guests += room['заселено']
        sum_square += (room['ширина'] * room['длинна'])
        sum_price += room['стоимость']

        for name_item in room['предметы']:
            amount_items = room['предметы'][name_item]
            if name_item in all_items:
                all_items[name_item] += amount_items
            else:
                all_items[name_item] = amount_items

    print(
        f'1) (общее количество допустимых гостей: {all_available_guests}, \n    общее количество реальных на текущий момент: {all_real_guests})')
    print(f'2) суммарнуя площадь всех номеров в отеле: {sum_square}')
    print('3) список всех предметов интерьера со всех комнат, и их количество:')

    for item in all_items:
        print(f'{item} - ({all_items[item]}) шт.')
    print(f'4) суммарная стоимость комнат: {sum_price}')


def hotel_arrangement():
    choice = input('Сделайте выбор: ')
    if choice == 1:

        room = {}
        i = 0
        while i < 7:
            param = input('Введите параметр комнаты: ')
            znach = input('Введите значение параметра:')
            room[param] = znach


def hotel_arrangement_menu(data):
    while True:
        text = '---= Обустройство отеля =---\n' \
               '0 - назад\n' \
               '1 - добавить комнату\n' \
               '2 - удалить комнату'
        print(text)

        choice = input('Ваш выбор: ')
        if choice == '0':
            return
        elif choice == '1':
            add_room_menu(data)
        elif choice == '2':
            pass


def add_room_menu(data):
    room = {}
    fields = ['номер', 'ширина', 'длинна', 'стоимость', 'посетителей допустимо', 'заселено']
    types = [int, float, float, float, int, int]
    for i in range(len(fields)):
        field = fields[i]
        converter = types[i]
        value = converter(input(f"{field}: "))
        room[field] = value

    room['предметы'] = {}
    while True:
        thing = input('Введіть річ (stop): ')
        if thing.lower() in ['stop', 'стоп']:
            break
        quantity = int(input('Введіть кількість: '))
        room['предметы'][thing] = quantity

    data['комнаты'].append(room)


def main_menu(data):
    while True:
        text = '----= Головне меню =----\n' \
               '1 - Обустройство отеля\n' \
               '2 - пошук кімнат\n' \
               '3 - \n' \
               '4 - статистика\n' \
               '5 - подивитися кімнати\n' \
               '6 - вийти'
        print(text)

        choice = input('Сделайте выбор: ')
        if choice == '1':
            hotel_arrangement_menu(data)
        elif choice == '2':
            search_rooms_menu(data)
        elif choice == '3':
            add_guests(data)
        elif choice == '4':
            statistics(data)
        elif choice == '5':
            show_rooms(data)
        elif choice == '6':
            exit()


def search_rooms_menu(data):
    square = 0
    visitors = 0
    max_price = float('inf')

    while True:
        text = f"---= Пошук кімнат =---\n" \
               f"Площа: {square}\n" \
               f"Відвідувачі: {visitors}\n" \
               f"Макс ціна: {max_price} грн\n" \
               f"Ваші дії:\n" \
               f"0 - назад\n" \
               f"1 - змінити площу\n" \
               f"2 - змінити відвідувачів\n" \
               f"3 - змінити макс ціну\n" \
               f"4 - шукати\n" \
               f"5 - зберегти"
        print(text)
        choice = input('Ваш вибір: ')
        if choice == '0':
            return
        elif choice == '1':
            square = int(input('Нова площа: '))
        elif choice == '2':
            visitors = int(input('Нова кількість відвідувачів: '))
        elif choice == '3':
            max_price = int(input('Нова макс ціна: '))
        elif choice == '4':
            search_rooms(data, square, visitors, max_price)
        elif choice == '5':
            print('Збереження')
            save_data(data)
        else:
            pass


def search_rooms(data, needed_square, needed_visitors, max_price):
    for room in data['комнаты']:
        square = room['ширина'] * room['длинна']
        if room['заселено'] == 0 and square >= needed_square and room['посетителей допустимо'] >= needed_visitors and \
                room['стоимость'] <= max_price:
            print('-' * 30)
            print(f'Кімната №{room["номер"]}\n'
                  f'Площа: {square}\n'
                  f'Стоимость: {room["стоимость"]}\n'
                  f'посетителей допустимо: {room["посетителей допустимо"]}')
            print('-' * 30)


def show_rooms(data):
    for room in data['комнаты']:
        print(room)


def create_init_data():
    data = {
        'комнаты': [
            {
                'номер': 4,
                'ширина': 4.5,
                'длинна': 6.3,
                'стоимость': 4000,
                'посетителей допустимо': 3,
                'заселено': 0,
                'предметы': {'шкаф B': 2, "телевизор ACA": 1, "стол дерево": 2, "стул пластик A": 5, 'кровать C': 1}
            },
            {
                'номер': 6,
                'ширина': 5.5,
                'длинна': 2.3,
                'стоимость': 3000,
                'посетителей допустимо': 1,
                'заселено': 1,
                'предметы': {'шкаф B': 1, "стол пластик": 1, "стул пластик A": 1, 'кровать D': 1}
            },
            {
                'номер': 7,
                'ширина': 15.5,
                'длинна': 4.2,
                'стоимость': 14000,
                'посетителей допустимо': 4,
                'заселено': 0,
                'предметы': {'шкаф B': 2, "стол пластик": 1, "стул пластик A": 11, 'кровать D': 1}
            },
            {
                'номер': 8,
                'ширина': 3.5,
                'длинна': 1.3,
                'стоимость': 1500,
                'посетителей допустимо': 1,
                'заселено': 0,
                'предметы': {'шкаф B': 1, "стул пластик A": 1, 'кровать D': 1}
            },
            {
                'номер': 9,
                'ширина': 10,
                'длинна': 5,
                'стоимость': 9000,
                'посетителей допустимо': 3,
                'заселено': 0,
                'предметы': {'шкаф B': 2, "стол пластик": 1, "стул пластик A": 11, 'кровать D': 3}
            },
        ]
    }
    return data


def add_guests(data):
    number_room_search = int(input('Введіть номер: '))
    count_guests_search = int(input('Введіть кількість гостей: '))
    result = False

    for room in data['комнаты']:
        if room['номер'] == number_room_search:
            if room['заселено'] == 0 and count_guests_search <= room['посетителей допустимо']:
                room['заселено'] = count_guests_search
                print('Done')
                result = True
            else:
                print('Номер зайнятий!')

    if not result:
        print(f"такий номер недоступний!")


def save_data(data):
    rooms = data['комнаты']
    headers = ['номер', 'ширина', 'длинна', 'стоимость', 'посетителей допустимо', 'заселено', 'предметы']
    with open(SAVINGS_FILENAME, 'wt', encoding='utf-8') as file:
        file.write(', '.join(headers) + '\n')
        for room in rooms:  # room = {}
            line = ''
            for key, value in room.items():
                line += f'{value}, '
            file.write(line[:-2] + '\n')


def load_data():
    pass


def main():
    data = create_init_data()
    main_menu(data)


main()
