def sum_calc():
    """
    Користувач вводить числа через +
    4 + 2 + 1 + 6 + 4 + 3 + 53 + 3
    Програма має підрахувати суму відповідних чисел.
    """
    string = input('Введіть числа:\n')
    numbers = string.split('+')
    sum_ = 0
    for brute_number_str in numbers:  # '  12 '
        clean_number_str = brute_number_str.strip()
        number = int(clean_number_str)
        sum_ += number
    print(sum_)


sum_calc()
