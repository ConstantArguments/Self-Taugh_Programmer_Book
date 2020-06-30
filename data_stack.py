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

# Example

new_stack = Stack()

print(new_stack.is_empty())

for i in range(7):
    new_stack.push(i)
    print(new_stack.items)

print(new_stack.size())
print(new_stack.peek())
print(new_stack.items)

for i in range (7):
    new_stack.pop()
    print(new_stack.items)