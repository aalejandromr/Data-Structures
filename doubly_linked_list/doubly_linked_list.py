"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # Add to empty DLL
        if self.head == None and self.tail is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        # Add to DLL with 1 element
        elif self.head == self.tail:
            current_head = self.head
            node = ListNode(value, None, current_head)
            self.head = node
        #General
        else:
            current_head = self.head
            node = ListNode(value, None, current_head)
            self.head.prev = node
            self.head = node
        self.length += 1



    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value


    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # empty DLL
        if self.head is None and self.tail is None:
            node = ListNode(value, None, None)
            self.head = node
            self.tail = node
        # general
        else:
            current_tail = self.tail
            node = ListNode(value, current_tail, None)
            self.tail.next = node
            self.tail = node

        self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        if node is not self.head:
            self.delete(node)
            self.add_to_head(value)


    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        if node is not self.tail:
            self.delete(node)
            self.add_to_tail(value)


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        # If empty
        if not self.head and not self.tail:
            return
        # If head and tail
        elif node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        # If head
        elif node is self.head:
            # update the head ref
            self.head = self.head.next
            node.delete()
        # If tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        # else
        else:
            node.delete()


    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value