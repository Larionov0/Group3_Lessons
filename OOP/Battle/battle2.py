import random


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

    def make_move(self, enemies_team):
        alive_team = [enemy for enemy in enemies_team if enemy.is_alive]
        if alive_team:
            target = random.choice(alive_team)
            self.kick(target)


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


def check_if_team_alive(team):
    # for warrior in team:
    #     if warrior.is_alive:
    #         return True
    # return False
    return any([warrior.is_alive for warrior in team])


def battle(team_1, team_2):
    round_ = 1
    while check_if_team_alive(team_1) and check_if_team_alive(team_2):
        print(f'---------| Round {round_} |----------')
        print('-------- Перша команда')
        for warrior in team_1:
            if warrior.is_alive:
                warrior.make_move(team_2)

        print('-------- Друга команда')
        for warrior in team_2:
            if warrior.is_alive:
                warrior.make_move(team_1)
        round_ += 1

    if not check_if_team_alive(team_1) and not check_if_team_alive(team_2):
        print('Нічия!')
    elif check_if_team_alive(team_1):
        print(f'Перша команда виграла')
    elif check_if_team_alive(team_2):
        print(f'Друга команда виграла')


def gen_gnome():
    weap = Weapon()
    weap.name = 'гномомеч'
    weap.msg = '*фіть*'
    weap.damage = random.randint(1, 2)
    weap.durability = random.randint(2, 10)

    gnome = Warrior()
    gnome.name = random.choice(['Реп`ях', 'Бульбар', "Гномар"])
    gnome.hp = gnome.max_hp = random.randint(5, 12)
    gnome.weapon = weap
    gnome.damage = random.randint(1, 2)
    gnome.armor = 0
    return gnome


def gen_orc():
    weap = Weapon()
    weap.name = 'дубина'
    weap.msg = '*БАМ*'
    weap.damage = random.randint(2, 4)
    weap.durability = random.randint(5, 15)

    orc = Warrior()
    orc.name = random.choice(['Ылмак', 'Тудрак', "Бердек"])
    orc.hp = orc.max_hp = random.randint(18, 30)
    orc.weapon = weap
    orc.armor = random.randint(1, 2)
    orc.damage = random.randint(3, 6)
    return orc


gnomes_team = [gen_gnome() for _ in range(50)]
orcs_team = [gen_orc() for _ in range(15)]


battle(orcs_team, gnomes_team)

print(len([enemy for enemy in gnomes_team if enemy.is_alive]))
print(len([enemy for enemy in orcs_team if enemy.is_alive]))
