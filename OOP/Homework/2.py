class Rectangle:
    width = 0
    length = 0

    def square(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width * 2) + (self.length * 2)

    def print_square(self):
        print(f"Площа: {self.square()}")

    def print_perimeter(self):
        print(f"Периметр: {self.perimeter()} ")


r1 = Rectangle()
r1.width = 5
r1.length = 6


r1.print_perimeter()
r1.print_square()
