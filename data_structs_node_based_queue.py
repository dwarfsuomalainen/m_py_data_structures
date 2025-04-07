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
    #LIFO repr
    '''def __repr__(self):
        current_node = self._last
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'''''
    # FIFO method
    def __repr__(self):
        current_node = self._first
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'
    # LIFO method
    '''def enqueue(self, data):
        node_to_add = ListNode(data, next = self._first, prev= None)
        if not self._first:
            self._first = self._last = node_to_add
        else:
            current_node = self._last
            current_node.prev = node_to_add
            node_to_add.next = current_node
            self._last = node_to_add
        self._size +=1'''
    # FIFo method
    def enqueue(self, data):
        node_to_add = ListNode(data, next = self._first, prev= None)
        if not self._first:
            self._first = self._last = node_to_add
        else:
            self._first.prev = node_to_add
            self._first = node_to_add
        self._size +=1

    def dequeue(self):
        if not self._size: return None

        node_to_remove = self._last
        prev_node = node_to_remove.prev

        if self._size == 1:
            self._first = self._last = None
        else:
            prev_node.next = None
            self._last = prev_node
        data = node_to_remove.data
        del node_to_remove
        self._size -= 1
        #print(data)
        return data


'''def main():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(queue)
main()'''

'''def main ():
    queue = Queue()
    queue.enqueue('A')
    print(queue)
    queue.enqueue('B')
    print(queue)
    queue.enqueue('C')
    print(queue)
    queue.enqueue('D')
    print(queue)
    queue.enqueue('D')
    print(queue)
    val = queue.dequeue()
    val = queue.dequeue()
    print(val, queue)
main()'''