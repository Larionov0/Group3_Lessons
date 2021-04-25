a = int(input())
try:
    print(2 / a)
except ZeroDivisionError:
    print('Сталася помилка')

print('The end')
