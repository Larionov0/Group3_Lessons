numbers = input('Введіть числа через пробіл:\n').split(' ')

new_numbers = map(int, numbers)

print(max(new_numbers))
