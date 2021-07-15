def print_decorator(func):
    def new_func(*args, **kwargs):
        print('-' * 40)
        func(*args, **kwargs)
        print('-' * 40)

    return new_func


@print_decorator
def print_smile():
    print(':)')


@print_decorator
def print_hello(name):
    print(f"Hello, {name}!")


@print_decorator
def print_list(strings):
    """
    Функція приймає список строк і виводить його на екран,
    кожну строку в окремому рядочку.
    """
    for string in strings:
        print(f'- {string}')


@print_decorator
def print_v(w, h, l):
    print(w * l * h)


print_hello('Bob')
print_list(['lol', 'lol', 'pup'])
print_smile()
print_v(3, 2, 2)
print_v(l=10, w=10, h=100)
