from queue import PriorityQueue

q = PriorityQueue()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

q.put((2, ListNode(2)))
q.put((2, ListNode(1)))
q.put((3, ListNode(3)))

while not q.empty():
    next_item = q.get()
    print(next_item)