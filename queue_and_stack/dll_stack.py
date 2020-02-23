from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size = len(self.storage)

    def pop(self):
        if self.size is not 0:
            old_head = self.storage.head
            self.storage.remove_from_head()
            self.size = len(self.storage)
            return old_head.value

    def len(self):
        return self.size
