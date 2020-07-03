"""1. Create Rectangle and Square classes with a method called
    calculate_perimeter that calculates the perimeter of the shapes they
    represent. Create Rectangle and Square objects and call the method
    on both of them.
   2. Define a method in your Square class called change_size that
    allows you to pass in a number that increases or decreases (if the
    number is negative) each side of a Square object by that number.
"""

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
        print(f"{self} Created!")

    def perimeter(self):
        result = 2 * self.length + 2 * self.width
        return result

class Square(Rectangle):
    def change_size(self, cl, cw):
        self.length = self.length + cl
        self.width = self.width + cw
        print(f"{self} Size Changed!")

rectangle1 = Rectangle(2, 4)
square1 = Square(4, 4)
print(rectangle1.perimeter())
print(square1.perimeter())

square1.change_size(1, 1)
print(square1.perimeter())
