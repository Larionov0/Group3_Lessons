def par_decor(n):
    def print_decorator(func):
        def new_func(*args, **kwargs):
            print('-' * n)
            func(*args, **kwargs)
            print('-' * n)

        return new_func

    return print_decorator


@par_decor(50)
def print_smile():
    print(':)')


@par_decor(10)
def print_hello(name):
    print(f"Hello, {name}!")


@par_decor(30)
def print_list(strings):
    """
    Функція приймає список строк і виводить його на екран,
    кожну строку в окремому рядочку.
    """
    for string in strings:
        print(f'- {string}')


@par_decor(1)
def print_v(w, h, l):
    print(w * l * h)


print_hello('Bob')
print_list(['lol', 'lol', 'pup'])
print_smile()
print_v(3, 2, 2)
print_v(l=10, w=10, h=100)
