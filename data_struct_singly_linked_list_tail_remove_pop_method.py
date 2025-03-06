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
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

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

    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index

        Parameters:
        - 'index': The position where to insert the new node
        - 'value': The value of the new node

        Returns: None
        """
        # Check if index is inside bounds
        if index < 0 or index > self._size:
            raise (ValueError('Index out of bounds'))

        # Prepare some variables to make the necessary changes
        # The new node will be inserted between previous_node and next_node
        previous_node = None
        next_node = self._head
        # Move to the given index and update pointer variables
        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        # Create new node. It's next pointer points to next node or None
        new_node = ListNode(value, next_node)

        # If insert at front, update head
        if previous_node is None:
            self._head = new_node
        else:
            # If not, update previous node
            previous_node.next = new_node

        # If insert at the end, update tail
        if previous_node == self._tail:
            self._tail = new_node

        # Update list size
        self._size += 1

    def remove(self, index):
        """
        Remove a new node from the position given by the index

        Parameters:
        - 'index': The position where to insert the new node

        Returns: The value of the node being removed
        """
        if index > self._size: raise ValueError
        count = 0
        current_node = self._head
        previous_node = None
        next_to_removed = None
        if index == 0:
            next_to_removed = current_node.next
            data = current_node.data
            self._head = next_to_removed
            self._size -= 1
            del(current_node)
            return data
        else:
            while count < index:
                previous_node = current_node
                current_node = current_node.next
                next_to_removed = current_node.next
                count += 1
        data = current_node.data
        previous_node.next = next_to_removed
        self._size -= 1
        del(current_node)
        return data

# main to test out .remove() method for singly linked list with tail
'''def main():
    mylist = SinglyLinkedList()

    for i in range(1, 6):
        mylist.append(i * 10)
    val = mylist.remove(2)
    print(val, mylist)
main()'''
# main to test out .pop() method for singly linked list with tail
'''def main():
    mylist = SinglyLinkedList()
    for c in 'abc':
        mylist.append(c)
    val = mylist.pop()
    print(val, mylist)
main()'''