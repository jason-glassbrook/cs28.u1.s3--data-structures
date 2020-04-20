import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList


class Stack:

    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        pass

    def pop(self):
        pass

    def len(self):
        return len(self)
