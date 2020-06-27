"""1. Create a list of your favorite musicians.
"""

favoriteMusicians = ["Phil Lynott",
                     "Sam Cooke",
                     "Curtis Mayfeild"]
print(favoriteMusicians)

"""2. Create a list of tuples, with each tuple containing the longitude and latitude
       of somewhere you've lived or visited.
"""

visited = []
bahamas = (25.0343, 77.3963)
tromso = (69.6492, 18.9553)
visited.append(bahamas)
visited.append(tromso)
print(visited)

"""3. Create a dictionary that contains different attributes about you: height,
       favorite color, favorite author, etc.
"""

me = {"height": "92 inches",
      "favorite color": "yellow",
      "favorite author": "Groucho"}
print(me)

"""4. Write a program that lets the user ask your height, favorite color, or favorite
       author, and returns the result from the dictionary you created in the previous
       challenge.
"""

def ask_me():
    """
    Returns values from keys in 'me' dictionary.
    Input from user.
    """
    
    sorry = "I'm sorry to hear that!"
    
    height = input("Do you want to know my height? Y/N:").capitalize()
    if height != "":
        if height[0] == "Y":
            print(me["height"])
        else:
            print(sorry)
    else:
            print(sorry)
    color = input("Do you want to know my favorite color? Y/N:").capitalize()
    if color != "":
        if color[0] == "Y":
            print(me["favorite color"])
        else:
            print(sorry)
    else:
        print(sorry)
    author = input("Do you want to know my favorite author?: Y/N:").capitalize()
    if author != "":
        if author[0] == "Y":
            print(me["favorite author"])
        else:
            print(sorry)
    else:
        print(sorry)
    
ask_me()

"""5. Create a dictionary mapping your favorite musicians to a list of your favorite
       songs by them.
"""

music = {}
music[favoriteMusicians[0]] = "Dancin in the moonlight"
music[favoriteMusicians[1]] = "Don't fight the feeling"
music[favoriteMusicians[2]] = "Move on up"
print(music)

"""6. Lists, tuples, and dictionaries are just a few of the containers built into
       Python. Research Python sets (a type of container). When would you use a set?

 Sets - Common uses include membership testing, removing duplicates from a
   sequence, and computing mathematical operations such as intersection, union,
   difference, and symmetric difference.
"""

thisSet = {"apple", "banana", "cherry"}
print(thisSet)

# Loop through the set, and print the values
for x in thisSet:
  print(x)

# Check if value is present in the set
print("banana" in thisSet)
print("mango" in thisSet)

# Add items to a set, using the update() method, duplicate "apple"
thisSet.update(["apple", "orange", "mango", "grapes"])
print(thisSet)
