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

  - Collision resolution by **Separate chaining**:
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/hash_table_collision_chaining.png)
    - If the hash function produces the same index for multiple elements, these elements are stored in the same index using a doubly linked list.
    - If x is the index for multiple elements, then it contains a pointer pointing to the head of the list. If there are no elements, x contains NIL.
  - **Open Addressing**: **Linear/Quadratic Probing** and **Double Hashing**:
    - **Open addressing** does not store multiple elements into the same slot - each slot is either filled with a single key or left NIL.
    - Technique 1: **Linear Probing**:
      - Collision is resolved by checking the next slot.
      - h<sub>i</sub>(X) = (Hash(X) + i) mod HashTableSize; i is the set of index values and Hash(X) is the new hash function.
      - Value of i is incremented linearly.
      - Problem: Cluster of adjacent slots filled - all must be traversed when inserting a new element.
    - Technique 2: **Quadratic Probing**:
      - Spacing between the slots is increased
      - h<sub>i</sub>(X) = (Hash(X) + i<sup>2</sup>) mod HashTableSize
    - Technique 3: **Double Hashing**:
      - If a collision occurs after applying a hash function Hash(X), then another hash function is calculated for finding the next slot
      - h<sub>i</sub>(X) = (Hash(X) + i*Hash<sub>2</sub>(X)) mod HashTableSize

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

## Trees

<p align="center">
    <a href="#introduction-to-trees">Introduction to Trees</a> •
    <a href="#binary-tree">Binary Tree</a> •
    <a href="#binary-search-tree">Binary Search Tree</a> •
    <a href="#avl-tree">AVL Tree</a> •
    <a href="#red-black-tree">Red Black Tree</a>
    <a href="#binary-heap">Binary Heap</a>
</p>

### Introduction to Trees

- A **non-linear hierarchical** data structure that consists of nodes connected via edges.
- For linear data structures, time complexity increases with data size - trees allow quicker and easier access.
- **Node**: An entity that contains a key or value and pointers to its child nodes. The last nodes of each path are known as leaf/external nodes - no link to child node. Nodes with child nodes - internal nodes.
- **Edge**: Link between any 2 nodes.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/node-edge.png)

- **Root**: topmost node of a tree.
- **Height (Node)**: Number of edges from the node to the deepest leaf (longest path from the node to the leaf node)
- **Depth (Node)**: Number of edges from the root to the node.
- **Height (Tree)**: Height of the root node.
- **Degree of a Node**: Total number of branches of that node
- **Forest**: Collection of disjoint trees - by cutting the root of a tree.
- **Tree traversal**: visiting every node in the tree.
- Use traversal methods that take into account the hierarchical structure of the tree.
- Every tree is a combination of a node carrying data and 2 subtrees.
- Types of Traversal:

  - **Inorder**: Visit all the nodes in the left subtree, root node then all the nodes in the right subtree.

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/in-order-traversal.gif)

  - **Preorder**: Visit root node, visit all the nodes in the left subtree, visit all the nodes in the right subtree.

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/pre-order-traversal.gif)

  - **Postorder**: Visit all the nodes in the left subtree, visit all the nodes in the right subtree, visit the root node.

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/post-order-traversal.gif)

### Binary Tree
- Tree data structure in which each parent node can have at most 2 children. Each node contains - data item, address of left child, address of right child.
- **Full Binary Tree**:

  - Every parent/internal node has either 2 or no children nodes.

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/full-binary-tree.png)

  - Also known as a proper binary tree
  - Let i = number of internal nodes | n = total number of nodes | l = number of leaves | λ = number of levels
  - Number of leaves = i + 1
  - n = 2i + 1
  - l = (n + 1) / 2
  - i = l – 1
  - l is at most 2<sup>λ</sup> - 1

- **Perfect Binary Tree**:

  - Every internal node has exactly 2 child nodes and all the leaf nodes are at the same level.

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/perfect-binary-tree.png)

  - All internal nodes have a degree of 2 (2 branches)
  - If a single node has no children, it is a perfect binary tree of height h = 0
  - If a node has h > 0, it is a perfect binary tree if both of its subtrees are of height h - 1 and are non-overlapping

- **Complete Binary Tree**:

  - All levels are completely filled except possibly the lowest one, which is filled from the left.
  - Similar to full binary trees except -
    1. All the leaf elements must lean towards the left.
    2. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/cb1.png)

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/cb2.png)

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/cb3.png)

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/cb4.png)

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/cb5.png)

  - We can use this tree to find the children and parent of any node

- **Degenerate / Pathological Tree** - A tree having a single child either left or right

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/dgen.png)

- **Skewed Binary Tree** - A pathological/degenerate tree in which the tree is either dominated by the left nodes or the right nodes.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/skew.png)

- **Balanced Binary Tree**:
  - Binary tree in which the height of the left and right subtree of any node differ by not more than 1.
    - difference between the left and the right subtree for any node is not more than one
    - the left subtree is balanced
    - the right subtree is balanced

### Binary Search Tree

- Quickly allows us to maintain a sorted list of numbers
- It has a maximum of 2 child nodes and can search for a number in **O(log(n))** time.
- How is binary search tree different from a binary tree -
  1. All nodes on the left subtree are lesser than the root node
  2. All nodes on the right subtree are greater than the root node
  3. Both subtrees of each node are also BSTs

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/bst.png)

- The binary tree on the right isn't a binary search tree because the right subtree of the node "3" contains a value smaller than it.
- **Operations**:
  - **SEARCH**: If the value is below the root, we can say for sure that the value is not in the right subtree; we need to only search in the left subtree and if the value is above the root, we can say for sure that the value is not in the left subtree; we need to only search in the right subtree. If the value is found in any of the subtrees, it is propagated up so that in the end it is returned, otherwise null is returned.
  - **INSERT**: Inserting a value in the correct position is similar to searching. We keep going to either right subtree or left subtree depending on the value and when we reach a point left or right subtree is null, we put the new node there.
  - **DELETION**:
    - **CASE 1**: The node to be deleted is the leaf node - simply delete the node from the tree
    - **CASE 2**: The node to be deleted has a single child node - replace that node with its child node, remove the child node from its original position
    - **CASE 3**: The node to be deleted has two children - get the inorder successor of that node, replace the node with the inorder successor, remove the inorder successor from its original position
- **Best Case Time Complexity**: **O(log(n))**
- **Worst Case Time Complexity**: **O(n)**
- Space Complexity: O(n)

### AVL Tree

- An **AVL tree** defined as a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees for any node cannot be more than one.
- Balance Factor = left subtree height - right subtree height. For a Balanced Tree(for every node): -1 ≤ Balance Factor ≤ 1

- **Example of an AVL Tree**:
  - The balance factors for different nodes are: 12 : +1, 8 : +1, 18 : +1, 5 : +1, 11 : 0, 17 : 0 and 4 : 0. Since all differences are lies between -1 to +1, so the tree is an **AVL tree**.
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/AVL-Tree_true.png)

- **Example of a BST which is not an AVL Tree**:
  - The Below Tree is not an AVL Tree as the balance factor for nodes 8, 4 and 7 is more than 1.
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/AVL-Tree_false.png.png)

- **Important Points about AVL Tree**:
  - Rotations: rotations are designed to restore balance in O(1) time while ensuring the overall time complexity remains O(log n). AVL Trees use four types of rotations to rebalance themselves after insertions and deletions:
    - **Left-Left (LL) Rotation**
    - **Right-Right (RR) Rotation**
    - **Left-Right (LR) Rotation**
    - **Right-Left (RL) Rotation**
  - **Insertion and Deletion**:
    While insertion is followed by upward traversals to check balance and apply rotations, deletion can be more complex due to multiple rotations possibly being required. **AVL Trees** may require multiple rebalancing steps during deletion.

- **Operations on an AVL Tree**:
  - **Searching**: It is same as normal Binary Search Tree (BST) as an **AVL Tree** is always a BST. So we can use the same implementation as BST. The advantage here is time complexity is O(log n)
  - **Insertion**: It does rotations along with normal BST insertion to make sure that the balance factor of the impacted nodes is less than or equal to 1 after insertion
  -**Deletion**: It also does rotations along with normal BST deletion to make sure that the balance factor of the impacted nodes is less than or equal to 1 after deletion.

- **Rotating the subtrees** (Used in Insertion and Deletion)

An **AVL tree** may rotate in one of the following four ways to keep itself balanced while making sure that the BST properties are maintained.

1. **Left-Left Rotation**:
  - Occurs when a node is inserted into the left subtree of the left child, causing the balance factor to become greater than +1.
  - Fix: Perform a single right rotation.
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/LLR_AVL.png)

2. **Right-Right Rotation**:
  - Occurs when a node is inserted into the right subtree of the right child, causing the balance factor to become less than -1.
  - Fix: Perform a single left rotation.
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/RRR_AVL.png)

3. **Left-Right Rotation**:
  - Occurs when a node is inserted into the right subtree of the left child, which disturbs the balance factor of an ancestor node, making it left-heavy.
  - Fix: Perform a left rotation on the left child, followed by a right rotation on the node.
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/LRR_AVL.png)

4. **Right-Left Rotation**:
  - Occurs when a node is inserted into the left subtree of the right child, which disturbs the balance factor of an ancestor node, making it right-heavy.
  - Fix: Perform a right rotation on the right child, followed by a left rotation on the node.
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/RLR_AVL.png)

- **Advantages of AVL Tree**:
  1. **AVL trees** can self-balance themselves and therefore provides time complexity as O(log n) for search, insert and delete.
  2. As it is a balanced BST, so items can be traversed in sorted order.
  3. **AVL trees** in general have relatively less height and hence the search is faster.

- **Disadvantages of AVL Tree**:
  1. It is difficult to implement compared to normal BST.
  2. **AVL trees** provide complicated insertion and removal operations as more rotations are performed.

### Red Black Tree

- TODO

### Binary Heap

- TODO