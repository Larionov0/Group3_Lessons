queue = ['Mary', 'Bob', 'Oliy']
while True:
    print ('На даний час черга виглядає так: \n' + str(queue))
    print('1 - add person: ')
    print('2 - pop person: ')
    print('3 - print queue: ')

    choise = input ('Something new?_')
    if choise == '1' :
        name = input('Enter new person: ')
        queue.append(name)
    elif choise == '2' :
        if len(queue) == 0 :
            print ('Free')
        else:
            queue.pop(0)
    elif choise == '3' :
        break

