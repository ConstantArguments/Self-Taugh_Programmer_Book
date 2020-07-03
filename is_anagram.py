def is_anagram(word1, word2):
    """
    Compares two strings to check if anagram.
    Returns true.
    :param: word1
    :param: word2
    """
    word1 = sort(word1)
    word2 = sort(word2)
    return word1 == word2

def sort(word):
    """
    Takes string and converts to lowercase, strips all whitespace, and
    sorts alphabetically.
    Returns modified string.
    :param: word
    """
    word = word.lower()
    word = word.replace(" ", "")
    word = sorted(word)
    return word

print(is_anagram("button", "potato"))
print(is_anagram("Anagram", "Nag A Ram"))
