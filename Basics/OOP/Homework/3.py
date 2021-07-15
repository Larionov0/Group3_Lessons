class Slime:
    name = ''
    weight = 0

    def prilepit(self, other):
        self.weight += other.weight
        other.weight = 0


s1 = Slime()
s1.name = "Solly"
s1.weight = 14

s2 = Slime()
s2.name = "Bolly"
s2.weight = 4


s2.prilepit(s1)
print(s1.weight)
print(s2.weight)
