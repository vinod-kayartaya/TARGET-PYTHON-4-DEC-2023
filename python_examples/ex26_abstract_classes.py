from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def shape_name(self):
        pass

    def author_info(self):
        return 'Vinod <vinod@vinod.co>'


class Circle(Shape):
    def __init__(self, radius=1):
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def shape_name(self):
        return 'Circle'


class Square(Shape):
    def __init__(self, side=1):
        self.__side = side

    def get_area(self):
        return self.__side**2

    def shape_name(self):
        return 'Square'

    def author_info(self):
        return 'Kumar <kumar@xmpl.com>'


if __name__ == '__main__':
    c1 = Circle(2.3)
    print(f'area of {c1.shape_name()} is {c1.get_area()} - written by {c1.autho_info()}')
    s1 = Square(4.5)
    print(f'area of {s1.shape_name()} is {s1.get_area()} - written by {s1.autho_info()}')
