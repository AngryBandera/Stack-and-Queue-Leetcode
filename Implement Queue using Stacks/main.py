class Node:
    def __init__(self, data, next_ = None):
        self.data = data
        self.next = next_

class MyQueue:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        self.head = Node(x, self.head)

    def pop(self) -> int:
        head = self.head
        if head is None:
            raise ValueError
        if head.next is None:
            data = self.head.data
            self.head = None
            return data
        while head.next.next is not None:
            head = head.next
        data = head.next.data
        head.next = None
        return data


    def peek(self) -> int:
        head = self.head
        if self.head is None:
            return ValueError
        while head.next is not None:
            head = head.next
        data = head.data
        return data

    def empty(self) -> bool:
        return self.head is None
