def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure

    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node

    Returns: None
    """
    root_index = start
    while 2 * root_index + 1 <= end:
        child = 2 * root_index + 1  # left child
        swap = root_index

        if array[child] > array[swap]:
            swap = child

        if child + 1 <= end and array[child + 1] > array[swap]:
            swap = child + 1

        if swap == root_index:
            return
        else:
            array[root_index], array[swap] = array[swap], array[root_index]
            root_index = swap

'''def _sink(self):
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
        else: break'''