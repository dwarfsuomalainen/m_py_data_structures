# Data Structures and Methods

## Description
This project implements fundamental data structures and their associated methods in Python. It includes complete implementations for **Arrays**, **Linked Lists**, **Stacks**, **Queues**, **Graphs**, **Trees**, **Heaps**, **Sorting**, **Hashing**, and **Searching**.

## Implemented Data Structures and Methods

### Array
```python
from data_structs_array_methods import IntArray

arr = IntArray()
arr.append(10)
arr.append(20)
arr.insert(1, 15)
arr.remove(0)

index = arr.search(15)
print(arr)
```

### Singly Linked List
```python
from data_structs_singly_linked_list_pop_method import SinglyLinkedList

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)

popped_value = sll.pop()
print(popped_value)
print(sll)
```

### Singly Linked List with Tail
```python
from data_struct_singly_linked_list_tail_remove_pop_method import SinglyLinkedList

sll_tail = SinglyLinkedList()
sll_tail.append(10)
sll_tail.append(20)
sll_tail.append(30)

sll_tail.remove(1)
popped_value = sll_tail.pop()

print(popped_value)
print(sll_tail)
```

### Doubly Linked List
```python
from data_structs_doubly_linked_list_remove_insert_method import DoublyLinkedList

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

dll.insert(1, 15)
dll.remove(2)

print(dll)
```

### Stacks
```python
from data_structs_stacks_push_pop_methods import Stack

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

popped_value = stack.pop()
print(popped_value)
print(stack)
```

### Queues
#### Node-Based Queue
```python
from data_structs_node_based_queue import Queue

queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')

print(queue)
val = queue.dequeue()
print(val, queue)
```

#### Stack-Based Queue
```python
from data_struct_stack_based_queue import StackBasedQueue

queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')

print(queue)
val = queue.dequeue()
print(val, queue)
```

### Bracket Balance Checker
```python
from brackets_balance_function_stacks import check_balance

check_balance("a(b)c[d]e{f}g")
check_balance("a(b)c[)d]e{f}g")
```

### Pairing Function Using Queue
```python
from data_structs_get_pairs_function_using_queue import get_pairs

pairs = get_pairs([74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65])
print(pairs)
```

### Searching
```python
from data_structs_iterative_binary_search_sorted_array import binary_search_iterative

array = [1, 3, 5, 7, 9, 11]
print(binary_search_iterative(array, 5))  # Output: Index of 5
```

### Graphs (DFS & BFS)
```python
from data_structs_graphs_DFS_BFS import Graph

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

print(g.BFS('A'))
print(g.DFS('A'))
```

### Trees
```python
from data_structs_trees_find_method import Tree

t = Tree()
t.insert(10)
t.insert(5)
t.insert(15)

print(t.find(15))
```

### Heaps
```python
from data_struct_heap_sink_method import Heap

h = Heap()
h.insert(10)
h.insert(5)
h.insert(20)

print(h.pop())  # Output: 5 if min-heap
```

### Heapsort
```python
from data_structs_heap_sort import heap_sort

arr = [6, 1, 5, 8, 2]
heap_sort(arr)
print(arr)  # Output: [1, 2, 5, 6, 8]
```

### Sift Down (Heap helper)
```python
from data_structs_sift_down_function import sift_down

arr = [6, 1, 5, 8, 2]
sift_down(arr, 1, 4)
print(arr)  # Output: [6, 8, 5, 1, 2]
```

### Insertion Sort
```python
from data_structs_insertion_sort_algorithm import insertion_sort

arr = [5, 2, 4, 6, 1, 3]
insertion_sort(arr)
print(arr)
```

### Hashing (with linear probing)
```python
from data_structs_hashing_find_free_put import HashTable

ht = HashTable(size=10)
ht.put('apple', 1)
ht.put('banana', 2)
ht.put('orange', 3)

print(ht.get('banana'))  # Output: 2
print(ht.get('grape'))   # Output: None
```

## Upcoming Implementations
- Advanced Tree Structures (AVL, Trie)
- Additional Sorting Algorithms (Merge, Quick, Bubble, etc.)
- Advanced Graph Algorithms (Dijkstra, Floyd-Warshall)
- Algorithmic Paradigms (Greedy, DP, Divide and Conquer)


