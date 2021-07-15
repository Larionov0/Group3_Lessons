import random
import time

SAVINGS_FILENAME = 'savings.txt'


def create_init_data():
    data = {
        'money': 1000,
        'satiety': 12,
        'name': 'Vasya'
    }
    things = ['шорти', "кепка"]

    store = [
        # [name, price]
        ['тапки', 50],
        ['телефон', 200],
        ['смартфон', 1000],
        ['спорт костюм', 400],
        ['годинник', 2000],
        ['лол', 123],
        ['квартира', 100000]
    ]
    return store, things, data


def main_menu(store, things, data):
    while True:
        print("\n\n\n--= Головне меню =--")
        print("Ваші гроші: " + str(data['money']) + " грн")
        print("Речі: " + str(things))
        print('1 - магазин')
        print('2 - заробітки')
        print('3 - битва за територію')
        print('4 - поритися на звалці')
        print('5 - вихід')
        print('6 - зберегти')

        choice = input("Ваш вибір: ")

        if choice == '1':
            store_menu(store, things, data)
        elif choice == '2':
            zarobitky_menu(things, data)
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            save_data(things, data)
            break
        elif choice == '6':
            save_data(things, data)


def store_menu(store, things, data):
    while True:
        print("\n\n--= Магазин =--")
        print("Ваші гроші: " + str(data['money']) + " грн")
        print("Речі: " + str(things))
        print('0 - назад')

        # виводимо всі товари з цінами і номерами
        number = 1
        for product in store:  # ['телефон', 200]
            print(number, '-', product[0], '(' + str(product[1]) + ' грн)')
            number += 1

        choice = int(input("Ваш вибір: "))
        if choice == 0:
            break

        index = choice - 1
        if 0 <= index < len(store):
            product = store[index]  # ['телефон', 200]
            if data['money'] >= product[1]:
                data['money'] -= product[1]
                things.append(product[0])
                print("Покупка успішна!")
            else:
                print("Не вистачає грошей")
        else:
            print('Не то пальто')


def zarobitky_menu(things, data):
    while True:
        print("\n\n--= Заробітки =--")
        print("Ваші гроші: " + str(data['money']) + " грн")
        print("Речі: " + str(things))
        print('0 - назад')
        print('1 - просити милостиню (5 - 25 грн)')
        print('2 - робота гружчиком (40 грн) (потрібні тапки)')
        print('3 - робота менеджером (100 грн) (потрібен телефон, будь-який костюм)')

        choice = input('Ваш вибір: ')
        if choice == '0':
            break
        elif choice == '1':
            print("Бомж заробляє...")
            time.sleep(4)
            zarobitok = random.randint(5, 25)
            data['money'] += zarobitok
            print("Ви заробили " + str(zarobitok) + " грн")

        elif choice == '2':
            if 'тапки' in things:
                input("Бомж таскає мішки... <Enter>")
                input("Бомж тягає відра... <Enter>")
                input("Бомж таскає ящики... <Enter>")
                input("Бомж перетягує мішки в інше місце... <Enter>")
                input("Бомж чистить речі начальнику... <Enter>")
                zarobitok = 40
                data['money'] += zarobitok
                print("Ви заробили " + str(zarobitok) + " грн")
            else:
                print("Недостатньо речей")

        elif choice == '3':
            if ('спорт костюм' in things or 'костюм' in things) and ('телефон' in things or 'смартфон' in things):
                print("Ви подзвонили клієнту. Привітайтеся.")
                text = input()
                if 'Доброго дня' in text or 'Привіт' in text or 'Добрий вечір' in text:
                    print('Порекомедуйте клієнту товар. Опишіть його.')
                    text = input()
                    if ('гарн' in text or 'чудов' in text or 'прекрасн' in text) and 'поган' not in text:
                        print("Клієнт вагається")
                        if random.randint(0, 1) == 1:
                            print("Клієнт купляє товар!")
                            zarobitok = 200
                        else:
                            print("Клієнт сказав, що зателефонує пізніше:)")
                            zarobitok = 30
                        data['money'] += zarobitok
                        print("Ви заробили " + str(zarobitok) + 'грн!')
                    else:
                        print("Клієнт не зацікавився")
                else:
                    print("Ви не привіталися! Клієнт зірвався")
            else:
                print("Недостатньо речей")


def save_data(things, data, filename=SAVINGS_FILENAME):
    file = open(filename, 'wt', encoding='utf-8')
    things_str = ', '.join(things)
    file.write(f'{data["name"]}\n{data["money"]}\n{things_str}')
    file.close()


def main():
    print("Одного дня ви вивалилися з вікна. Добре, що живете на 2 поверсі.")
    print("Ключів у вас немає. Тепер ви бомж.")
    print("Тепер вам треба заробити на нову квартиру.")
    store, things, data = create_init_data()
    main_menu(store, things, data)


main()
