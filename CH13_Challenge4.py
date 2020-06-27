"""4. Create a class called Horse and a class called Rider. Use composition to model a horse
    that has a rider.
"""

class Person:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.hair = height
        self.weight = weight
        self.age = age
        print(f"{self} created!")

class Rider(Person):
    def __init__(self, name, height, weight, age, skill):
        Person.__init__(self, name, height, weight, age) # inherits parent's properties
        self.skill = skill # adds additional properties
        print(f"{self} created!") # output will show 2 objects at same

class Horse:
    def __init__(self, name, color, weight, age, rider):
        self.name = name
        self.color = color
        self.age = age
        self.rider = rider
        print(f"{self} created!")

rider1 = Rider("Melissa", "5'8\"", "130 lbs", 38, "low")
horse1 = Horse("Biscuit", "tan", "1300 lbs", "9 months", rider1)

print(f"{horse1.name}'s rider is {horse1.rider.name}")
