from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size = len(self.storage)

    def dequeue(self):
        if self.size is not 0:
            old_node = self.storage.tail
            self.storage.remove_from_tail()
            self.size = len(self.storage)
            return old_node.value

    def len(self):
        return len(self.storage)
