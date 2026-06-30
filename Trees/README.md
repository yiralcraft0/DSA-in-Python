## This a summery of my learnings from AI sorces.

# 🌳 CHAPTER 1 — Why Trees?-----------------------

## 📌 Why do we need Trees?

Linear data structures (Arrays, Linked Lists, Hash Tables) have limitations:

* **Arrays**

  * Insertion/Deletion can be expensive because elements may need to shift.
  * Fixed size (unless using dynamic arrays).

* **Linked Lists**

  * Sequential access only (cannot directly jump to a node).
  * Searching takes **O(n)**.

* **Hash Tables**

  * Excellent for searching.
  * Do **not** maintain hierarchical relationships.
  * Not suitable when parent-child relationships matter.

Trees solve these problems by organizing data hierarchically.

---

## 📌 Real-life Examples

* File System
* Organization Chart
* Family Tree
* HTML DOM
* Decision Trees
* AI Search Trees

---

# 🌳 CHAPTER 2 — Introduction to Trees-----------------------

## 📌 What is a Tree?

A Tree is a **non-linear data structure** made of nodes connected through parent-child relationships.

It always has:

* One Root node
* Zero or more child nodes
* No cycles

---

## 📌 Properties

* Root is the topmost node.
* Every node (except root) has exactly one parent.
* A tree with **n nodes has n−1 edges**.
* There is exactly one path between any two nodes.

---

# 🌳 CHAPTER 3 — Tree Terminology-----------------------

## 📌 Important Terms

### Root

Topmost node.

### Parent

Node having one or more children.

### Child

Node connected below a parent.

### Siblings

Nodes sharing the same parent.

### Leaf Node

Node with **0 children**.

### Internal Node

Any non-leaf node.

### Degree of a Node

Number of children of that node.

### Degree of Tree

Maximum degree among all nodes.

### Depth

Number of edges from the root to a node.

### Height of a Node

Longest path (in edges) from that node to a leaf.

### Height of Tree

Height of the root node.

### Ancestors

All nodes above a node.

### Descendants

All nodes below a node.

### Subtree

A node together with all of its descendants.

> Every node (including a leaf) is the root of its own subtree.

---

# 🌳 CHAPTER 4 — Types of Binary Trees-----------------------

## 📌 Binary Tree

Every node has **at most 2 children**.

Children are ordered:

* Left Child
* Right Child

---

## 🌿 Full Binary Tree

Every node has:

* 0 children
* OR
* 2 children

No node has exactly one child.

---

## 🌲 Perfect Binary Tree

A Full Binary Tree in which:

* Every internal node has 2 children.
* All leaf nodes are at the same level.

Formula:

Total Nodes = **2^(h+1) − 1**

where **h** is the height of the tree.

---

## 🧩 Complete Binary Tree

* Every level is completely filled,
* except possibly the last level.
* The last level is filled **from left to right**.

Used in **Heaps**.

---

## ⚖️ Balanced Binary Tree

For every node:

Height difference between left and right subtree ≤ 1.

Provides efficient operations.

---

## 📏 Degenerate Tree

Every node has only one child.

Behaves like a Linked List.

Worst-case operations become **O(n)**.

---

## ↙️ Left Skewed Tree

Every node has only a left child.

---

## ↘️ Right Skewed Tree

Every node has only a right child.

---

# 🌳 CHAPTER 5 — Binary Tree Implementation-----------------------

## 📌 Basic Idea

A Binary Tree is built using **nodes connected by references**.

Each node stores:

* data
* left child reference
* right child reference

---

## 📌 Manual Construction

Build the tree by:

1. Creating nodes.
2. Connecting nodes using left and right references.
3. Starting from the root.

---

## 📌 Important Concept

A Tree is **not stored continuously in memory** like an array.

It is a collection of nodes connected using references (pointers).

---

# 🌳 CHAPTER 6 — Tree Traversals-----------------------

## 📌 Traversal

Traversal means visiting every node exactly once in a specific order.

---

## 📌 DFS vs BFS

### DFS (Depth First Search)

* Uses recursion (or stack).
* Includes:

    * Preorder
    * Inorder
    * Postorder

### BFS (Breadth First Search)
* Level Order 

    * Uses a queue.
    * Traverses one level at a time.

---

## 1️⃣ Preorder (DFS)

**Order:** Root → Left → Right

Memory Trick:

**Root First**

---

## 2️⃣ Inorder (DFS)

**Order:** Left → Root → Right

Memory Trick:

**Root Middle**

Important:

In a Binary Search Tree (BST), Inorder traversal returns nodes in **sorted order**.

---

## 3️⃣ Postorder (DFS)

**Order:** Left → Right → Root

Memory Trick:

**Root Last**

Common Uses:

* Deleting trees
* Freeing memory
* Expression trees

---

## 4️⃣ Level Order (BFS)

Visits nodes **level by level**.

Uses a **Queue (FIFO)**.

---

## 📌 Complexity

All traversals:

* **Time Complexity:** O(n)

Space Complexity:

* DFS: O(h), where **h** is the height of the tree.
* BFS: O(w), where **w** is the maximum width of the tree.

---

# 🚀 Final Revision Cheatsheet

| Topic       | Key Point                              |
| ----------- | -------------------------------------- |
| Tree        | Non-linear hierarchical data structure |
| Binary Tree | Max 2 children per node                |
| Full        | Every node has 0 or 2 children         |
| Perfect     | Full + all leaves at the same level    |
| Complete    | Last level filled from left to right   |
| Balanced    | Height difference ≤ 1                  |
| Degenerate  | Looks like a linked list               |
| Preorder    | Root → Left → Right                    |
| Inorder     | Left → Root → Right                    |
| Postorder   | Left → Right → Root                    |
| Level Order | Level by Level (BFS)                   |
| DFS         | Uses recursion/stack                   |
| BFS         | Uses queue                             |

---

# 🎯 Key Takeaways

* Trees represent hierarchical relationships efficiently.
* Binary Trees restrict each node to at most two children.
* Different Binary Tree types optimize different use cases.
* Traversals define different ways of visiting nodes.
* Understanding traversals is essential before learning **Binary Search Trees (BSTs)**, **AVL Trees**, **Heaps**, and advanced tree algorithms.

