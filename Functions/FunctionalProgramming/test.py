numbers = input('Введіть числа через пробіл:\n').split(' ')

new_numbers = [int(number) for number in numbers]

print(max(new_numbers))
