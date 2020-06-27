"""3. Write a function that takes two objects as parameters and returns True if they are
    the same object, and False if not.
"""

class Widget:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        print(f"Widget {self} created!")

def is_same(a, b):
    return a is b

widget1 = Widget("Bonk", 44)
widget2 = Widget("Bonk", 44)
widget3 = Widget("Conk", 22)
same_widget = widget1

print(is_same(widget1, widget2)) #False (differnt Objects with same Properties)
print(is_same(widget1, widget3)) #False
print(is_same(same_widget, widget1)) #True