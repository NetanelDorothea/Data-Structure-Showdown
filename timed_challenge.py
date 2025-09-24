# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
"""
12. Count Items in Structure
Given a head reference, count the number of items stored.
Input: "head" → "node1" → "node2" → None
Output: 3
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_count(self):
        i = 0
        current = self.head
        s = ""
        while current:
            i += 1
            s = s + f"{current.value} → "
            current = current.next
        s = s + "None"
        print(s)
        return i

# Test your solution with multiple inputs and be sure to test edge cases (e.g. empty lists, wrong data type, etc.)

# Case 1: Normal list
data = ["head", "node1", "node2"]
lst = List()
for i in data:
    lst.add(i)
print("Count:", lst.print_count())  # Expected: "head → node1 → node2 → None", Count: 3

# Case 2: Empty list
empty_lst = List()
print("Count:", empty_lst.print_count())  # Expected: "None", Count: 0

# Case 3: Single element
single_lst = List()
single_lst.add("only_node")
print("Count:", single_lst.print_count())  # Expected: "only_node → None", Count: 1

# Case 4: Mixed data types
mixed_lst = List()
mixed_lst.add(10)
mixed_lst.add("hello")
mixed_lst.add(3.14)
print("Count:", mixed_lst.print_count())  # Expected: "10 → hello → 3.14 → None", Count: 3

# What structure you chose and why
# How the time limit shaped your decision
# What trade-offs or compromises you made under time pressure
#
# I chose for a linked list becuase this specific problem required to have a head reference. Linked lists consists of a head followed by nodes that are linked to other nodes in order.
# This way I could efficiently go through every node and count the amount of nodes. 
# Otherwise I would have chosen for a list to iterate through with a simple for loop since this would also work.
# Because I knew quite fast that I needed a linked list, I went for that. I knew the linked list wouldnt take too much time either because its pretty easy to create.
# Because of the time, I made sure I added the required methods for this specific problem, meaning no functions to delete or add to the front, only the essential methods.
# I also had no comments since this would take up valuable time.
# Another compromise I made, although it has nothing to do withh time pressure, was not searching for clues or answers online but doing everything from the top of my head. I believe that is also how I am supposed to do it in real interviews.  
