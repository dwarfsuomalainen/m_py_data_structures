class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        new_node = ListNode(value)

        # If list is empty just point the header to the new node
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

    def pop(self):
        if not self._head: return None
        current_node = self._head
        self._tail = current_node
        previous_node = None
        if not current_node.next:
            self._head = None
            return current_node.data
        else:
            while current_node.next != None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            self._tail = previous_node
            data = current_node.data
            self._size -=1
            return data
    def pop(self):
        if not self._head: return None
        if self._head == self._tail:
            data = self._head.data
            self._head = self._tail = None
            self._size -= 1
            return data
        current_node = self._head
        previous_node = None
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        #data = current_node.value
        self._tail = previous_node
        previous_node.next = None
        self._size -= 1
        return current_node.data ### node to be removed with del() insisted in task

def main():
    mylist = SinglyLinkedList()
    for c in 'abc':
        mylist.append(c)
    val = mylist.pop()
    print(val, mylist)
main()