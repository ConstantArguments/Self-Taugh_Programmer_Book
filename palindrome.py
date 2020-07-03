def palindrome(word):
    """
    Returns True of false if word is the same forwards and backwards.
    :param word: str for comparison.
    """
    word = word.lower()
    word = word.replace(" ", "")
    #[::-1] is syntax for returning a slice of an entire iterable in reverse.
    return word[::-1] == word

print(palindrome("Hamster"))
print(palindrome("Mom"))
print(palindrome("Madam Im Adam"))