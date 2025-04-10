def binary_search_iterative(array, value):
    """
    Performs a binary search in the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    start_point = 0
    end_point = len(array) - 1

    mid = end_point // 2
    index = 0

    if array[mid] == value:
        return mid

    if value < array[mid] and mid >= start_point + 1:
        for i in range (start_point,mid):
            if array[i] == value:
                return i

    if value > array[mid] and mid <= end_point:
        #print(mid)
        #print(end_point)
        for i in range(mid,end_point + 1):
            if array[i] == value:
                return i
    return None

def interpolation_search(array, value):
    start_point = 0
    end_point = len(array) - 1

    mid = start_point + int((end_point - start_point) * ((value-array[start_point])/(array[end_point]-array[start_point])))
    index = 0

    if array[mid] == value:
        return mid

    if value < array[mid] and mid >= start_point + 1:
        for i in range (start_point,mid):
            if array[i] == value:
                return i

    if value > array[mid] and mid <= end_point - 1:
        #print(mid)
        #print(end_point)
        for i in range(mid,end_point + 1):
            if array[i] == value:
                return i
    return None

def main():
    array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
    print(binary_search_iterative(array, 0))
    print(binary_search_iterative(array, 98))
    print(binary_search_iterative(array, 29))
    print(binary_search_iterative(array, 100))
    print(binary_search_iterative(array, -1))
    print(binary_search_iterative(array, 44))
main()
'''def main():
    array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
    print(interpolation_search_iterative(array, 0))
    print(interpolation_search_iterative(array, 98))
    print(interpolation_search_iterative(array, 29))
    print(interpolation_search_iterative(array, 100))
    print(interpolation_search_iterative(array, -1))
    print(interpolation_search_iterative(array, 44))
main()'''