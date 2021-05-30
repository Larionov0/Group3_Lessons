def factorial(n):
    """
    5! = 5 * 4 * 3 * 2 * 1 = 120

    f(6) = 6 * f(5) = 6 * 5 * f(4) = 6 * 5 * 4 * f(3) =
    = 6 * 5 * 4 * 3 * 2 * f(1) = 6 * 5 * 4 * 3 * 2 * 1
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)


def sum_numbers_in_strange_list(value):
    """
    f([1, 2, [3, [[3, [], 4, [[4, [4], [5]]], [5, 2, 4, [4, 3, [1, 2]]]]]]])

    Точки зупинки:
    1) Коли value - int - повертаємо це value
    2) Коли список value пустий - повертаємо 0

    f([[1], 4, [[1, 2], 4]]) = f([1]) + f([4, [[1, 2], 4]]) =|
    f([1]) = f(1) + f([]) = 1 + 0 = 1

    |= 1 + f([4, [[1, 2], 4]]) = 1 + f(4) + f([[[1, 2], 4]]) =
    = 1 + 4 + f([[[1, 2], 4]]) = 1 + 4 + f([[1, 2], 4]) + f([]) =
    = 1 + 4 + f([1, 2]) + f([4]) + 0 = 1 + 4 + f(1) + f([2]) + f(4) + f([]) + 0 =
    = 1 + 4 + 1 + f(2) + f([]) + 4 + 0 + 0 = 1 + 4 + 1 + 2 + 0 + 4 + 0 + 0
    """
    if type(value) is int:
        return value
    if len(value) == 0:
        return 0

    return sum_numbers_in_strange_list(value[0]) + sum_numbers_in_strange_list(value[1:])


print(sum_numbers_in_strange_list([[1], 4, [[1, 2], 4]]))
print(sum_numbers_in_strange_list([1, 2, [3, [[3, [], 4, [[4, [4], [5]]], [5, 2, 4, [4, 3, [1, 2]]]]]]]))
