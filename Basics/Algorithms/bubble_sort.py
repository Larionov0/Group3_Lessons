names = ['Olya', 'Katia', 'Vasya', 'Olexa', 'Bob']
ages = [25, 12, 21, 14, 22]

ogr = len(ages) - 1
while ogr != 0:
    i = 0
    while i < ogr:
        if ages[i] > ages[i + 1]:
            ages[i], ages[i + 1] = ages[i + 1], ages[i]
            names[i], names[i + 1] = names[i + 1], names[i]
        i += 1
    ogr -= 1

print(names)
print(ages)

