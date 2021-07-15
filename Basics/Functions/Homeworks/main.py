numbers = [1, 5, 3, 6, 2, 6, 3, 6, 4, 2, 3, 6]


for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)


print(numbers)
