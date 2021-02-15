data = [
#   [ім'я студента, вік студента, назва групи, країна в якій студент навчається, форма навчання, [бали по ОС]]
    ['Роман', 21, 'ЕС-18м', 'Україна', 'денна', ['вишка - 84 бали', "Елекричні апарати - 94", "Перехідні процеси - 75", "Психологія - 89"]],
    ['Іван', 22, 'ЕСМ-16м', 'Україна', 'денна', ['Мережі - 65 бали', "Елекричні частини станцій - 91", "Перехідні процеси - 96", "Філософія - 84"]],
    ['Marek', 22, 'EMST 1.2a', 'Polska(Poland)', 'stacjonarna', ['Podstawy-Normalizacji - 68 ', "Komputerowa Analiza SEE - 84", "Elektrotechnologie - 89", "Napędy - 99"]],
    ['Андрій', 19, 'ЕС-20б', 'Україна', 'заочна', ['Трансформатори - 96 бали', "Елекричні мережі і системи - 5", "Сучасні технології - 4", "Правознавство - 5"]],
    ['John', 28, 'DAAD 15', 'England', 'stationary', ['Mathematics  - 90 ', "Civil Technology or Electrical Technology or Mechanical Technology - 80", "Engineering Graphics and Design - 86", "Life Orientation - 94"]],
    ['Roman', 23, 'EMST 1.6a', 'Polska(Poland)', 'stacjonarna', ['Metody kompensacji mocy biernej - 94', "Matematyka - 80", "Elektrocieplownie - 69", 'Elektromechaniczne systemy napędowe - 79']]
    ]


while True:
    print("--= Список студентів  =--")
    print('1 - додати нового  студента')
    print('2 - продивитися список студентів')
    print('0 - вихід з програми')

    choice = input('Ваш вибір: ')
    
    if choice == '1':
        # вводимо ім'я студента
        while True:
            name = input("Введіть ім'я студента: ")
            if 4 <= len(name) <= 40:
                break
            else:
                print('Довжина не підходить!')

        # вводимо вік студента
        while True:
            age = input('Вік студента: ')
            if age.isdigit():
                age = int(age)
                if age <= 0:
                    print('Число не підходить!')
                else:
                    break
            else:
                print('Це не число!')

        # вводимо назву групи
        while True:
            grupe = input("Введіть назву групи: ")
            if 3 <= len(name) <= 30:
                break
            else:
                print('Довжина не підходить!')

        # країна в якій студент навчається
        while True:
            country = input('Введіть країну: ')

            if 4 <= len(country) <= 20:
                break
            else:
                print('Не підходяща кількість символів!')
                
        # форма навчання студента
        while True:
            form = input('Введіть свою форму навчання: ')
            if 4 <= len(form) <= 20:
                break
            else:
                print('Не підходяща кількість символів!')
        

        # вводимо бали за навчання
        points = []
        while True:
            point = input('Інгрідієнт: ')
            
            if point == 'stop' or point == 'стоп':
                break

            if 3 <= len(point) <= 30:
                points.append(point)
            else:
                print('Не підходяща кількість символів')

        students = [name, age, grupe, country, form, points]
        data.append(students)
    
    elif choice == '2':
        for students in data:  # ['Роман', '21' 'ЕС-18м', 'Україна', 'денна', ['вишка - 4 бали', "Елекричні апарати - 5", "Перехідні процеси - 4", "Психологія - 5"]
            print('-' * 30)
            print("ім'я студента:", students[0])
            print('вік студента:', students[1])
            print('назва групи: ', students[2])
            print('країна в якій студент навчається:', students[3])
            print('форма навчання: ', students[4])
            print('бали по ОС')
            for oceny in students[5]:
                print('-', oceny)
        print('-' * 30)
        
        
    elif choice == '0':
        break
