class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class MyStack:

    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.empty():
            raise ValueError('Stack is empty')
        item = self.head.item
        self.head = self.head.next
        return item

    def top(self):
        if self.empty():
            raise ValueError('Stack is empty')
        else:
            return self.head.item
