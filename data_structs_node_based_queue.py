import data_structs_doubly_linked_list_remove_insert_method
class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue():
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def __repr__(self):
        return

    def enqueue(self, data):
        node_to_add = ListNode(data, next = self._first, prev= None)
        if not self._first:
            self._first = self._last = node_to_add
        else:
            self._last.prev = node_to_add
            self._last = node_to_add
        self._size +=1

    def dequeue(self):


        self._size -= 1
        return


def main():
    queue = Queue()
    queue.enqueue('A')
    print(queue)
main()