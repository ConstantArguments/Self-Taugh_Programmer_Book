"""1. Reverse the string "Yesterday" using a stack.
"""

class Stack:
    """Data Structure first-in-last-out (FILO)."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Returns True if "stack" is empty."""
        return self.items == []

    def push(self, item):
        """Adds items to "stack"."""
        self.items.append(item)

    def pop(self):
        """Removes items from "stack"."""
        return self.items.pop()

    def peek(self):
        """Looks at top item in "stack", but does not remove it."""
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        """Returns Int for size of "stack"."""
        return len(self.items)

word = "Yesterday"
reverse_word = ""
word_stack = Stack()

for i in range(len(word)):
    word_stack.push(word[i])

for i in range(word_stack.size()):
    letter = word_stack.pop()
    reverse_word += letter

print(reverse_word)

"""2. Use a stack to create a new list with the following reversed: [1, 2, 3, 4, 5].
"""
my_list = [1, 2, 3, 4, 5]
my_list_stack = Stack()
reverse_list = []

for items in my_list:
    my_list_stack.push(items)

for i in range (my_list_stack.size()):
    num = my_list_stack.pop()
    reverse_list.append(num)

print(reverse_list)