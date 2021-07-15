class Human:
    name = 'Bob'
    age = 0
    money = 0


h1 = Human()
h1.name = 'Alex'
h1.age = 20
h1.money = 10000

h2 = Human()
h2.name = 'Anna'
print(h1.name, h2.name)

h3 = Human()
h3.age = 36

people = [h1, h2, h3]
sum_age = 0
for human in people:
    sum_age += human.age
print(sum_age / len(people))
