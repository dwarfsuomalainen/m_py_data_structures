def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    if array[0] < array[1]:
        array[0], array[1] = array[1], array[0]
    print(array)
    while True:
        for i in range(1, len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

def main():
    array = [6, 8, 5, 1, 2]
    print(array)
    insertion_sort(array)
    print(array)
main()