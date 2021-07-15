numbers = [5, 4, 2, 6, 2, 8, 4, 7, 3]

max_ = 0
min_ = float('inf')
for number in numbers:
    if number > max_:
        max_ = number
    if number < min_:
        min_ = number

print(max_)
print(min_)
