import random
import time


name = 'Vasya'
money = 1000
things = ['шорти', "кепка"]
satiety = 10

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

print("Одного дня ви вивалилися з вікна. Добре, що живете на 2 поверсі.")
print("Ключів у вас немає. Тепер ви бомж.")
print("Тепер вам треба заробити на нову квартиру.")

while True:
    print("\n\n\n--= Головне меню =--")
    print("Ваші гроші: " + str(money) + " грн")
    print("Речі: " + str(things))
    print('1 - магазин')
    print('2 - заробітки')
    print('3 - битва за територію')
    print('4 - поритися на звалці')
    print('5 - вихід')

    choice = input("Ваш вибір: ")

    if choice == '1':
        while True:
            print("\n\n--= Магазин =--")
            print("Ваші гроші: " + str(money) + " грн")
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
                if money >= product[1]:
                    money -= product[1]
                    things.append(product[0])
                    print("Покупка успішна!")
                else:
                    print("Не вистачає грошей")
            else:
                print('Не то пальто')

    elif choice == '2':
        while True:
            print("\n\n--= Заробітки =--")
            print("Ваші гроші: " + str(money) + " грн")
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
                money += zarobitok
                print("Ви заробили " + str(zarobitok) + " грн")
                
            elif choice == '2':
                if 'тапки' in things:
                    input("Бомж таскає мішки... <Enter>")
                    input("Бомж тягає відра... <Enter>")
                    input("Бомж таскає ящики... <Enter>")
                    input("Бомж перетягує мішки в інше місце... <Enter>")
                    input("Бомж чистить речі начальнику... <Enter>")
                    zarobitok = 40
                    money += zarobitok
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
                            money += zarobitok
                            print("Ви заробили " + str(zarobitok) + 'грн!')
                        else:
                            print("Клієнт не зацікавився")
                    else:
                        print("Ви не привіталися! Клієнт зірвався")
                else:
                    print("Недостатньо речей")
                

    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        break
    else:
        pass
