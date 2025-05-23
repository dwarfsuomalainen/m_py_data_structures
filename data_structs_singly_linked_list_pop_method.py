class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
    def pop(self):
        if not self._head: return None
        current_node = self._head
        previous_node = None
        if not current_node.next:
            self._head = None
            return current_node.data
        else:
            while current_node.next != None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            data = current_node.data
            return data

# main to test out .pop() method for singly linked list
'''def main():
    list = SinglyLinkedList()
    for i in 'abc':
        list.append(i)
    val = list.pop()
    print(val, list)
main()'''