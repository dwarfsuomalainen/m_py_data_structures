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

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """
        parent_val = self._heap[0]
        parent = 0
        #condition checks if parent has left child ()
        while 2 * parent + 1 < self._size:
            left = 2 * parent + 1
            right = 2 * parent + 2
            smallest = left
            if right < self._size and self._heap[right] < self._heap[left]:
                smallest = right
            if self._heap[parent] > self._heap[smallest]:
                self._heap[parent],self._heap[smallest] = self._heap[smallest],self._heap[parent]
                parent = smallest
            else: break

def main():
    h = Heap()
    h._heap = [8, 6, 5, 9, 7]
    h._size = 5
    h._sink()
    print(h._heap)
main()