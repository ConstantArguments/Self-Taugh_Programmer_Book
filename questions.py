questions = ["What is your name?",
             "What is your fav. color?",
             "What is your purpose?",
             "Who is your favorite member of 'Menudo'?",
             "How do you do the dew?",]
n = 0
while True:
    print("Type q to quit")
    a = input(questions[n])
    if a == "q":
        break
    n = (n + 1) % 5 # any number divided by a larger number will % the smaller number

