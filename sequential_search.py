def seq_search(items, n):
    """
    Returns True if item in list.
    :param list: list containing items.
    :param n: item you are searching for.
    :return: True or False.
    """
    found = False
    for i in items:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
search1 = seq_search(numbers, 2)
print(search1)

numbers = range(0, 100)
search2 = seq_search(numbers, 200) #200 is not in numbers
print(search2)

words = [
    "able", "about", "above", "accept", "according", "account", "across",
    "act", "action", "activity", "actually", "add", "address",
    "administration", "admit", "adult", "affect", "after", "again", "against",
    "age", "agency"
    ]
search3 = seq_search(words, "across")
print(search3)