"""1. Define a class called Apple with four instance variables that represent four
    attributes of an apple.
"""

class Apple:
    def __init__(self, w, c, s, p):
        self.weight = w
        self.color = c
        self.sweet = s
        self.picked = p
        print(f"{self} Created!")

apple1 = Apple(6, "red mottled", True, 10)
apple2 = Apple(7.3, "green", False, 3)

"""2. Create a Circle class with a method called area that calculates and returns its area.
    Then create a Circle object, call area on it, and print the result. Use Python's pi
    function in the built-in math module.
"""
import math # normally imports at top of file

class Circle:
    def __init__(self, r):
        self.radius = r
        print(f"{self} Created!")

    def area(self):
        result = 2 * math.pi * self.radius
        return result

circle1 = Circle(4)
circle2 = Circle(17)
print(circle1.area())
print(circle2.area())

"""3. Create a Triangle class with a method called area that calculates and returns its area.
    Then create a Triangle object, call area on it, and print the result.
"""

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print(f"{self} Created!")

    def area(self):
        result = self.base * self.height / 2
        return result

triangle1 = Triangle(2, 4)
triangel2 = Triangle(11, 5)
print(triangle1.area())
print(triangel2.area())

"""4. Make a Hexagon class with a method called calculate_perimeter that calculates and
    returns its perimeter. Then create a Hexagon object, call calculate_perimeter on it, and
    print the result.
"""

class Hexagon:
    def __init__(self, a, b, c, d, e, f):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d
        self.side5 = e
        self.side6 = f
        print(f"{self} Created!")

    def perimeter(self):
        result = self.side1 + self.side2 + self.side3 +self.side4 + self.side5 + self.side6
        return result

hexagon1 = Hexagon(2, 4, 6, 4, 3, 1)
hexagon2 = Hexagon(23, 14, 7, 18, 22, 4)
print(hexagon1.perimeter())
print(hexagon2.perimeter())
