class Warrior:
    name = ''
    attack = 3
    hp = max_hp = 10
    armor = 1
    is_alive = True
    weapon = None

    def get_damage(self, damage):
        remaining_damage = damage - self.armor
        print(f'Пройшло {remaining_damage} / {damage} одиниць урона')
        if remaining_damage > 0:
            self.hp -= remaining_damage
            print(f'{self.name} втратив {remaining_damage} hp. Тепер у нього {self.hp} / {self.max_hp} hp')
            if self.hp <= 0:
                self.die()

    def die(self):
        self.is_alive = False
        print(f'{self.name} помирає в бою!')

    def kick(self, other):
        print(f'{self.name} дає копняка по {other.name}')
        bonus = 0
        if self.weapon is not None:
            bonus += self.weapon.kick_bonus()
        other.get_damage(self.attack + bonus)


class Weapon:
    name = ''
    damage = 1
    msg = '*дзвін меча*'
    durability = 4
    is_alive = True

    def kick_bonus(self):
        """
        Повертає бонус урона
        """
        if self.is_alive is False:
            return 0

        print(f'{self.msg}  (+ {self.damage} damage)')
        self.decrease_durability()
        return self.damage

    def decrease_durability(self):
        self.durability -= 1
        if self.durability == 0:
            print(f'Зброя {self.name} зламалася')
            self.is_alive = False


def battle(w1, w2):
    round_ = 1
    while w1.is_alive and w2.is_alive:
        print(f'---------| Round {round_} |----------')
        w1.kick(w2)
        w2.kick(w1)
        round_ += 1

    if not w1.is_alive and not w2.is_alive:
        print('Нічия!')
    elif w1.is_alive:
        print(f'{w1.name} виграв')
    elif w2.is_alive:
        print(f'{w2.name} виграв')


weapon1 = Weapon()
weapon1.name = 'Меч'
weapon1.damage = 3
weapon1.durability = 2
weapon1.msg = '*дзвін меча*'

w1 = Warrior()
w1.name = 'Буйло'
w1.attack = 4
w1.weapon = weapon1


weapon2 = Weapon()
weapon2.name = 'Дубина'
weapon2.damage = 1
weapon2.durability = 10
weapon2.msg = '*звук тупого удару*'

w2 = Warrior()
w2.name = 'Парез'
w2.armor = 2
w2.hp = w2.max_hp = 15
w2.weapon = weapon2


battle(w1, w2)
