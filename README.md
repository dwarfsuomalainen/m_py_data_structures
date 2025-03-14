# Data Structures and Methods  

## Description  
This project implements fundamental data structures and their associated methods in Python. The current focus is on **Arrays**, **Linked Lists**, **Stacks**, and **Queues**, with additional structures and algorithms in progress.  

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

### Stacks  
```python
from data_structs_stacks_push_pop_methods import Stack  

stack = Stack()  
stack.push(10)  
stack.push(20)  
stack.push(30)  

popped_value = stack.pop()  # Removes and returns 30  
print(popped_value)  # Output: 30  
print(stack)  # Output: <Stack (2 elements): [20, 10]>
```

### Queues  

#### **Node-Based Queue**  
```python
from data_structs_node_based_queue import Queue  

queue = Queue()  
queue.enqueue('A')  
queue.enqueue('B')  
queue.enqueue('C')  

print(queue)  # Output: <Queue (3 elements): [A, B, C]>  

val = queue.dequeue()  
print(val, queue)  # Output: A <Queue (2 elements): [B, C]>  
```

#### **Stack-Based Queue**  
Implemented using two stacks: an **inbound stack** (for enqueueing elements) and an **outbound stack** (for dequeuing elements).  

```python
from data_struct_stack_based_queue import StackBasedQueue  

queue = StackBasedQueue()  
queue.enqueue('A')  
queue.enqueue('B')  
queue.enqueue('C')  

print(queue)  # Output: <StackBasedQueue (3 elements): [A, B, C]>  

val = queue.dequeue()  
print(val, queue)  # Output: A <StackBasedQueue (2 elements): [B, C]>  
```

### **Bracket Balance Checker**  
```python
from brackets_balance_function_stacks import check_balance  

check_balance("a(b)c[d]e{f}g")  # Output: Ok - 3  
check_balance("a(b)c[)d]e{f}g")  # Output: Match error at position 6  
```

### **Pairing Function Using Queue**  
```python
from data_structs_get_pairs_function_using_queue import get_pairs  

pairs = get_pairs([74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65])  
print(pairs)  # Example Output: [(74, 21), (18, 71), (22, 77), ...]  
```

## Upcoming Implementations  
These structures and algorithms are planned for future development:  

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

