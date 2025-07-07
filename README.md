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