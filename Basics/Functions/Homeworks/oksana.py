def criateNlist(n):
    list = []
    number = 0
    while number < n:
        list.append(n)
        number += 1
    return list


print(criateNlist(n=3))
print(criateNlist(4))

