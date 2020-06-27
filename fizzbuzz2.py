def fizzbuzz():
    print("\nThis is FIZZBUZZ!\n\nIf a number is divisible by \"3\", say \"fizz\".\n"
            "If the number is divisible by \"5\", say \"buzz\".\n"
            "If the number is divisible by \"15\", say \"fizzbuz\".\n"
            "\nGO!\n")
    for i in range (1, 101):
        # print "fizz" for integers divisible by 3
        if i % 3 == 0 and i % 5 != 0:
            print("fizz")
        # print "buzz" for integers divisible by 5
        if i % 5 == 0 and i % 3 != 0:
            print("buzz")
        # print "fizzbuzz" for integers divisible by 15
        if i % 15 == 0:
            print("fizzbuzz")
        else:
            print(i)

fizzbuzz()
