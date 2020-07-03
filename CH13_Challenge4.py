"""4. Create a class called Horse and a class called Rider. Use
    composition to model a horse that has a rider.
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
        """
        Inherits parent's properties.
        Adds additional properties.
        """
        Person.__init__(self, name, height, weight, age)
        self.skill = skill
        # Will print 2 duplicate lines because of inheritance of Person.
        print(f"{self} created!")

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
