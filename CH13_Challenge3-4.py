"""3. Create a class called Shape. Define a method in it called
    what_am_i that prints "I am a shape" when called. Change your Square
    and Rectangle classes from the previous challenges to inherit from
    Shape, create Square and Rectangle objects, and call the new
    method on both of them.
"""
class Shape:
    def __init__(self, l, w):
        self.length = l
        self.width = w
        print(f"{self} Created!")

    def what_am_i(self):
        print(f"{self} I am a shape!")

class Rectangle(Shape):
    def perimeter(self):
        result = 2 * self.length + 2 * self.width
        return result

class Square(Shape):
    def change_size(self, cl, cw):
        self.length = self.length + cl
        self.width = self.width + cw
        print(f"{self} Size Changed!")

rectangle1 = Rectangle(2, 4)
square1 = Square(4, 4)

rectangle1.what_am_i()
square1.what_am_i()