"""1. Print each item in the following list:
    [
    "The Walking Dead", "Entourage",
    "The Sopranos", "The Vampire Diaries"
    ].
"""

mylist = [
    "The Walking Dead", "Entourage",
    "The Sopranos", "The Vampire Diaries"
    ]
for shows in mylist:
    print(shows)

"""2. Print all the numbers from 25 to 50.
"""

for i in range (25, 51):
    print(i)

"""3. Print each item in the list from the first challenge and their
    indexes.
"""

i = 0
for shows in mylist:
    print(f"Index for {shows} is [{i}].")
    i += 1

"""4. Write a program with an infinite loop (with the option to type q
    to quit) and a list of numbers. Each time through the loop ask the
    user to guess a number on the list and tell them whether or not they
    guessed correctly.
"""

import random

random.seed()

list = []
for i in range (1, 11):
    list.append(random.randint(1, 100))
list.sort()
# print(list)

while True:
    guess = input(
        "\n\nType \"q\" to QUIT, or... Guess a number between 1 and 100: "
        )
    try:
        if guess == "q":
            print("\n\nQ U I T T E R !!!! :(")
            break
        guess = int(guess)
        if guess in list:
            print("You guessed correctly!")
            print(list)
            break
        else:
            print("Wrong! Try again.")
            continue
    except:
        continue

"""5. Multiply all the numbers in the list [8, 19, 148, 4] with all the
    numbers in the list [9, 1, 33, 83], and append each result to a
    third list.
"""
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for numbers1 in list1:
    for numbers2 in list2:
        product = numbers1 * numbers2
        list3.append(product)

print(list1)
print(list2)
print(list3)
