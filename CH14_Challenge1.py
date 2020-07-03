"""1. Add a square_list class variable to a class called Square so that
    every time you create a new Square object, the new object gets added
    to the list.
"""

class Square:
    square_list = []
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.square_list.append(self) # appends list with objects
        print(f"{self} created!")

square1 = Square(2, 2)
square2 = Square(4, 4)
square3 = Square(3, 3)
square4 = Square(5, 5)

print(Square.square_list)
print(type(Square.square_list[0]))