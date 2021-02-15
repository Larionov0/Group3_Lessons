menu = [
#   [назва, ціна, куплено, розділ, [інгрідієнти...]]
    ['борщ', 50, 12, 'перше', ['вода', "буряк", "картопля", "квасоля"]],
    ['уха', 60, 2, 'перше', ['вода', "риба", "картопля", "морква"]],
    ['вареники з грибами', 40, 30, 'друге', ['тісто', "гриби"]],
    ['вареники з картоплею', 40, 25, 'друге', ['тісто', "картопля"]],
    ['стейк з тунця', 150, 15, 'друге', ['риба', "морква", "білий соус"]],
    ['овочевий сік', 40, 8, 'третє', ['морква', "банан", "буряк"]]
    ]


while True:
    print("--= Шеф-кухар меню =--")
    print('1 - додати нову страву')
    print('2 - продивитися всі страви')
    print('3 - видалити страву за назвою')
    print('4 - змінити страву')
    print('5 - знайти всі страви за інгрідієнтом')
    print('6 - страву куплено')
    print('7')
    print('0 - вихід з програми')

    choice = input('Ваш вибір: ')
    
    if choice == '1':
        # вводимо назву страви
        while True:
            name = input('Введіть назву страви: ')
            if 4 <= len(name) <= 40:
                break
            else:
                print('Довжина не підходить!')

        # вводимо ціну
        while True:
            price = input('Ціна: ')
            if price.isdigit():
                price = int(price)
                if price <= 0:
                    print('Число не підходить!')
                else:
                    break
            else:
                print('Це не число!')

        # вводимо кількість
        while True:
            count = input('Куплено: ')
            if count.isdigit():
                count = int(count)
                if count <= 0:
                    print('Число не підходить!')
                else:
                    break
            else:
                print('Це не число!')

        # вводимо розділ
        while True:
            section = input('Введіть розділ: ')

            if 4 <= len(section) <= 20:
                break
            else:
                print('Не підходяща кількість символів!')
        

        # вводимо інгрідієнти
        ingredients = []
        while True:
            ingredient = input('Інгрідієнт: ')
            
            if ingredient == 'stop' or ingredient == 'стоп':
                break

            if 3 <= len(ingredient) <= 30:
                ingredients.append(ingredient)
            else:
                print('Не підходяща кількість символів')

        dish = [name, price, count, section, ingredients]
        menu.append(dish)
    
    elif choice == '2':
        for dish in menu:  # ['вареники з грибами', 40, 30, 'друге', ['тісто', "гриби"]]
            print('-' * 30)
            print('Назва:', dish[0])
            print('Ціна:', dish[1])
            print('Куплено: ', dish[2])
            print('Розділ:', dish[3])
            print('Інгрідієнти:')
            for ingredient in dish[4]:
                print('-', ingredient)
        print('-' * 30)
        
    elif choice == '3':
        name = input('Введіть назву: ')
        result = False
        
        i = 0
        for dish in menu:  # ['вареники з грибами', 40, 30, 'друге', ['тісто', "гриби"]]
            if dish[0] == name:
                result = True
                menu.pop(i)
                print('Видалено успішно')
                break
            i += 1
        
        if not result:  # if result == False
            print('Такої страви немає')
    
    elif choice == '4':
        # зміни
        print('--= Внесення змін =--')
        number = 1
        for dish in menu:
            print(number, '-', dish[0])
            number += 1
        
        number = int(input('Ваш вибір:'))
        index = number - 1

        dish = menu[index]
        
        while True: # робота з dish
            print('----= Робота зі стравою =----')
            print('Назва:', dish[0])
            print('Ціна:', dish[1])
            print('Куплено: ', dish[2])
            print('Розділ:', dish[3])
            print('Інгрідієнти:')
            for ingredient in dish[4]:
                print('-', ingredient)

            print('\nВиберіть, що ви хочете змінити:')
            print('0 - до головного меню')
            print('1 - назва')
            print('2 - ціна')
            print('3 - куплено')
            print('4 - розділ')
            print('5 - інгрідієнти')
            choice = input('Ваш вибір: ')

            if choice == '1':
                # вводимо назву страви
                while True:
                    name = input('Введіть назву страви: ')
                    if 4 <= len(name) <= 40:
                        break
                    else:
                        print('Довжина не підходить!')
                dish[0] = name

            elif choice == '2':
                # вводимо ціну
                while True:
                    price = input('Ціна: ')
                    if price.isdigit():
                        price = int(price)
                        if price <= 0:
                            print('Число не підходить!')
                        else:
                            break
                    else:
                        print('Це не число!')
                dish[1] = price

            elif choice == '3':
                # вводимо кількість
                while True:
                    count = input('Куплено: ')
                    if count.isdigit():
                        count = int(count)
                        if count <= 0:
                            print('Число не підходить!')
                        else:
                            break
                    else:
                        print('Це не число!')
                dish[2] = count

            elif choice == '4':
                # вводимо розділ
                while True:
                    section = input('Введіть розділ: ')

                    if 4 <= len(section) <= 20:
                        break
                    else:
                        print('Не підходяща кількість символів!')
                dish[3] = section

            elif choice == '5':
                # вводимо інгрідієнти
                ingredients = []
                while True:
                    ingredient = input('Інгрідієнт: ')
                    
                    if ingredient == 'stop' or ingredient == 'стоп':
                        break

                    if 3 <= len(ingredient) <= 30:
                        ingredients.append(ingredient)
                    else:
                        print('Не підходяща кількість символів')

                dish[4] = ingredients

            elif choice == '0':
                break
    
    elif choice == '5':
        ingredient = input('Введіть інгрідієнт: ')

        for dish in menu:
            ingredients = dish[4]
            if ingredient in ingredients:
                print('-', dish[0])
    
    elif choice == '6':
        print('0 - назад')
        number = 1
        for dish in menu:  # ['борщ', 50, 12, 'перше', ['вода', "буряк", "катопля", "квасоля"]]
            print(number, '-', dish[0], "(", dish[2], ")")
            number += 1
        number = int(input('Виберіть страву: '))
        if number != 0:
            index = number - 1
            dish = menu[index]
            dish[2] += 1
            print('Збережено')

    elif choice == '7':
        ingrs = []
        for dish in menu:
            for ingr in dish[4]:
                if ingr not in ingrs:
                    ingrs.append(ingr)
                    print(ingr)

    elif choice == '8':
        min_price = float('inf')
        min_names = []
        for dish in menu:
            if dish[1] < min_price:
                min_price = dish[1]
                min_names.clear()
                min_names.append(dish[0])
            elif dish[1] == min_price:
                min_names.append(dish[0])
        
        print(min_price)
        print(min_names)
    
    elif choice == '0':
        break
