## Note: This Is Summery Of What I Learned From AI Sourses.
---

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

---

# 🌳 CHAPTER 7 — Binary Search Tree (BST)

## 📌 Why do we need BST?

A normal Binary Tree has no ordering.

Example:

```text
        10
       /  \
      50   20
```

To search for a value, you may need to visit every node.

**Time Complexity:** O(n)

BST solves this by storing values in a sorted manner.

---

# 📌 Golden Rule of BST

For **every node**:

```text
Left Subtree < Node < Right Subtree
```

Or simply:

```text
Smaller → At Left
Larger  → At Right
```

This rule must be true for **every node in the tree**, not just the root.

---

# 📌 Important Observation

A node must satisfy the BST property with respect to **all of its ancestors**, not just its parent.

Example:

```text
        50
       /
      30
        \
         60
```

Although:

```text
60 > 30
```

it is still **not** a BST because:

```text
60 is inside the left subtree of 50

60 > 50 ❌
```

Everything in the left subtree of 50 must be **less than 50**.

---

# 📌 Searching in BST

At every node:

```text
If value < node → Go Left

If value > node → Go Right

If equal → Found
```

Instead of searching the whole tree, BST eliminates half of the remaining search space at each comparison.

Average Time Complexity:

```text
O(log n)
```

Worst Case (Skewed Tree):

```text
O(n)
```

---

# 🌳 CHAPTER 8 — BST Operations

---

## 📌 Designing the Tree Class

A Tree object stores only one thing:

```python
root
```

Why?

Because every node is reachable from the root.

Think of the root as the **entry point** to the entire tree.

---

## 📌 Node Class

Each Node stores:

* data
* left child reference
* right child reference

The Tree manages nodes.

---

# 📌 Recursive Insert

### Base Case

If the current node is:

```text
None
```

Create and return a new node.

---

### Recursive Case

Compare the new value with the current node.

```text
Smaller → Left

Greater → Right
```

Recursively insert into the appropriate subtree.

---

### Most Important Line

After recursion finishes:

```text
Return the current node.
```

Why?

Because recursion rebuilds the subtree while returning.

Every recursive call returns the updated subtree root back to its parent.

---

# 📌 Recursive Search

Algorithm:

```text
If node is None
    Return False

If value == node.data
    Return True

If value < node.data
    Search Left

Else
    Search Right
```

Unlike insert, search **does not modify the tree**.

It only follows one path from root to leaf.

---

# 📌 Find Minimum

Observation:

The smallest value is always found by continuously moving left.

Algorithm:

```text
Start at root

While left child exists

    Move left

Return current node
```

Time Complexity:

```text
O(h)
```

where **h** is the height of the tree.

---

# 📌 Find Maximum

Exactly the opposite.

Algorithm:

```text
Start at root

While right child exists

    Move right

Return current node
```

Time Complexity:

```text
O(h)
```

---

# 📌 BST Deletion (Concept)

Deletion has **three cases**.

---

## Case 1 — Leaf Node

```text
      30

Delete 30
```

Simply remove it.

---

## Case 2 — One Child

Example:

```text
      30
     /
   20
```

Delete 30.

Instead of deleting the subtree:

Connect the parent directly to 20.

Result:

```text
20
```

The subtree survives.

---

## Case 3 — Two Children

Example:

```text
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
```

Deleting 50 directly would disconnect both subtrees.

Instead:

Replace it with either:

* **Inorder Successor** (smallest value in the right subtree), or
* **Inorder Predecessor** (largest value in the left subtree).

Then delete that replacement node from its original position.

Both methods preserve the BST property.

---

# 📌 Inorder Successor

Definition:

The **smallest node in the right subtree**.

How to find it:

```text
Go Right

Then keep going Left
```

---

# 📌 Inorder Predecessor

Definition:

The **largest node in the left subtree**.

How to find it:

```text
Go Left

Then keep going Right
```

---

# 📌 Complexity Summary

| Operation | Average  | Worst |
| --------- | -------- | ----- |
| Search    | O(log n) | O(n)  |
| Insert    | O(log n) | O(n)  |
| Delete    | O(log n) | O(n)  |
| Find Min  | O(h)     | O(n)  |
| Find Max  | O(h)     | O(n)  |

Where:

* **h** = height of the tree

---

# 🧠 Key Concepts Learned

* BST maintains an ordering property.
* Every comparison eliminates half of the remaining search space.
* The Tree object only stores the **root**.
* Recursive insert works by **returning updated subtree roots**.
* Search never changes the tree.
* The minimum value is found by repeatedly moving left.
* The maximum value is found by repeatedly moving right.
* Deletion is not about removing nodes blindly—it is about **rewiring the tree** while preserving the BST property.
* Nodes with two children are handled using the inorder successor or inorder predecessor.

---

# 🎯 Final Revision Cheatsheet

```text
BST Rule:
Left < Node < Right

Insert:
Compare → Left/Right → Return node

Search:
Compare → Left/Right → Found or None

Minimum:
Keep going Left

Maximum:
Keep going Right

Delete:
Leaf → Remove
One Child → Replace with child
Two Children → Replace with Successor/Predecessor
```

---


