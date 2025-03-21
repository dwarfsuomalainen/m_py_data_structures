'''Write a method that finds a node that holds a certain value
Given a basic BST structure (included), add a _find() method to it, to search for values in the tree. The basic definition of the method is already included. Start from the root node and move to the appropriate nodes searching for the wanted value. The method should return the node that holds the value or None if the value is not found.

Notice that the Node object, when printed, prints some odd code. This is done on purpose to help checking on the exercises.'''


class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'

class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise(ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        #set current node and parent node
        current_node = self._root_node

        
        #iterate the tree
        if not current_node: return None
        while current_node:
            if current_node.data == data:
                return current_node
            #check if data smaller than node data, and reassign current node accordingly BST logic
            elif current_node.data > data:
                current_node = current_node._left_child
                #print(current_node)
            # check if data greater than node data, and reassign current node accordingly BST logic
            elif current_node.data < data:
                current_node = current_node._right_child
                #print(current_node)
        return None

    def find_minimum(self):
        #set current node and parent node
        current_node = self._root_node
        #print(current_node)
        #iterate the tree
        #if not current_node: return None
        while current_node:
            #print(current_node.data)
            if not current_node._left_child: return current_node
            else: current_node = current_node._left_child
        return current_node

    def find_maximum(self):

        current_node = self._root_node
        while current_node:
            #print(current_node.data)
            if not current_node._right_child: return current_node
            else: current_node = current_node._right_child
        return current_node


# main to test out ._find() method
'''def main():
    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    print(tree._find(35))
main()'''

#main to test out .find_minimum() method
def main():

    tree = Tree()
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(90)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    minimum = tree.find_minimum()
    maximum = tree.find_maximum()
    print(minimum, maximum)
main()


