"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    data = set(product_ids)
    if len(product_ids) != len(data):
        return True
    return False 

data_1 = [10, 20, 30, 20, 40]
data_2 = [1, 2, 3, 4, 5]
print(f"Input: [10, 20, 30, 20, 40] is expected to output True. Terminal Output: {has_duplicates(data_1)}.")
print(f"Input: [1, 2, 3, 4, 5] is expected to output False. Terminal Output: {has_duplicates(data_2)}.")

#Write a 2–3 sentence comment justifying: 
# (1) Why this data structure fits the task and 
# (2) what operations are performed and their expected runtime
# The set is perfect for this problem because a it automatically removes duplicates which quickly reveals the list for duplicates. 
# The operations are creating a set from a list and comparing lenghts, which will have an overall linear runtime that scales efficiently.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_node = Node(task)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            print(f"{task} successfully added!")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"{task} successfully added!")

    def remove_oldest_task(self):
        if self.front is None:
            print("No tasks to remove.")
            return
        removed_task = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_task.value

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(f"Expected outcome: {task_queue.remove_oldest_task()} → \"Email follow-up\"") 

#Write a 2–3 sentence comment justifying: 
# (1) Why this data structure fits the task and 
# (2) what operations are performed and their expected runtime
# The queue is a perfect data structure because it contains the FiFo principal and keeps all items in order, which is ideal we need to delete taks by order from first to last.
# The operations are enqueue (add) and dequeue (remove), both of which have a constant runtime which is effecient for taskmanagent. 

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.n = set()

    def add(self, value):
        self.n.add(value)

    def get_unique_count(self):
        return len(self.n)

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(f"Expected outcome: {tracker.get_unique_count()} → 2")

#Write a 2–3 sentence comment justifying: 
# (1) Why this data structure fits the task and 
# (2) what operations are performed and their expected runtime
# The set is perfect for this problem because it automatically removes duplicates to easily track the unique values. 
# The operations are adding numbers to a set, and checking its length, both of which will have an average constant runtime.
