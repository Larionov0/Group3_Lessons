class Slime:
    def __init__(self, name, weight, eyes=2):
        self.name = name
        self.weight = weight
        self.eyes = eyes

    def __gt__(self, other):  # >
        return self.weight > other.weight

    def __eq__(self, other):  # ==
        return self.weight == other.weight and self.eyes == other.eyes

    def __ge__(self, other):  # >=
        return self.weight >= other.weight

    def __add__(self, other):  # +
        new_slime = Slime(
            name='New',
            weight=self.weight + other.weight,
            eyes=self.eyes + other.eyes
        )
        self.weight = 0
        self.eyes = 0
        other.weight = 0
        other.eyes = 0

        return new_slime

    def __str__(self):  # str   (і за print)
        return f'Слимачок {self.name} ({self.weight} кг;  {self.eyes} очей)'


s1 = Slime('Solly', 10)
s2 = Slime('Bolly', weight=4, eyes=3)


if s1 > s2:
    print('Соллі великий')
else:
    print('Соллі маленький')

print(s1)
print(s2)
s3 = s1 + s2
print(s3)

print(s1)
