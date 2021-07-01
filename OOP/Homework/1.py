class Child:
    name = ''
    age = 0

    def information(self):
        print(self.name, self.age)

    def age1y(self):
        self.age += 1
        print(f"teper {self.name} {self.age} rokiw")


c1 = Child()
c1.name = 'Mikola'
c1.age = 6

c2 = Child()
c2.name = 'Vasiok'
c2.age = 5

c2.information()
c1.age1y()
