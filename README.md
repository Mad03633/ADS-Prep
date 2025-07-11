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

A **Red-Black Tree** is a self-balancing binary search tree where each node has an additional attribute: a color, which can be either red or black. The primary objective of these trees is to maintain balance during insertions and deletions, ensuring efficient data retrieval and manipulation.

- A **Red-Black Tree** have the following properties:
  1. **Node Color**: Each node is either red or black.
  2. **Root Property**: The root of the tree is always black.
  3. **Red Property**: Red nodes cannot have red children (no two consecutive red nodes on any path).
  4. **Black Property**: Every path from a node to its descendant null nodes (leaves) has the same number of black nodes.
  5. **Leaf Property**: All leaves (NIL nodes) are black.
These properties ensure that the longest path from the root to any leaf is no more than twice as long as the shortest path, maintaining the tree's balance and efficient performance.

**Example of Red-Black Tree:**
![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Red_Black_example.png)

- The Correct **Red-Black Tree** in above image ensures that every path from the root to a leaf node has the same number of black nodes. In this case,​ there is one (excluding the root node).
- The Incorrect **Red Black Tree** does not follow the red-black properties as two red nodes are adjacent to each other. Another problem is that one of the paths to a leaf node has zero black nodes, whereas the other two contain a black node.

**Comparison with AVL Tree**:
  - The AVL trees are more balanced compared to Red-Black Trees, but they may cause more rotations during insertion and deletion. So if your application involves frequent insertions and deletions, then **Red-Black trees** should be preferred. And if the insertions and deletions are less frequent and search is a more frequent operation, then AVL tree should be preferred over the Red-Black Tree.

- How does a **Red-Black** Tree ensure balance?
  - A simple example to understand balancing is, that a chain of 3 nodes is not possible in the **Red-Black tree**. We can try any combination of colors and see if all of them violate the Red-Black tree property.

- **Basic Operations on Red-Black Tree**:
1. **Insertion**. 
Inserting a new node in a Red-Black Tree involves a two-step process: performing a standard binary search tree (BST) insertion, followed by fixing any violations of **Red-Black** properties.
  - **BST Insert**: Insert the new node like in a standard BST.
  - **Fix Violations**:
      - If the parent of the new node is black, no properties are violated.
      - If the parent is red, the tree might violate the Red Property, requiring fixes.
  - **Fixing Violations During Insertion**.
  After inserting the new node as a red node, we might encounter several cases depending on the colors of the node's parent and uncle (the sibling of the parent):
    - **Case 1**: **Uncle is Red**: Recolor the parent and uncle to black, and the grandparent to red. Then move up the tree to check for further violations.
    - **Case 2**: **Uncle is Black**:
        - **Sub-case 2.1**: **Node is a right child**: Perform a left rotation on the parent.
        - **Sub-case 2.2**: **Node is a left child**: Perform a right rotation on the grandparent and recolor appropriately.

  2. **Searching**.
  Searching for a node in a **Red-Black Tree** is similar to searching in a standard Binary Search Tree (BST). The search operation follows a straightforward path from the root to a leaf, comparing the target value with the current node's value and moving left or right accordingly.
  1. **Start at the Root**: Begin the search at the root node.
  2. **Traverse the Tree**:
    - If the target value is equal to the current node's value, the node is found.
    - If the target value is less than the - current node's value, move to the left child.
    - If the target value is greater than the current node's value, move to the right child.
  3. **Repeat**: Continue this process until the target value is found or a NIL node is reached (indicating the value is not present in the tree).

  3. **Deletion**.
  Deleting a node from a **Red-Black Tree** also involves a two-step process: performing the BST deletion, followed by fixing any violations that arise.
    1. **BST Deletion**: Remove the node using standard BST rules.
    2. **Fix Double Black**:
      - If a black node is deleted, a "double black" condition might arise, which requires specific fixes.

    **Fixing Violations During Deletion**
    When a black node is deleted, we handle the double black issue based on the sibling's color and the colors of its children:
      - **Case 1: Sibling is Red**: Rotate the parent and recolor the sibling and parent.
      - **Case 2: Sibling is Black**:
        - **Sub-case 2.1: Sibling's children are black**: Recolor the sibling and propagate the double black upwards.
        - **Sub-case 2.2: At least one of the sibling's children is red**:
          - If the sibling's far child is red: Perform a rotation on the parent and sibling, and recolor appropriately.
          - If the sibling's near child is red: Rotate the sibling and its child, then handle as above.
  4. **Rotation**.
  **Rotations** are fundamental operations in maintaining the balanced structure of a **Red-Black Tree** (RBT). They help to preserve the properties of the tree, ensuring that the longest path from the root to any leaf is no more than twice the length of the shortest path. Rotations come in two types: left rotations and right rotations.
  1. **Left Rotation**.
  2. **Right Rotation**.
  
- **Advantages of Red-Black Trees**:
  1. **Balanced**: **Red-Black Trees** are self-balancing, meaning they automatically maintain a balance between the heights of the left and right subtrees. This ensures that search, insertion, and deletion operations take O(log n) time in the worst case.
  2. Efficient search, insertion, and deletion: Due to their balanced structure, **Red-Black Trees** offer efficient operations. Search, insertion, and deletion all take O(log n) time in the worst case.

- **Disadvantages of Red-Black Trees**:
  1. More complex than other balanced trees: Compared to simpler balanced trees like **AVL trees**, **Red-Black Trees** have more complex insertion and deletion rules.
  2. Constant overhead: Maintaining the **Red-Black Tree** properties adds a small overhead to every insertion and deletion operation.

### Binary Heap
A **Binary Heap** is a complete binary tree that stores data efficiently, allowing quick access to the maximum or minimum element, depending on the type of heap. It can either be a **Min Heap** or a **Max Heap**. In a **Min Heap**, the key at the root must be the smallest among all the keys in the heap, and this property must hold true recursively for all nodes. Similarly, a **Max Heap** follows the same principle, but with the largest key at the root.

- **Valid and Invalid examples of heaps**:
![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Min_heap.png)
![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Max_heap.png)

**Operations on Heap**:
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Operations_Heap_1.png)
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Operations_Heap_2.png)

## Graphs

<p align="center">
    <a href="#graph-basics">Graph Basics</a> •
    <a href="#spanning-tree">Spanning Tree</a> •
    <a href="#strongly-connected-components">Strongly Connected Components</a> •
    <a href="#adjacency-matrix">Adjacency Matrix</a> •
    <a href="#adjacency-list">Adjacency List</a> •
    <a href="#dfs-algorithm">DFS Algorithm</a> •
    <a href="#breadth-first-search">Breadth First Search</a> •
    <a href="#dijkstras-algorithm">Dijkstra's Algorithm</a> •
    <a href="#bellman-fords-algorithm">Bellman Ford's Algorithm</a> •
    <a href="#floyd-warshalls-algorithm">Floyd-Warshall's Algorithm</a> •
    <a href="#prims-algorithm">Prim's Algorithm</a> •
    <a href="#kruskal-algorithm">Kruskal's Algorithm</a>
</p>

### Graph Basics

- A collection of nodes that have data and are connected to other nodes.
- A **graph** is a data structure (V, E) - collection of **vertices V**, a collection of **edges E** [represented as ordered pairs of vertices (u,v)]

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/graph.png)

- V = {0, 1, 2, 3} | E = {(0,1), (0,2), (0,3), (1,2)} | G = {V, E}
- **Adjacency**: A vertex is said to be adjacent to another vertex if there is an edge connecting them. Vertices 2 and 3 are not adjacent because there is no edge between them.
- **Path**: A sequence of edges that allows you to go from vertex A to vertex B. 0-1, 1-2 and 0-2 are paths from vertex 0 to vertex 2.
- **Directed Graph**: A **graph** in which an edge (u,v) doesn't necessarily mean that there is an edge (v, u) as well. The edges in such a graph are represented by arrows to show the direction of the edge.
![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/directed_graph.jpg)

- **Graph Representations**: **Adjacency Matrix** and **Adjacency List**

### Spanning Tree

- **Undirected Graph**: Graph in which the edges do not point in any direction - bidirectional
![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/undirected_graph.jpg)
- **Connected Graph**: Graph in which there is always a path from a vertex to any other vertex
![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/connected_graph.jpg)
- **Spanning Tree**: Sub-graph of an undirected connected graph, which includes all the vertices of the graph with a minimum possible number of edges. If a vertex is missed, then it is not a spanning tree.
- The total number of spanning trees with n vertices that can be created from a complete graph is equal to n<sup>(n-2)</sup>
- A **minimum spanning tree** is a spanning tree in which the sum of the weight of the edges is as minimum as possible.

### Adjacency Matrix

- Representing graphs as a matrix of 0s and 1s - boolean value of the matrix indicates if there is a direct path between two vertices.
- Each cell in the matrix is represented as A(i,j) where i and j are vertices.
- The value of A(i,j) is either 1 or 0 depending on whether there is an edge from vertex i to vertex j.
- In case of undirected graphs, the matrix is symmetric about the diagonal because of every edge (i,j), there is also an edge (j,i).

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/adjacency_matrix.jpg)

- **Advantages** -
  1. Basic operations are time efficient - constant time operations
  2. Even if the graph and the adjacency matrix is sparse, we can represent it using data structures for sparse matrices.
  3. By performing operations on the adjacent matrix, we can get important insights into the nature of the graph and the relationship between its vertices.
- **Disadvantages** -
  1. The VxV space requirement of the adjacency matrix makes it a memory hog.
  2. Operations like inEdges and outEdges are expensive when using the adjacency matrix representation.

### Adjacency List

- Represents a graph as an array of linked lists. The index of the array represents a vertex and each element in its linked list represents the other vertices that form an edge with the vertex.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/adjacency_list.jpg)

- **Advantages** -
  1. Efficient in terms of storage because we only need to store the values for the edges.
  2. It also helps to find all the vertices adjacent to a vertex easily.
- **Disadvantages** -
  1. Finding the adjacent list is not quicker than the adjacency matrix because all the connected nodes must be first explored to find them.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/time_matrix_list.jpg)

### DFS Algorithm

- Recursive algorithm for searching all the vertices of a graph or tree.
- Vertex categorized as visited or not visited
- The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.
- Working of DFS -
  1. Place any vertex on top of a stack
  2. Take top item of the stack and add it to the visited list
  3. Create a list of that vertex's adjacent nodes - Add the ones which aren't in the visited list to the top of the stack.
  4. Keep repeating 2 and 3 until stack is empty
- Time complexity - O(V + E), where V is the number of nodes and E is the number of edges.
- Space complexity - O(V).

**Example**:
**Input**: [[2,3,1], [0], [0,4], [0], [2]]

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/example_dfs_bfs.jpg)

**Output**: [0 2 4 3 1]
**Explanation**: 
  - DFS Steps:
    - Start at 0: Mark as visited. Output: 0
    - Move to 2: Mark as visited. Output: 2
    - Move to 4: Mark as visited. Output: 4 (backtrack to 2, then backtrack to 0)
    - Move to 3: Mark as visited. Output: 3 (backtrack to 0)
    - Move to 1: Mark as visited. Output: 1 (backtrack to 0)

### Breadth First Search

- Recursive algorithm for searching all the vertices of a graph or tree data structure.
- The algorithm works as follows:

  1. Start by putting any one of the graph's vertices at the back of a queue.
  2. Take the front item of the queue and add it to the visited list
  3. Create a list of that vertex's adjacent nodes - add the ones which aren't in the visited list to the back of the queue.
  4. Keep repeating steps 2 and 3 until the queue is empty.

- The graph might have two different disconnected parts
- Time complexity - O(V + E), where V is the number of nodes and E is the number of edges.
- Space complexity - O(V).

**Example**:
**Input**: [[2,3,1], [0], [0,4], [0], [2]]

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/example_dfs_bfs.jpg)

**Output**: [0 2 3 1 4]
**Explanation**: 
  - DFS Steps:
    - Start at 0: Mark as visited. Output: 0
    - Move to 2: Mark as visited. Output: 2
    (backtrack to 0)
    - Move to 3: Mark as visited. Output: 3 (backtrack to 0)
    - Move to 1: Mark as visited. Output: 1 (backtrack to 0)
    - Move to 4: Mark as visited. Output: 1 (backtrack to 2, then backtrack to 0)

### Dijkstra's Algorithm

- Allows us to find the shortest path between any two vertices of a graph
- Differs from the minimum spanning tree because the shortest distance between two vertices might not include all the vertices of the graph
- Works on the logic that any subpath of the shortest path between the source and the destination is also the shortest path.
- Time Complexity: O((V+E)LogV) for adjacency list and O(V^2) for adjacency matrix
- Space Complexity: O(V)

Basic steps of **Dijkstra's algorithm**:
  1. Initialize distances to all vertices as infinity, and distance to the starting vertex as 0.
  2. Put all vertices in a priority queue (min-heap), where the key is distance to the vertex.
  3. While the queue is not empty:
   - Extract the vertex with the minimum distance.
   - For each adjacent vertex, update the distance if a shorter path through the extracted vertex is found.

**Example**:
**Input**: src = 0, V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/dijkstra.jpg)

**Output**:  0 4 8 10 10
**Explanation**:  
- **Shortest Paths**:  
  - 0 to 1 = 4. 0 → 1
  - 0 to 2 = 8. 0 → 2
  - 0 to 3 = 10. 0 → 2 → 3 
  - 0 to 4 = 10. 0 → 1 → 4

### Bellman Ford's Algorithm

**Bellman-Ford** is a single source shortest path algorithm. It effectively works in the cases of **negative edges** and is able to detect **negative cycles** as well. It works on the principle of **relaxation** of the edges. In the presence of a **negative weight cycle**, **return -1** to signify that shortest path calculations are not feasible.

**Example**:
  - **Input**: V = 5, edges = [[0, 1, 5], [1, 2, 1], [1, 3, 2], [2, 4, 1], [4, 3, -1]], src = 0

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/bellman-ford.jpg)

  - **Output**: [0, 5, 6, 6, 7]
  - **Explanation**:  Shortest Paths:  
    - For 0 to 1 minimum distance will be 5. By following path 0 → 1
    - For 0 to 2 minimum distance will be 6. By following path 0 → 1  → 2
    - For 0 to 3 minimum distance will be 6. By following path 0 → 1  → 2 → 4 → 3 
    - For 0 to 4 minimum distance will be 7. By following path 0 → 1  → 2 → 4
  - **Note**:
    - [2 ➔ 4, weight=1]
    - dist[2] + 1 < dist[4]
    - 6 + 1 < ∞ → dist[4] = 7
    - dist = [0, 5, 6, 7, 7]
    
    - [4 ➔ 3, weight=-1]
    - dist[4] + (-1) < dist[3]
    - 7 + (-1) = 6 < 7 → dist[3] = 6
    - dist = [0, 5, 6, 6, 7]

  - **Input**: V = 4, edges = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]], src = 0

  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/bellman-ford-neg-cycle.jpg)

  - **Output**: [-1]
    - **Explanation**: The graph contains a negative weight cycle formed by the path 1 → 2 → 3 → 1, where the total weight of the cycle is negative.

**Basic steps of the Bellman-Ford algorithm**:
  1. Initialize the distance to the starting vertex as 0, and the distances to all other vertices as infinity.
  2. Repeat **Ѵ-1** times (where V is the number of vertices in the graph):
    - For each edge (u, v) with weight w:
      - If the distance to the vertex plus the edge weight is less than the distance to the vertex ѵ, update the distance to the vertex ѵ.
  3. Check for **negative cycles**:
    - For each edge (u, v) with weight w:
    - If the distance to the vertex plus the edge weight is less than the distance to the vertex ѵ, there is a **negative cycle**.

### Floyd Warshall's Algorithm

- An algorithm for finding the shortest path between **ALL THE PAIRS** of vertices in a weighted graph.
- Works for both the **directed** and **undirected** weighted graphs - does not work for the graphs with **negative cycles**
- Implementation:
  - Create a matrix A0 of dimension n\*n where n is the number of vertices.
  - Each cell A[i][j] is filled with the distance from the ith vertex to the jth vertex. If there is no path from ith vertex to jth vertex, the cell is left as **infinity**
  - Create a matrix A1 using matrix A0. The elements in the first column and the first row are left as they are.
  - Let k be the intermediate vertex in the shortest path from source to destination. In this step, k is the first vertex. A[i][j] is filled with (A[i][k] + A[k][j]) if (A[i][j] > A[i][k] + A[k][j])
  - Similarly, A2 is created using A1. The elements in the second column and the second row are left as they are.
- **Time Complexity** - **O(n<sup>3</sup>)**
- Space Complexity - O(n<sup>2</sup>)

- **Example**:
  - **Input**: 
  dist[][] = [[0, 4, 10⁸, 5, 10⁸],
              [10⁸, 0, 1,  10⁸, 6],
              [2, 10⁸, 0, 3, 10⁸],
              [10⁸, 10⁸, 1, 0, 2],
              [1, 10⁸, 10⁸, 4, 0]]
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/floyd-warshall-input.jpg)
  - **Output**:[[0, 4, 5, 5, 7], 
               [3, 0, 1, 4, 6], 
               [2, 6, 0, 3, 5],
               [3, 7, 1, 0, 2], 
               [1, 5, 5, 4, 0]]

  - **Explanation**:
  ![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/floyd-warshall-output.jpg)

  *Each cell dist[i][j] in the output shows the shortest distance from node i to node j, computed by considering all possible intermediate nodes using the Floyd-Warshall algorithm.*

- **Basic steps of the Floyd–Warshall algorithm**:
  1. Create a distance matrix, where dist[i][j] is the minimum distance from vertex i to vertex j. 
  2. Initialize the distance matrix by setting dist[i][j] to the weight of the edge between vertices i and j if such an edge exists, and to infinity (INF) if no edge exists. For all vertices j, set dist[i][i] to 0.
  3. Iteratively use each vertex as an intermediate vertex and update distances: 
   - For each pair of vertices (i, j), update dist[i][j] if a shorter path can be obtained through intermediate vertex j.

### Prim's Algorithm

**Prim's algorithm** is a greedy algorithm for finding a minimum spanning tree (MST) in an **undirected weighted graph**. A minimum spanning tree is a subset of the edges of the graph that connects all vertices *without forming cycles* and has the minimum possible sum of edge weights.

- A minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which form a tree that includes every vertex and has the minimum sum of weights among all the trees that can be formed from the graph
- Implementation:
  - Initialize the minimum spanning tree with a vertex chosen at random
  - Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree
  - Keep repeating step 2 until we get a minimum spanning tree
- **Time Complexity**: O(V^2) for adjacency matrix, O((E + V) log V) with a priority queue

- **Example**:

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Prim's_algo.png)

- **Main steps of Prim's algorithm**:
  - Step 1: Determine an arbitrary vertex as the starting vertex of the MST. We pick 0 in the **above** diagram.
  - Step 2: Follow steps 3 to 5 till there are vertices that are not included in the MST (known as fringe vertex).
  - Step 3: Find edges connecting any tree vertex with the fringe vertices.
  - Step 4: Find the minimum among these edges.
  - Step 5: Add the chosen edge to the MST. Since we consider only the edges that connect fringe vertices with the rest, we never get a cycle.
  - Step 6: Return the MST and exit

### Kruskal's Algorithm

**Kruskal's algorithm** is a greedy algorithm for finding a minimum spanning tree (MST) in an undirected weighted graph. Unlike **Prim's algorithm**, which grows around a chosen starting vertex, Kruskal's algorithm works on **sets and adds edges** as needed until all vertices are connected.

- A minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which form a tree that includes every vertex and has the minimum sum of weights among all the trees that can be formed from the graph
- **Start from the edges with the lowest weight** and keep adding edges until we reach the goal.
- Implementation:
  - Sort all the edges from low weight to high
  - Take the edge with the lowest weight and add it to the spanning tree. If adding the edge created a cycle, then reject this edge.
  - Keep adding edges until we reach all vertices
- Time Complexity: O(E log E) or O(E log V)

- **Example**:

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Kruskal's_algo.png)

**Main steps of Kruskal's algorithm**:
  1. Sort all edges in the graph in ascending order of their weights. 
  2. Initialize an empty set to hold the MST.
  3. Iteratively check each edge in the sorted list: 
    - If adding an edge does not form a cycle, add it to the MST. Repeat until the MST contains **V-1** edges (where V is the number of vertices in the graph).