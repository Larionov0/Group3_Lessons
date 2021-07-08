import random


class Human:
    def __init__(self, name, surname, age=0, money=0, is_male=False):
        self.name = name
        self.surname = surname
        self.age = age
        self.money = money
        self.is_male = is_male

    def say_hi(self):
        print(f'{self.name}: "Hello, my age is {self.age}"')

    def say_hi_to_smwn(self, other_human):
        print(f"{self.name}: 'Hello, {other_human.name}!'")

    def grow_up(self):
        self.age += 1
        word = 'йому' if self.is_male else 'їй'
        print(f'У {self.name} день народження! Тепер {word} {self.age} років!')

    def __str__(self):
        sex = 'чоловік' if self.is_male else 'жінка'
        return f"Людина {self.name}. {sex}\n" \
               f"{self.age} років, {self.money} грн"


class Worker(Human):
    def __init__(self, name, surname, age=0, job=None, salary=0, money=0, is_male=False):
        super().__init__(name, surname, age, money, is_male)
        self.job = job
        self.salary = salary

    def work(self):
        if self.job == 'маляр':
            print(f'{self.name}: *звуки фарби*')
        elif self.job == 'програміст':
            print(f'{self.name}: *звуки клавіатури*')
        self.money += self.salary
        print(f'{self.name} отримав {self.salary} грн. Тепер у нього {self.money} грн')

    def say_hi(self):
        print(f'{self.name} (стомлено): Ну привіт')

    def grow_up(self):
        super().grow_up()
        print(f'Подарунок від компанії! 1000 грн')
        self.money += 1000

    def get_job_document(self):
        return f"Працівник {self.name} {self.surname}\n" \
               f"Вік: {self.age}\n" \
               f"Стать: {'чоловік' if self.is_male else 'жінка'}"


h1 = Human('Bob', 'Bobinski', 21, 20000, is_male=True)
h2 = Human('Anna', 'Anninska', 29, 28000)
w1 = Worker('Alex', 'Alexenko', 22, 'програміст', 30000, 10000, True)


w1.work()
