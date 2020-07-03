"""3. Create a regular expression that matches any word that starts with
    any character and is followed by two o's. Then use Python's
    re module to match "boo" and "loo" in the sentence:
    "The ghost that says boo haunts the loo."
"""

import re

my_string = "The ghost that says boo haunts the loo."
m = re.findall(".oo", my_string, re.IGNORECASE)
n = re.findall("[bl]oo", my_string, re.IGNORECASE)
o = re.findall("[bl]o*", my_string, re.IGNORECASE)
print(m)
print(n)
print(o)
