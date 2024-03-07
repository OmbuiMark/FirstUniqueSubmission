#code written in VS Code with Python 3.7.6

from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# FirstUnique class to track the first unique number in a data stream
class FirstUnique:
    def __init__(self, nums):
        # Initialize data structures
        self.unique_queue = deque()
        self.num_counts = defaultdict(int)
        self.unique_map = {}

        # Add initial numbers
        for num in nums:
            self.add(num)

    # Add a new number to the data stream
    def add(self, number):
        # Update count and handle unique/non-unique cases
        self.num_counts[number] += 1
        if self.num_counts[number] == 1:
            self.add_unique(number)
        elif self.num_counts[number] > 1:
            self.remove_unique(number)

    # Return the first unique number, or -1 if none
    def showFirstUnique(self):
        return self.unique_queue[0].val if self.unique_queue else -1

    # Helper method to add a unique number
    def add_unique(self, number):
        node = Node(number)
        self.unique_queue.append(node)
        self.unique_map[number] = node

    # Helper method to remove a non-unique number
    def remove_unique(self, number):
        if number in self.unique_map:
            self.remove_node(self.unique_map[number])
            del self.unique_map[number]

    # Helper method to remove a node from the linked list
    def remove_node(self, node):
        # Update prev and next pointers for adjacent nodes
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # Remove node from the queue
        if node == self.unique_queue[0]:
            self.unique_queue.popleft()
        elif node == self.unique_queue[-1]:
            self.unique_queue.pop()