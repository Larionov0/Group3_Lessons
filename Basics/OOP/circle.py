from math import pi


def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


class Circle:
    r = 0
    x = 0
    y = 0

    def get_l(self):  # довжина кола
        """
        l = 2 pi R
        """
        l = 2 * pi * self.r
        return l

    def get_s(self):  # площа круга
        """
        Pi R ^ 2
        """
        return pi * self.r ** 2

    def check_if_point_is_inside(self, point):
        """
        Перевірити, чи лежить точка всередині кола
        :param point: list[int]
        :return: bool

        Для перевірки треба перевірити, чи відстань від центра кола до точки
        є меншою за радіус кола

        Example:
        circle.check_if_point_is_inside([1, 3]) -> True / False
        """
        d = distance([self.x, self.y], point)

        # if d <= self.r:
        #     return True
        # else:
        #     return False
        return d <= self.r


c = Circle()
c.x = 4
c.y = 3
c.r = 1

if c.check_if_point_is_inside([3.3, 3.7]):
    print('Точка в колі)')
