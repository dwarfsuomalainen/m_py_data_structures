class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
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
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def __iter__(self):
        self._iter_index = self._head
        return self

    def __next__(self):
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        """
        Return value at index
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise (ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        # Return the value
        return current_node.data

    def __setitem__(self, index, value):
        """
        set value at index k with val
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise (ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        # Set the value
        current_node.data = value

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value. This is the last node, so next is None,
        # but there can be already some node in the list, hence the prev value
        new_node = ListNode(value, next=None, prev=self._tail)

        # If list is empty, update head and tail pointers
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # In any other case, update tail node to point to the new element
            # and update tail pointer. The new node already points to its
            # previous element
            self._tail.next = new_node
            self._tail = new_node

        # update size
        self._size += 1

    def pop(self):
        """
        Removes the last node of the list

        Parameters: None

        Returns:
            The content of the removed node. If list is empty, returns None
        """
        # If list is empty, returns None
        if not self._size:
            return None

        # Locate previous_node (the node just before last node)
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # If node to remove is first node, then update head pointer
        if node_to_remove == self._tail:
            self._head = None
        else:
            # If not, update the pointer of the previous node
            previous_node.next = None  # It is now the last node

        # Update tail pointer
        self._tail = previous_node

        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del (node_to_remove)
        return value

    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index

        Parameters:
        - 'index': The position where to insert the new node
        - 'value': The value of the new node

        Returns: None
        """
        node_to_insert = ListNode(value)

        next_node = None
        prev_node = None
        counter = 0
        if index > self._size: raise ValueError

        if self._size == 0:
            self._head = node_to_insert
            self._tail = node_to_insert
            self._size += 1
            return
        if index == self._size:
            # print("tail")
            current_node = self._tail
            # print(current_node.data)
            node_to_insert.prev = current_node
            # print(node_to_insert.prev)
            current_node.next = node_to_insert
            # print(current_node.next)
            self._tail = node_to_insert
            # print(self._tail)
            self._size += 1
            return
        elif index == 0:
            current_node = self._head
            node_to_insert.next = current_node
            self._head = node_to_insert
            self._size += 1
            return
        else:
            current_node = self._head
            while counter < index:
                current_node = current_node.next
                counter += 1
            prev_node = current_node.prev
            node_to_insert.next = current_node
            current_node.prev = node_to_insert
            node_to_insert.prev = prev_node
            prev_node.next = node_to_insert
            self._size += 1
        return None

    def remove_by_value(self, value):
        """
        Remove first node with given value and return its position
        """
        # Find if there is a node with given value
        current_node = self._head
        index = 0
        while current_node and current_node.data != value:
            current_node = current_node.next
            index += 1

        # If value was not found, current_node is None
        if not current_node:
            return None

        previous_node = current_node.prev
        next_node = current_node.next

        # If node to remove is the first node, update head
        if previous_node is None:
            self._head = next_node
        else:
            # If not, update previous node
            previous_node.next = next_node

        # If node to remove is last node, update tail
        if next_node is None:
            self._tail = previous_node
        else:
            # If not, update next node
            next_node.prev = previous_node

        # Update size, remove the node and return its index
        self._size -= 1
        del (current_node)
        return index

    def contains(self, value):
        """
        Returns True if value if found in the list and False if not
        """
        for node_value in self:
            if value == node_value:
                return True
        return False

    def clear(self):
        """
        Clear the list
        """
        # Remove all nodes
        current_node = self._head
        while current_node:
            next = current_node.next
            del (current_node)
            current_node = next

        # Update pointers and size
        self._head = self._tail = None
        self._size = 0

    def remove(self, index):
        """
        Remove a new node from the position given by the index

        Parameters:
        - 'index': The position where to insert the new node

        Returns: The value of the node being removed
        """
        if self._size == 0:
            raise ValueError
            return

        if index > self._size: raise ValueError

        if index == 0:
            node_to_remove = self._head
            data = node_to_remove.data
            current_node = node_to_remove.next
            self._head = current_node
            del(node_to_remove)
            self._size -= 1
            return data
        if index == self._size - 1:
            #print(self._size -1 )
            node_to_remove = self._tail
            prev_node = node_to_remove.prev
            data = node_to_remove.data
            prev_node.next = None
            #print(self._tail)
            self._tail = prev_node
            del (node_to_remove)
            self._size -= 1
            return data
        else:
            counter = 0
            current_node = self._head
            prev_node = None
            while counter < index:
                prev_node = current_node
                current_node = current_node.next
                counter += 1
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node_to_remove = current_node
            data = node_to_remove.data
            del node_to_remove
            self._size -=1
            return data

# main to test out .remove() method for doubly linked list
'''def main():
    ''''''mylist = DoublyLinkedList()
    #for i in range(10, 51, 10):
    #    mylist.append(i)
    val = mylist.remove(0)
    print(val, mylist)''''''
    mylist = DoublyLinkedList()

    try:
        val = mylist.remove(0)
    except ValueError:
        print(mylist)
    except Error as e:
        print(f'Exception: {e}')
    else:
        print('No exception raised!')
main()'''

# main to test out .insert() method for doubly linked list
'''def main():
    mylist = DoublyLinkedList()
    for i in range(10, 51, 10):
        mylist.append(i)
    val = mylist.insert(5, 999)
    print(val, mylist)
main()'''