<h1 align="center">
    <br>
    Algorithms and Data Structures: A Simple Guide
    </br>
</h1>

<p align="center">
    <a href="#introduction-to-data-structures">Introduction to Data Structures</a> •
    <a href="#trees">Trees</a> •
    <a href="#graphs">Graphs</a> •
    <a href="#introduction-to-algorithms">Introduction to Algorithms</a> •
    <a href="#sorting-algorithms">Sorting Algorithms</a> •
    <a href="#search-algorithms">Search Algorithms</a> •
    <a href="#dynamic-programming">Dynamic Programming</a> •
    <a href="#graph-algorithms">Greedy Algorithms</a> •
</p>

## Introduction to Data Structures

<p align="center">
    <a href="#basics">Basics</a> •
    <a href="#stacks">Stacks</a> •
    <a href="#queues">Queues</a> •
    <a href="#linked-list">Linked List</a> •
    <a href="#hash-tables">Hash Tables</a> •
    <a href="#heaps">Heaps</a>
</p>

### Basics

- **Data Structures** are storage units used to store and organize data - done in a way so that data can be accessed and updated efficiently
- Types of data structures - **Linear** and **Non-Linear**
- **Linear Data Structures** -

  - Elements are arranged in sequential order
  - Easier to implement for less complex use cases
  - **Arrays**: Elements are arranged in continuous memory - all the elements that can be stored in an array are of the same type.
  - **Stacks**: Elements stored in LIFO (Last In First Out)
  - **Queues**: Elements stores in FIFO (First In First Out)
  - **Linked List**: Elements connected through a series of nodes, where each node contains item and address to the next node

- **Non-Linear Data Structures** -
  - Non-sequential
  - Arranged in hierarchical order - one element connected to one or multiple elements
  - **Graphs**: Each node is called a vertex and vertices are connected to each other via edges.
  - **Trees**: Similar to graphs, but there can only be one edge between two vertices.

|       Linear Data Structures        |       Non-Linear Data Structures        |
| :---------------------------------: | :-------------------------------------: |
|             Sequential              |             Non-Sequential              |
|  All items present in single layer  |           In multiple layers            |
|      Traversed in a single run      |         Requires multiple runs          |
|   Inefficient memory utilization    | Relatively efficient memory utilization |
| Time complexity increases with data |    Time complexity remains the same     |

### Stacks

- Linear Data Structure that follows the principle of LIFO - Last in First Out - last element added to the stack is the first one to be removed.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Stack.png)

- **KEY CONCEPTS**:
    - **PUSH**: Add an element to the top of the stack
    - **POP**: Remove an element from the top of the stack
    - **IsEmpty**: Check if the stack is empty
    -**PEEK**: Check the value of the top element in the stack without removing it
- Applications: Undo / Redo in text editors, Backtracking problems (mazes), String reversals, compilers, browser (saving previously visited URLs)

- Time Complexity of **Stack**:
    - Best Case: O(1)
    - Average Case: O(1)
    - Worst Case: O(N), where N is the number of items in the stack.
    - Space Complexity: O(1)

### Queues

- Linear data structure that follows **FIFO - First In First Out** rule - the item that goes in first comes out first

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Simple_queue.png)

- **KEY CONCEPTS**:

  - **ENQUEUE**: Add an element to the end of the queue
  - **DEQUEUE**: Remove and return an element from the front of the queue
  - **PEEK**: Check the value of the first element in the queue without removing it
  - **IsEmpty**: Check if the queue is empty
  - **IsFull**: Check if the queue is full
  - **FRONT**: The end of the queue from which the elements are removed
  - **REAR**: The end of the queue from which the elements are added

- Applications: CPU Scheduling, File System buffers, interrupts in real time systems

- Types of Queues:

  - **Simple Queue**

    - Standard FIFO queue
    - Space: O(n)
    - Time Complexities (Enqueue, Dequeue, Peek): O(1)

  - **Circular Queue**

    ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/cirq.jpg)

    - Like regular queue, but the last element is connected to the first element, solving the limitation of non-usable empty space.
    - Works in the process of circular increment - modulo division with the queue size
    - Same initialization of FRONT and REAR pointer variables
    - **ENQUEUE**: FRONT is set to 0, REAR is circularly incremented by 1, if it reaches the end, it would be at the start of the queue, then add to the position pointed to by REAR.
    - **DEQUEUE**: Return value pointed by FRONT, circularly increase FRONT by 1, for last element, reset the FRONT and REAR values to -1
    - IsFull conditions: FRONT == 0 && REAR == SIZE - 1, FRONT = REAR + 1
    - Space: O(n)
    - Time Complexities (Enqueue, Dequeue, Peek): O(1)

  - **Priority Queue**

    - Each element is linked with a priority value - served on the basis of their priority.
    - If elements have the same priority, they are then served according to their order in the queue.
    - Implemented using binary heaps (heapq in Python).
    - Does not follow FIFO - follows rule of priority
    - Space: O(n)
    - Time Complexities (Enqueue, Dequeue, Peek): O(logn), O(1)

  - **Deque (Double Ended Queues)**
    ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/double-ended-queue.png)
    - Flexible, allowing addition and removal from both ends.
    - Space: O(n)
    - Time Complexities (Enqueue, Dequeue, Peek): O(1)

### Linked List

- Linear data structure that includes a series of connected nodes - each node stores the data and the address of the next node.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/linked-list.png)

- **HEAD**: Address of the first node
- Last node identified as the node that points to its next portion as NULL
- Types of Linked Lists: **Singly**, **Doubly**, **Circular**
- The power of linked list comes from the ability to break the chain and rejoin it. Doing something similar in an array would have required shifting the positions of all the subsequent elements.
- Space Complexity: O(n)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/linked-list-complexity.png)

- Applications - Dynamic memory allocation, stacks and queues, hash tables
- Linked List operations:

  - **Traversal**: Access each element of the linked list
  - **Insertion**: Add a new element to the linked list
  - **Deletion**: Removes the existing elements from the linked list
  - **Search**: Find a node in the linked list
  - **Sort**: Sort the nodes of a linked list

- **Doubly Linked List**: Add a pointer to the previous node, therefore can traverse either direction - forward or backward.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/DLL.png)

- **Circular Linked List**: Last element is linked to the first element, forming a loop. This can be both a doubly linked list or a singly linked list.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/CLL.png)

### Hash Tables

- Data structure that stores data in key-value pairs -
  - **Key**: Unique integer that is used for indexing the values
  - **Value**: Data associated with the Keys
- In a **hash table**, the new index is processed using keys, then the element corresponding to that key is stored in the index - **Hashing**.
- **Hashing** is a technique of mapping a large set of arbitrary data to tabular indexes using a hashing function. It allows lookups, updating and retrieval operation to occur in a constant time - O(1), that is it is not dependent on the size of the data
- Let k = key and h(x) = hashing function. h(k) will give us a new index to store the element associated with key k.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/hash_table.png)

- **Hash Collision** - When the hash function generates the same index for multiple keys. This can be resolved by -

  - Collision resolution by **chaining**:
    - If the hash function produces the same index for multiple elements, these elements are stored in the same index using a doubly linked list.
    - If x is the index for multiple elements, then it contains a pointer pointing to the head of the list. If there are no elements, x contains NIL.
  - **Open Addressing**: **Linear/Quadratic Probing** and **Double Hashing**:
    - **Open addressing** does not store multiple elements into the same slot - each slot is either filled with a single key or left NIL.
    - Technique 1: **Linear Probing**:
      - Collision is resolved by checking the next slot.
      - h(k, i) = (h′(k) + i) mod m; i is the set of index values and h'(k) is the new hash function.
      - Value of i is incremented linearly.
      - Problem: Cluster of adjacent slots filled - all must be traversed when inserting a new element.
    - Technique 2: **Quadratic Probing**:
      - Spacing between the slots is increased
      - h(k, i) = (h′(k) + c1i + c2i<sup>2</sup>) mod m
      - c1 and c2 are positive auxiliary constants
    - Technique 3: **Double Hashing**:
      - If a collision occurs after applying a hash function h(k), then another hash function is calculated for finding the next slot
      - h(k, i) = (h1(k) + ih2(k)) mod m

- Good Hash Functions: May not prevent collisions but can reduce the number of collisions.
  - Division Method:
    - If k is a key and m is the size of the hash table, the hash function h() is calculated as h(k) = k mod m
    - The value of m must not be the powers of 2 - will always get lower order p bits.
  - Multiplication Method:
    - h(k) = ⌊m(kA mod 1)⌋
    - kA mod 1 gives the fractional part kA
    - ⌊ ⌋ gives the floor value
    - A is any constant. The value of A lies between 0 and 1. But, an optimal choice will be ≈ (√5-1)/2 (Knuth)
  - Universal Hashing: hash function is chosen at random independent of keys