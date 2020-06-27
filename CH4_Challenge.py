"""1. Write a function that takes a number as an input and returns that number
    squared.
"""

def num_squared():
    """
    Returns user input squared.
    """

    x = input("Enter a number: ")
    try:
        x = float(x)
        result = x ** 2
        return(result)
    except ValueError:
        print("You should have entered a number!")

"""2. Create a function that accepts a string as a parameter and prints it.
"""

def print_string():
    """
    Returns input string.
    """

    x = input("Enter a word or phrase: ")
    x = str(x)
    if x != "":
        return(x)
    else:
        print("Invalid Input!")

"""3. Write a function that takes three required parameters and two optional
    parameters.
"""

def three_param(x, y=4, z=6):
    """
    Returns x + y + z.
    :param x: int or float.
    :optional param y: int or float.
    :optional param z: int or float.
    """

    x = float(x)
    y = float(y)
    z = float(z)
    result = x + y + z
    return result

"""4. Write a program with two functions. The first function should take an integer
    as a parameter and return the result of the integer divided by 2. The second function should take an integer as a parameter and return the result of the integer multiplied by 4. Call the first function, save the result as a variable, and pass it as a parameter to the second function.
"""

def div_by_two(x):
    """
    Returns x / 2.
    :param x: int.
    """

    result = x / 2
    return result

def mult_by_four(x):
    """
    Returns x * 4.
    :param x: int.
    """

    result = x * 4
    return result

"""5. Write a function that converts a string to a float and returns the result.
    Use exception handling to catch the exception that could occur.
"""

def string_to_float(x):
    """
    Returns a float.
    param x: int.
    """

    try:
        return float(x)
    except:
        print("You should have entered a number!")

print(num_squared())

print(print_string())

print(three_param(2))

x = div_by_two(4)
print(mult_by_four(x))

print(string_to_float(8))

# 6. Add a docstring to all of the functions you wrote in challenges 1–5.
