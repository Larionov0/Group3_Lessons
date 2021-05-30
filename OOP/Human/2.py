import random


class Human:
    name = 'Bob'
    age = 0
    money = 0
    is_male = True

    def say_hi(self):
        print(f'{self.name}: "Hello, my age is {self.age}"')

    def say_hi_to_smwn(self, other_human):
        print(f"{self.name}: 'Hello, {other_human.name}!'")

    def grow_up(self):
        self.age += 1
        word = 'йому' if self.is_male else 'їй'
        print(f'У {self.name} день народження! Тепер {word} {self.age} років!')

    def born_child(self, other_human):
        if self.is_male != other_human.is_male and self.age >= 14 and other_human.age >= 14:
            child = Human()
            child.name = random.choice(['Павло', "Іван", "Петро", "Анна", "Ірина"])
            child.is_male = bool(random.randint(0, 1))
            return child
        else:
            return None

    def print(self):
        sex = 'чоловік' if self.is_male else 'жінка'
        print(f"Людина {self.name}. {sex}\n"
              f"{self.age} років, {self.money} грн")


h1 = Human()
h1.name = 'Alex'
h1.age = 20
h1.money = 10000

h2 = Human()
h2.name = 'Anna'
h2.is_male = False
h2.age = 20

# h1.say_hi_to_smwn(h2)
# h1.grow_up()
# h2.grow_up()

child = h1.born_child(h2)
child.print()
h1.print()
h2.print()
