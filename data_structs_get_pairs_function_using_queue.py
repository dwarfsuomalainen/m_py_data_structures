
from data_structs_node_based_queue import Queue


def get_pairs(list_of_nums):
    #print(list)
    evens = Queue()
    odds = Queue()
    list_to_return = []
    for num in list_of_nums:
        if num % 2 == 0:
            evens.enqueue(num)
        else: odds.enqueue(num)
    #print(evens)
    #print(odds)
    while evens._size != 0 and odds._size != 0:
        list_to_return.append((evens.dequeue(),odds.dequeue()))
    #print(list_to_return)
    return list_to_return

'''def main():
    list_to_function = DoublyLinkedList()
    list_to_function.append(6)
    list_to_function.append(90)
    list_to_function.append(77)
    list_to_function.append(88)
    list_to_function.append(22)
    list_to_function.append(33)
    list_to_function.append(43)
    list_to_function.append(55)
    print(list_to_function)
    get_pairs(list_to_function)

main()'''
'''
def main():
    print(get_pairs([74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65]))
main()'''