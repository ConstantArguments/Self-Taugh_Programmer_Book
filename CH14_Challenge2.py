"""2. Change the Square class so that when you print a Square object, a
    message prints telling you the len of each of the four sides of the
    shape. For example, if you create a square with Square(29) and print
    it, Python should print 29 by 29 by 29 by 29.
"""

class Square:
    square_list = []
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.square_list.append(self) # appends list with objects
        print(f"{self} created!")
    def __repr__(self):
        return (
            f"{self.length} by {self.width}"
            f" by {self.length} by {self.width}"
            )


square1 = Square(2, 2)
square2 = Square(4, 4)
square3 = Square(3, 3)
square4 = Square(5, 5)

print(Square.square_list)
