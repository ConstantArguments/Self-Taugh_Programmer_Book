class Queue:
    """First-in-first-out data structure (FIFO)."""
    def __init__(self):
        """Creates "queue" list."""
        self.items = []


    def is_empty(self):
        """Returns true if "queue" is empty."""
        return self.items == []


    def enqueue(self, item):
        """Addes item to "queue"."""
        self.items.insert(0, item)


    def dequeue(self):
        """Removes item from "queue"."""
        return self.items.pop()


    def size(self):
        """Returns int for length of "queue"."""
        return len(self.items)

# Example
new_queue = Queue()

print(new_queue.is_empty())

for i in range(7):
    new_queue.enqueue(i)
    print(new_queue.items)

print(new_queue.size())

for i in range(7):
    new_queue.dequeue() #note lack of argument.
    print(new_queue.items)