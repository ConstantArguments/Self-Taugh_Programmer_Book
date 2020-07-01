def count_down(go, seconds):
    """
    Recursive.
    Countdown to blast off.
    :param go: Bool.
    :param seconds: positive int.
    """
    if go  == True:
        print(f"T-minus {seconds} seconds and counting...")
        go = False
    seconds -= 1
    if seconds == 0:
        print("BLAST OFF!!!")
        return
    print(f"{seconds}")
    count_down(go, seconds)

def mission_control():
    """
    Starts count_down if approved for launch.
    """
    thumb_up = input("Do we have a go on launch? y/n: ")
    thumb_up = thumb_up.lower()
    if thumb_up == "y":
        count_down(True, 10)
    else:
        print("ALL HANDS STAND DOWN!!!")

mission_control()