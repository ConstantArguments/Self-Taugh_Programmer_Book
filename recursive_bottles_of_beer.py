def bottles_of_beer(bob):
    """
    Recursive.
    Prints lyrics for '99 bottles of beer'.
    Adjusts plural of bottle as needed.
    :param bob: positive int.
    """
    tmp = bob
    stmp = "s"
    sbob = "s"
    if bob == "no more":
        print("Are we drunk yet?")
        return
    bob -= 1
    if tmp == 1:
        stmp = ""
    if bob == 1:
        sbob = ""
    if bob == 0:
        bob = "no more"
    print(f"{tmp} bottle{stmp} of beer on the wall. {tmp} bottle{stmp} of beer. Take one down, pass it around, {bob} bottle{sbob} of beer on the wall.")
    bottles_of_beer(bob)

bottles_of_beer(99)