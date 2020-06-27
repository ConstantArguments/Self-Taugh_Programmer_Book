"""1. Find a file on your computer and print its contents using Python.
"""

with open("quote.txt", "r") as f:
    print(f.read())


"""2. Write a program that asks a user a question, and saves their answer to a file.
"""

def question():
    answer = input("What is your favorite quote?: ")
    quote = open("quote.txt", "w")
    quote.write(answer)
    quote.close

question()

"""3. Take the items in this list of lists:
    [["Top Gun", "Risky Business", "Minority Report"],
     ["Titanic", "The Revenant", "Inception"],
     ["Training Day", "Man on Fire", "Flight"]]
     and write them to a CSV file. The data from each list should be a row in
     the file, with each item in the list separated by a comma.
"""
import csv

films = [["Top Gun", "Risky Business", "Minority Report"],
         ["Titanic", "The Revenant", "Inception"],
         ["Training Day", "Man on Fire", "Flight"]]

def movies():
    with open("movies.csv", "w") as f:
        w = csv.writer(f, delimiter=",")
        for film in films:
                w.writerow(film)

movies()
