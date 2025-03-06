
---

# Data Structures and Methods  

## Description  
This project implements fundamental data structures and their associated methods in Python. The current focus is on **Arrays** and **Linked Lists**, with additional structures and algorithms in progress.  

## Implemented Data Structures and Methods  

### Array  
```python
from data_structs_array_methods import IntArray  

arr = IntArray()  
arr.append(10)  
arr.append(20)  
arr.insert(1, 15)  # Inserts 15 at index 1  
arr.remove(0)  # Removes element at index 0  

index = arr.search(15)  # Returns index of element 15  

print(arr)  # Example Output: IntArray (2 elements): [15, 20]
```

### Singly Linked List  
```python
from data_structs_singly_linked_list_pop_method import SinglyLinkedList  

sll = SinglyLinkedList()  
sll.append(10)  
sll.append(20)  
sll.append(30)  

popped_value = sll.pop()  # Removes and returns 30  
print(popped_value)  # Output: 30  
print(sll)  # Output: <SinglyLinkedList: [10, 20]>
```

### Singly Linked List with Tail  
```python
from data_struct_singly_linked_list_tail_remove_pop_method import SinglyLinkedList  

sll_tail = SinglyLinkedList()  
sll_tail.append(10)  
sll_tail.append(20)  
sll_tail.append(30)  

sll_tail.remove(1)  # Removes element at index 1 (20)  
popped_value = sll_tail.pop()  # Removes and returns 30  

print(popped_value)  # Output: 30  
print(sll_tail)  # Output: <SinglyLinkedList (1 element): [10]>
```

### Doubly Linked List  
```python
from data_structs_doubly_linked_list_remove_insert_method import DoublyLinkedList  

dll = DoublyLinkedList()  
dll.append(10)  
dll.append(20)  
dll.append(30)  

dll.insert(1, 15)  # Inserts 15 at index 1  
dll.remove(2)  # Removes element at index 2 (30)  

print(dll)  # Output: <DoublyLinkedList (2 elements): [10, 15]>
```

## Upcoming Implementations  
These structures and algorithms are planned for future development:  

### Stacks and Queues  
- **Stack**: `push()`, `pop()`, `peek()`, `is_empty()`  
- **Queue**: `enqueue()`, `dequeue()`, `peek()`, `is_empty()`  

### Trees  
- **Binary Search Tree (BST)**: `insert()`, `remove()`, `search()`, `traverse()`  
- **AVL Tree**: `insert()`, `delete()`, `balance()`  
- **Trie**: `insert()`, `search()`, `delete()`  

### Hashing  
- **Hash Table**: `insert()`, `remove()`, `search()`, `collision_handling()`  

### Graphs  
- **Graph Representation**: Adjacency list and matrix  
- **Graph Traversal**: `BFS()`, `DFS()`  
- **Shortest Path Algorithms**: `Dijkstra()`, `Floyd-Warshall()`  

### Priority Queues and Heaps  
- **Min Heap**: `insert()`, `remove_min()`, `heapify()`  
- **Max Heap**: `insert()`, `remove_max()`  

### Searching  
- **Linear Search**  
- **Binary Search**  
- **Ternary Search**  

### Sorting  
- **Bubble Sort**  
- **Selection Sort**  
- **Insertion Sort**  
- **Merge Sort**  
- **Quick Sort**  
- **Heap Sort**  

### Algorithms  
- **Recursion and Backtracking**  
- **Dynamic Programming** (e.g., `Fibonacci`, `Knapsack Problem`)  
- **Greedy Algorithms** (e.g., `Activity Selection`, `Huffman Coding`)  
- **Divide and Conquer**  

---

