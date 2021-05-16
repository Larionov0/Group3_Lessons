def create_list(n):
    lst = []
    number = 1
    for _ in range(n):
        lst.append(number)
        number *= 2
    return lst


def gen_list(n):
    number = 1
    for _ in range(n):
        yield number
        number *= 2


# for number in create_list(6):
#     print(f'Число {number}')

