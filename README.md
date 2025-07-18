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

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/diff_prim_kruskal.jpg)

## Introduction to Algorithms

- **Algorithms** - Finite steps/instructions followed to solve a computational problem in an efficient manner.
- **Importance of algorithms** -

  - Different algorithms aid in solving problems in an efficient manner.
  - Improves run **time/speed** of programs

- Characteristics of algorithms -

  - Finite number of steps
  - Clear and easy to understand
  - Efficient in utilization of resources

- Factors that determine an algorithm's efficiency: **Time complexity** and **Space complexity**
- **Space Complexity** -

  - Calculating the amount of space consumed by an algorithm during the course of its execution.
  - Broadly classified into **fixed/constant complexity** and **linear complexity**
  - **Fixed/Constant**: Size of space consumed will not increase with increase of input size.
  - **Linear**: Space consumed increases with increase of input size - O(n).
  - Take note of the number of variabled during calculation of space complexity

- **Time Complexity** -

  - Concentrate on the number of statements executed for calculation of time complexity.
  - **Loops** - will be executed 'len + 1' times - it will also calculate till, after the condition is false
  - **Inside the loop** - 'len' times execution
  - Increasing order of time complexity - O(1) < O(log(n)) < O(n) < O(nlog(n)) < O(n<sup>2</sup>) < O(n<sup>3</sup>) < O(2<sup>n</sup>) < O(3<sup>n</sup>) < O(n<sup>n</sup>)

- **Asymptotic Notations** -

  - Mathematical functions used to calculate the running time as well as the order of growth of algorithms.
  - Running time refers to the time taken for the computer to run all the statements in an algorithm.
  - Rate of growth refers to how the algorithm will behave when a large amount of input is given.
  - **Types**: **Big O** (worst case - tight upper bound), **Big Omega** (lower bound), **Big Theta**(average case)

- **Big O** -

  - **Big O** notation is generally used to calculate the complexity of an algorithm - how the algorithm will perform when the input size is increased
  - To say a function f(n) is equal to O(g(n)), if there is a constant “c” and “n0” such that the function f(n) will always be less that “c * g(n)”, can be written as “f(n) < c*g(n)" - the function f(n) will not go above the function g(n) for a large value of n. Hence we can consider the function “g(n)” as upper bound for the function f(n)

- **Big Omega** and **Theta** -
  - **Omega** - For a function f(n) is equal to Ω(g(n)) if there exist a constant C and n0 such that f(n) is always greater than C(g(n)). i.e. f(n) > C(g(n)) or C(g(n)) < f(n) (Best Case)
  - **Theta** - For a function f(n) is equal to Ø(n) if a function f(n) is greater than C1 g(n) and is less than C2g(n) for all n>= 0. It means that the function f(n) will always be in-between C1*g(n) and C2*g(n). It can be shown in formula as : C1*g(n) <= f(n) <= C2*g(n) (Average Case)

## Sorting Algorithms

<p align="center">
    <a href="#bubble-sort">Bubble Sort</a> •
    <a href="#insertion-sort">Insertion Sort</a> •
    <a href="#selection-sort">Selection Sort</a> •
    <a href="#quick-sort">Quick Sort</a> •
    <a href="#merge-sort">Merge Sort</a> •
    <a href="#heap-sort">Heap Sort</a> •
    <a href="#counting-sort">Counting Sort</a> •
    <a href="#radix-sort">Radix Sort</a> •
    <a href="#shell-sort">Shell Sort</a> •
    <a href="#smooth-sort">Smooth Sort</a> •
    <a href="#tree-sort">Tree Sort</a> •
    <a href="#cube-sort">Cube Sort</a> •
    <a href="#bucket-sort">Bucket Sort</a>
</p>

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/sorts.jpg)

### Bubble Sort

- **Bubble Sort** will sort by checking if the next element is greater than the present element - if greater then it will swap the elements.
- Use of **2 loops** - **outer** and **inner**
- Each element is compared to its adjacent element - if current is greater, then we swap them
- At the end of the first iteration, the largest element will be at the end, the second largest will be at the n - 1 position
- **Outer loop** is to loop n times and **inner loop** is for swapping
- In place sorting
- **Worst Case**: **O(n<sup>2</sup>)**
- Best Case: O(1) - because an extra variable is used for swapping.

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Bubble-sort.gif)

```
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped;
  
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
      
        // If no two elements were swapped, then break
        if (!swapped)
            break;
    }
}

```

### Insertion Sort

- **Insertion Sort** is an efficient algorithm for sorting a small number of elements.
- In-place sorting - rearranges the elements in place.
- Keys: Numbers that we wish to sort
- Divide array into **sorted** and **unsorted** elements, select first **unsorted element** (key), swap the **sorted elements** to the right to create the correct position and shift the unsorted element (key), advance marker to right (next key)
- Best Case: O(n)
- **Worst Case**: **O(n<sup>2</sup>)**
- Space Complexity: O(1)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Insertion-Sort.gif)

```
void insertionSort(int arr[], int n)
{
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;

        /* Move elements of arr[0..i-1], that are
           greater than key, to one position ahead
           of their current position */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
```

### Selection Sort

- **Selection Sort** is a sorting technique where the **smallest element** is taken from the array and placed at the **first index** - this is repeated for the remaining elements.
- Get the **smallest element** from the array, exchange it with the **first index element**
- Second smallest element swap with second index position, and so forth
- Need of 2 loops - outer loop iterate all the array elements one by one, inner loop - here the element from the outer loop is checked against all the elements from inner loop. If a smaller element is found, then that element will be replaced with the index of outer loop
- **Best, Worst Case**: **O(n<sup>2</sup>)**
- Space Complexity: O(1)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Selection-Sort.gif)

```
void selectionSort(vector<int> &arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; ++i) {

        // Assume the current position holds
        // the minimum element
        int min_idx = i;

        // Iterate through the unsorted portion
        // to find the actual minimum
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_idx]) {

                // Update min_idx if a smaller
                // element is found
                min_idx = j; 
            }
        }

        // Move minimum element to its
        // correct position
        swap(arr[i], arr[min_idx]);
    }
}
```

### Quick Sort

- Based on the **Divide and Conquer** strategy
- **Method**:
  1. Select the **pivot element**: Different variations have different methods of picking the pivot elements. The most basic one picks the **right-most element** as the **pivot element**.
  2. **Rearrange the array**: Arranged in the manner so that the elements smaller than the pivot are to the left whereas the elements larger than the pivot are stored on the right.
     - Pointer fixed at the pivot element. This is compared with the element starting from the first index
     - Second pointer set for the element if it is larger than the pivot
     - Pivot is compared with other elements - If an element smaller than the pivot element is reached, the smaller element is swapped with the greater element found earlier.
     - Process is repeated to set the next greater element as the second pointer. And, swap it with another smaller element.
     - The process goes on until the second last element is reached
     - Pivot swapped with the new second pointer.
  3. Divide the subarrays - Pivot elements are again chosen for the left and the right sub-parts separately. And, step 2 is repeated. The subarrays are divided until each subarray is formed of a single element.
- Time complexity:
  - **Best, Average**: **O(nlog(n))**
  - **Worst**: **O(n<sup>2</sup>)**
- Space Complexity: O(log(n))

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/quicksort.gif)

```
int partition(vector<int>& arr, int low, int high) {
  
    // Choose the pivot
    int pivot = arr[high];
  
    // Index of smaller element and indicates 
    // the right position of pivot found so far
    int i = low - 1;

    // Traverse arr[low..high] and move all smaller
    // elements on left side. Elements from low to 
    // i are smaller after every iteration
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    
    // Move pivot after smaller elements and
    // return its position
    swap(arr[i + 1], arr[high]);  
    return i + 1;
}

// The QuickSort function implementation
void quickSort(vector<int>& arr, int low, int high) {
  
    if (low < high) {
      
        // pi is the partition return index of pivot
        int pi = partition(arr, low, high);

        // Recursion calls for smaller elements
        // and greater or equals elements
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

### Merge Sort

- Based on the **divide and conquer** strategy
- Divide: Divide the array into **half**, and continue to do so with the resultant arrays until only single elements are left
- **Conquer**: Sort the **left part** and **right part** of the array recursively
- **Combine**: Combine the left and right arrays to form one complete, sorted array
- External Sorting, Stable
- Best Case, Worst Case and Average Case: **O(nlogn)**

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/Merge-Sort.gif)

```
// Merges two subarrays of arr[].
// First subarray is arr[left..mid]
// Second subarray is arr[mid+1..right]
void merge(vector<int>& arr, int left, 
                     int mid, int right){
                         
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temp vectors
    vector<int> L(n1), R(n2);

    // Copy data to temp vectors L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0;
    int k = left;

    // Merge the temp vectors back 
    // into arr[left..right]
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], 
    // if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], 
    // if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// begin is for left index and end is right index
// of the sub-array of arr to be sorted
void mergeSort(vector<int>& arr, int left, int right){
    
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}
```

### Heap Sort

- **Heap sort** works by visualizing the elements of the array as a special kind of **complete binary tree** called a heap.
- If the index of any element in the array is i, the element in the index 2i+1 will become the left child and element in 2i+2 index will become the right child. Also, the parent of any element at index i is given by the lower bound of (i-1)/2
- A binary tree is said to follow a heap data structure if - it is a **complete binary tree** and all nodes in the tree follow the property that they are greater than their children - the largest element is at the root and both its children and smaller than the root and so on. Such a heap is called a max-heap. If instead, all nodes are smaller than their children, it is called a min-heap

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/min-max-heap.png)

- Starting from a **complete binary tree**, we can modify it to become a **Max-Heap** by running a function called **heapify** on all the non-leaf elements of the heap.
- To maintain the **max-heap** property in a tree where both sub-trees are max-heaps, we need to run **heapify** on the root element repeatedly until it is larger than its children or it becomes a leaf node.
- **Heap Sort Method**:
  - Since the tree satisfies **Max-Heap** property, then the largest item is stored at the root node.
  - **Swap**: Remove the **root element** and put at **the end** of the array (nth position) Put the last item of the tree (heap) at the vacant place
  - **Remove**: Reduce the size of the heap by 1
  - **Heapify**: Heapify the root element again so that we have the highest element at root
  - Repeat this process
- **Time Complexity** - **O(nlog(n))**
- Space Complexity - O(1)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/heapsort.gif)

```
// To heapify a subtree rooted with node i
// which is an index in arr[].
void heapify(vector<int>& arr, int n, int i){

    // Initialize largest as root
    int largest = i;

    // left index = 2*i + 1
    int l = 2 * i + 1;

    // right index = 2*i + 2
    int r = 2 * i + 2;

    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;

    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;

    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

// Main function to do heap sort
void heapSort(vector<int>& arr){
    int n = arr.size();

    // Build heap (rearrange vector)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // One by one extract an element from heap
    for (int i = n - 1; i > 0; i--) {

        // Move current root to end
        swap(arr[0], arr[i]);

        // Call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}
```

### Counting Sort

- **Counting Sort** is a sorting algorithm that works by **counting** the number of elements with each unique value. This algorithm is particularly effective for sorting integers over a limited range of values. The time complexity of Counting Sort is **O(n + k)**, where **n** is the number of **elements** in the array and **k** is the **range** of the elements' values.

1. Find the **maximum value** in the array.
2. Create an auxiliary array count, **from 0 to the maximum value**, and fill it with **zeros**.
3. **Count** the number of each element in the original array and store this data in the **count array**.
4. Modify the count array so that each element contains **the sum of the previous counters**. This allows you to determine the positions of the elements in the sorted array.
5. Create an **output array** output and fill it with the sorted elements using the data from the **count array**.
6. Copy the sorted elements from the output array to the original array.
- **Time Complexity** - Best, Average and Worst: **O(n + k)** - There are mainly four main loops
- Space Complexity - O(max)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/count_sort.png)

```
vector<int> countSort(vector<int>& inputArray)
{

    int N = inputArray.size();

    // Finding the maximum element of array inputArray[].
    int M = 0;

    for (int i = 0; i < N; i++)
        M = max(M, inputArray[i]);

    // Initializing countArray[] with 0
    vector<int> countArray(M + 1, 0);

    // Mapping each element of inputArray[] as an index
    // of countArray[] array

    for (int i = 0; i < N; i++)
        countArray[inputArray[i]]++;

    // Calculating prefix sum at every index
    // of array countArray[]
    for (int i = 1; i <= M; i++)
        countArray[i] += countArray[i - 1];

    // Creating outputArray[] from countArray[] array
    vector<int> outputArray(N);

    for (int i = N - 1; i >= 0; i--)

    {
        outputArray[countArray[inputArray[i]] - 1]
            = inputArray[i];

        countArray[inputArray[i]]--;
    }

    return outputArray;
}
```

### Radix Sort

- **Radix Sort** is a non-comparative sorting algorithm that sorts numbers by their **digits**. It works by starting with the **least significant digit** and moving toward the **most significant digit**. **Radix sort** often uses an auxiliary sort, such as **counting sort** or bucket sort, to sort by each digit.

1. Determine the **maximum** value in the array to find out the number of **digits**.
2. Start with the **least significant digit** (the one).
3. Use a stable sorting algorithm (such as **counting sort**) to sort the numbers by the current digit.
4. Move to the next **most significant digit**.
5. Repeat steps 3-4 until all digits are sorted.
- **Time Complexity** - Best, Average and Worst: **O(n + k)**
- Space Complexity - O(max)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/radix-sort.gif)

```
// A utility function to get maximum
// value in arr[]
int getMax(int arr[], int n)
{
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}

// A function to do counting sort of arr[]
// according to the digit
// represented by exp.
void countSort(int arr[], int n, int exp)
{

    // Output array
    int output[n];
    int i, count[10] = { 0 };

    // Store count of occurrences
    // in count[]
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    // Change count[i] so that count[i]
    // now contains actual position
    // of this digit in output[]
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];

    // Build the output array
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    // Copy the output array to arr[],
    // so that arr[] now contains sorted
    // numbers according to current digit
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}

// The main function to that sorts arr[]
// of size n using Radix Sort
void radixsort(int arr[], int n)
{

    // Find the maximum number to
    // know number of digits
    int m = getMax(arr, n);

    // Do counting sort for every digit.
    // Note that instead of passing digit
    // number, exp is passed. exp is 10^i
    // where i is current digit number
    for (int exp = 1; m / exp > 0; exp *= 10)
        countSort(arr, n, exp);
}
```

## Shell Sort

- **Shell sort** is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved. The **idea** is to first sort the elements that are **far from each other**, and then gradually reduce this distance to **1** (then a regular insertion sort is performed, but the array will already be partially sorted).

- **Algorithm**:
  - Step 1 − Start
  - Step 2 − Initialize the value of gap size, say h.
  - Step 3 − Divide the list into smaller sub-part. Each must have equal intervals to h.
  - Step 4 − Sort these sub-lists using insertion sort.
  - Step 5 – Repeat this step 2 until the list is sorted.
  - Step 6 – Print a sorted list.
  - Step 7 – Stop.

- **Time Complexity**:
  - **Worst-Case**: (O(n^2))
  - **Best-Case**: (O(n log n))

```
/* function to sort arr using shellSort */
int shellSort(int arr[], int n)
{
    // Start with a big gap, then reduce the gap
    for (int gap = n/2; gap > 0; gap /= 2)
    {
        // Do a gapped insertion sort for this gap size.
        // The first gap elements a[0..gap-1] are already in gapped order
        // keep adding one more element until the entire array is
        // gap sorted 
        for (int i = gap; i < n; i += 1)
        {
            // add a[i] to the elements that have been gap sorted
            // save a[i] in temp and make a hole at position i
            int temp = arr[i];

            // shift earlier gap-sorted elements up until the correct 
            // location for a[i] is found
            int j;            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                arr[j] = arr[j - gap];
            
            //  put temp (the original a[i]) in its correct location
            arr[j] = temp;
        }
    }
    return 0;
}
```

## Smooth Sort

- **Smooth Sort** is an improved version of Heap Sort.
- **Main Goal**:
  - Speed up sorting when the array is **partially** sorted.
  - Heap Sort always has O(n log n) complexity, regardless of the initial order. **Smooth Sort** also works in O(n log n) in the **worst case**, but if the array is almost sorted, it works in almost **O(n)**.

- **Smooth Sort** uses a special structure – **Leonardo heaps** instead of a regular binary heap.
- **Leonardo numbers** are similar to Fibonacci numbers, but start as:
  - L(0) = 1
  - L(1) = 1
  - L(k) = L(k-1) + L(k-2) + 1
  - The first numbers are: 1, 1, 3, 5, 9, 15, ...

```
// Define the Leonardo numbers
int leonardo(int k)
{
    if (k < 2) {
        return 1;
    }
    return leonardo(k - 1) + leonardo(k - 2) + 1;
}

// Build the Leonardo heap by merging
// pairs of adjacent trees
void heapify(vector<int>& arr, int start, int end)
{
    int i = start;
    int j = 0;
    int k = 0;

    while (k < end - start + 1) {
        if (k & 0xAAAAAAAA) {
            j = j + i;
            i = i >> 1;
        }
        else {
            i = i + j;
            j = j >> 1;
        }

        k = k + 1;
    }

    while (i > 0) {
        j = j >> 1;
        k = i + j;
        while (k < end) {
            if (arr[k] > arr[k - i]) {
                break;
            }
            swap(arr[k], arr[k - i]);
            k = k + i;
        }

        i = j;
    }
}

// Smooth Sort function
vector<int> smooth_sort(vector<int>& arr)
{
    int n = arr.size();

    int p = n - 1;
    int q = p;
    int r = 0;

    // Build the Leonardo heap by merging
    // pairs of adjacent trees
    while (p > 0) {
        if ((r & 0x03) == 0) {
            heapify(arr, r, q);
        }

        if (leonardo(r) == p) {
            r = r + 1;
        }
        else {
            r = r - 1;
            q = q - leonardo(r);
            heapify(arr, r, q);
            q = r - 1;
            r = r + 1;
        }

        swap(arr[0], arr[p]);
        p = p - 1;
    }

    // Convert the Leonardo heap
    // back into an array
    for (int i = 0; i < n - 1; i++) {
        int j = i + 1;
        while (j > 0 && arr[j] < arr[j - 1]) {
            swap(arr[j], arr[j - 1]);
            j = j - 1;
        }
    }

    return arr;
}
```

## Tree Sort

- **Tree Sort** is a sorting algorithm that uses a **binary search tree (BST)** to sort elements.

- **How does the algorithm work?**:
  1. Inserting elements into a **BST**
    - We start with an empty tree.
    - Insert each array element into the tree, following the BST rule:
      - If the element is smaller than the current node, go left.
      - If it is larger, go right.

  2. **In-order** traversal
    - After constructing the tree, we perform an In-order traversal.
    - In-order traversal BST always produces a sorted sequence.

- **Time Complexity**:
  - **Worst-Case**: (O(n^2))
  - **Best-Case**: (O(n log n))

## Cube Sort

- **Cube Sort** is a rare sorting algorithm based on multidimensional sorting.
- Designed as a generalization of Bucket Sort / Counting Sort / Radix Sort, but works in 3D (cubic) space.
- Cube Sort is almost never used in the industry. It is known mainly as an academic algorithm or in problems with high-dimensional data.

- **The main idea**:
  - If you need to sort data with several keys (for example, (x, y, z)), you can:
  - Represent the data as a three-dimensional array (cube).
  - Sort the elements by each of the three coordinates (axes) in turn:
    - First by x
    - Then by y
    - Then by z
  - This approach ensures ordering by all keys.

- **Time Complexity**: O(n log n)

### Bucket Sort

- Sorting algorithm that divides the unsorted array elements into **several groups (buckets)**
- Each **bucket** is then **sorted** by using any of the suitable **sorting algorithms** or recursively applying the same bucket algorithm
- **Method**:
  - Create an **array** of size **n**. Each slot of this array is used as a **bucket** for storing elements.
  - Insert elements into the buckets from the array. The elements are inserted according to the range of the bucket.
  - The elements of each bucket are sorted using any of the stable sorting algorithms
  - The elements from each bucket are gathered
- **Time Complexity**:
  - **Best**: **O(n + k)**
  - Average: O(n)
  - **Worst**: **O(n<sup>2</sup>)**
- Space Complexity - O(n + k)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/bucket.webp)

```
// Insertion sort function to sort individual buckets
void insertionSort(vector<float>& bucket) {
    for (int i = 1; i < bucket.size(); ++i) {
        float key = bucket[i];
        int j = i - 1;
        while (j >= 0 && bucket[j] > key) {
            bucket[j + 1] = bucket[j];
            j--;
        }
        bucket[j + 1] = key;
    }
}

// Function to sort arr[] of size n using bucket sort
void bucketSort(float arr[], int n) {
    // 1) Create n empty buckets
    vector<float> b[n];

    // 2) Put array elements in different buckets
    for (int i = 0; i < n; i++) {
        int bi = n * arr[i];
        b[bi].push_back(arr[i]);
    }

    // 3) Sort individual buckets using insertion sort
    for (int i = 0; i < n; i++) {
        insertionSort(b[i]);
    }

    // 4) Concatenate all buckets into arr[]
    int index = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < b[i].size(); j++) {
            arr[index++] = b[i][j];
        }
    }
}
```

## Search Algorithms

<p align="center">
    <a href="#linear-search">Linear Search</a> •
    <a href="#binary-search">Binary Search</a>
</p>

### Linear Search

- **Sequential searching algorithm** where we start from **one end** and check **every** element of the list until the desired element is **found**.
- **Method**:
  - Start from the **first element** and **compare** it with each element in the array
  - Return the index if there is a match
- **Time Complexity** - O(n)
- Space Complexity - O(1)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/linear.gif)

```
int search(vector<int>& arr, int x) {
    for (int i = 0; i < arr.size(); i++)
        if (arr[i] == x)
            return i;
    return -1;
}
```

### Binary Search

- **Searching algorithm** for finding an **element's position** in a **sorted** array
- Element is always searched in the **middle** of a portion of an array
- **Method**:
  - Set **two pointers** **low** and **high** at the **lowest** and the **highest** positions respectively
  - Find the **middle element** of the array
  - If **x > middle** element, **compare x** with the **middle element** of the elements on the **right side** of middle element. This is done by setting low to **low = middle element + 1**
  - Else, compare x with the middle element of the elements on the **left side** of middle element. This is done by setting high to **high = middle element - 1**
  - Repeat steps 3 to 6 until low meets high.
- **Time Complexity**:
  - **Best**: O(1)
  - Average: O(log(n))
  - **Worst**: O(log(n))
- Space Complexity - O(1)

![](https://github.com/Mad03633/ADS-Prep/blob/main/Media/binary.gif)

```
// An iterative binary search function.
int binarySearch(int arr[], int low, int high, int x)
{
    while (low <= high) {
        int mid = low + (high - low) / 2;

        // Check if x is present at mid
        if (arr[mid] == x)
            return mid;

        // If x greater, ignore left half
        if (arr[mid] < x)
            low = mid + 1;

        // If x is smaller, ignore right half
        else
            high = mid - 1;
    }

    // If we reach here, then element was not present
    return -1;
}
```