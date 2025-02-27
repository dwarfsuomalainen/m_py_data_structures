class ListNode:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedLisr:
    def __init__(self):
        self._head = None

    def append(self, value):
        node = ListNode(value, next=None)
        if self._head is None:
            self._head = node
        else:
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
