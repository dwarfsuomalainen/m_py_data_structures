class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue():
    def __init__(self):
        self._InboundStack = ListNode()
        self._OutboundStack = ListNode()
        self._size = 0

    def __repr__(self):
        return

    def enqueue(self, data):

        return

    def dequeue(self):

        return