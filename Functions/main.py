def line():
    print('-' * 40)


def helloer(name):
    print(f"Hello, {name}")


def summer(n1, n2):
    result = n1 + n2
    return result


def kley(strings, sep):
    """
    :param strings: list[str]
    ['Alan', 'Alex', 'Leha']
    :param sep: str
    '-=-'

    :return: str
    kley(['a', 'b', 'c'], '==')   ->   'a==b==c'
    """
    text = ''
    for string in strings:
        text += string + sep
    text = text[:-len(sep)]
    return text


# strings = ['Alan', 'Bob', 'Katia']
# text = kley(strings, sep='=<->=')
# print(text)


def input_int(question, min_=None, max_=None, error_message='Це не число'):
    while True:
        number_str = input(question)
        if number_str.isdigit():
            number = int(number_str)

            if min_ != None:
                if number < min_:
                    print('Надто мале число:(')
                    continue
            if max_ != None:
                if number > max_:
                    print('Надто велике число:(')
                    continue

            return number
        else:
            print(error_message)


age = input_int('Введіть вік: ', 10, 150)
print(age + 1)
count = input_int('Введіть кількість: ')
time = input_int('Введіть час: ', error_message='Час в секундах (число)!')
