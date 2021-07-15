goods = {}
n = 0
while n < 5 :
    print('введіть вагу і назву ', n+1, 'першого товару')
    name = input('Enter goods name ')
    netto = int(input('Netto '))
    goods[name] = netto
    n += 1
print(goods)
