class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        child_node_index = self._size - 1
        while child_node_index > 0:
            parent_index = (child_node_index - 1) // 2
            if self._heap[child_node_index] < self._heap[parent_index]:
                #print(self._heap[parent_index], "parent")
                #print(self._heap[child_node_index], "child")
                self._heap[parent_index], self._heap[child_node_index] = self._heap[child_node_index], self._heap[parent_index]
                child_node_index = parent_index
            else: break



def main():
    h = Heap()
    h._heap = [3, 6, 5, 9, 7, 8, 2]
    h._size = 7
    h._float()
    print(h._heap)
main()
