"""1. Print three different strings.
"""
print("String One!")
print("String Two!")
print("String Three!")

"""2. Write a program that prints a message if a variable is less than 10, and
    different message if the variable is greater than or equal to 10.
"""
x = input("Enter a number:")
x = int(x)
if x < 10:
    print(f"{x} is less than 10.")
else:
    print(f"{x} is greater than or equal to 10.")

"""3. Write a program that prints a message if a variable is less than or equal
    to 10, another message if the variable is greater than 10 but less than or equal to 25, and another message if the variable is greater than 25.
"""
y = input("Enter a number:")
y = int(y)
if y <= 10:
    print(f"{y} is less than or equal to 10.")
if y > 10 and y <= 25:
    print(f"{y} is greater than 10, but less than or equal to 25.")
if y > 25:
    print(f"{y} is greater than 25.")

"""4. Create a program that divides two variables and prints the remainder.
   5. Create a program that takes two variables, divides them, and prints the
        quotient.
"""
a = input("Enter a number:")
a = int(a)
b = input("Enter another number:")
b = int(b)
c = a % b
d = a // b
print(f"{a} divided by {b} has a remainder of {c}.")
print(f"{a} divided by {b} has a quotient of {d}.")

"""6. Write a program with a variable age assigned to an integer that prints
    different strings depending on what integer age is.
"""
age = input("Enter a number:")
age = int(age)
wait = 21 - age
if age >= 21:
    print("Have a beer.")
else:
    print(f"Come back in {wait} years!")
