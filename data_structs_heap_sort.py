from data_structs_sift_down_function import sift_down


def heap_sort(array):
    """
    Sort the array using the Heapsort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    n = len(array)

    for i in range((n - 2) // 2, -1, -1):
        sift_down(array, i, n - 1)

    for end in range(n - 1, 0, -1):
        array[0], array[end] = array[end], array[0]  # move max to end
        sift_down(array, 0, end - 1)


'''def sift_down(array, start, end):
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
            root_index = swap'''