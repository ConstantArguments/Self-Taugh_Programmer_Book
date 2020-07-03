"""1. Print every character in the string "Camus".
"""

name = "Camus"
i = 0
while i < len(name):
    print(name[i:i+1])
    i += 1

"""2. Write a program that collects two strings from a user, inserts
    them into the string "Yesterday I wrote a [response_one]. I sent it
    to [response_two]!" and prints a new string.
"""

def mad_lib():
    """
    Prints string based on user input.
    """
    noun = input("Give me a noun: ")
    person = input("Give me the name of a person: ")
    phrase = "Yesterday I wrote a {}. I sent it to {}!"
    print(phrase.format(noun, person))

mad_lib()

"""3. Use a method to make the string "aldous Huxley was born in 1894."
    grammatically correct by capitalizing the first letter in the
    sentence.
"""

mystring = "aldous Huxley was born in 1894."
mylist = mystring.split()
mylist[0] = mylist[0].capitalize()
print(" ".join(mylist))

"""4. Take the string "Where now? Who now? When now?" and call a method
    that returns a list that looks like:
    ["Where now?", "Who now?", "When now?"].
"""

mylist = "Where now? Who now? When now?".split("?")
del mylist[-1]
i = 0
for x in mylist:
    mylist[i] = mylist[i].strip() + "?"
    i += 1
print(mylist)

"""5. Take list ["The", "fox", "jumped", "over", "the", "fence", "."]
    and turn it into a grammatically correct string. There should be a
    space between each word, but no space between the word fence and the
    period that follows it. (Don't forget, you learned a method that
    turns a list of strings into a single string.)
"""

mylist = ["The", "fox", "jumped", "over", "the", "fence", "."]
del mylist[-1]
print(" ".join(mylist) + ".")

"""6. Replace every instance of "s" in "A screaming comes across the
    sky." with a dollar sign.
"""

mystring = "A screaming comes across the sky."
mystring = mystring.replace("s", "$")
print(mystring)

"""7. Use a method to find the first index of the character "m" in the
    string "Hemingway".
"""

mystring = "Hemingway"
myletter = "m"
try:
    myindex = mystring.index(myletter)
    print(myindex)
except:
    print("Not found")
    print

"""8. Find dialogue in your favorite book (containing quotes) and turn
    it into a string.
"""

quote1 = '“What’ll it be?” its voice hit Dave’s nerves like a truck.'
quote2 = '“Another beer, sir,” Dave said meekly. “If you please.”'
quote3 = '"Right away" said the little feller.'

"""9. Create the string "three three three" using concatenation, and
    then again using
    multiplication.
"""

mystring = "three "
print(mystring + mystring + mystring)
print(mystring * 3)

"""10. Slice the string "It was a bright cold day in April, and the
    clocks were striking thirteen." to only include the characters
    before the comma.
"""

mystring = (
    "It was a bright cold day in April, and the clocks were striking thirteen."
    )
myindex = mystring.index(",")
print(mystring[0:myindex])
