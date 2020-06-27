for i in range (1, 101):
    # print "fizz" for integers divisible by 3
    if (i % 3) == 0:
        if (i % 5) != 0:
            print("fizz")
    # print "buzz" for integers divisible by 5
    if (i % 5) == 0:
        if (i % 3) != 0:
            print("buzz")
    # print "fizzbuzz" for integers divisible by 15
    if (i % 15) == 0:
        print("fizzbuzz")
    else:
        print(i)
