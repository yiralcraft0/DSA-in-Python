# Linked Lists

## What is a Linked List?
A **Linked List** is a linear data structure where elements (called **nodes**) are stored in separate memory locations, and each node points to the next node using a **reference/pointer**. Unlike arrays, elements are **not** stored in contiguous memory.

Each node contains:
- **Data** — the value stored
- **Next** — a pointer/reference to the next node

```
[Data|Next] -> [Data|Next] -> [Data|Next] -> None
```

---

## Why Use It?
- Efficient insertion/deletion (no shifting of elements like arrays)
- Dynamic size — grows/shrinks as needed
- No memory wastage from over-allocation

---

## Memory Layout
- **Non-contiguous** — nodes can live anywhere in memory
- Each node stores an extra pointer (overhead compared to arrays)
- No random access — must traverse from the head to reach an element

---

## Types of Linked Lists

| Type | Description |
|---|---|
| Singly Linked List | Each node points to the next only |
| Doubly Linked List | Each node points to both next and previous |
| Circular Linked List | Last node points back to the head (can be singly or doubly) |
---

## Time Complexity

| Operation | Singly Linked List | Array |
|---|---|---|
| Access (by index) | O(n) | O(1) |
| Search | O(n) | O(n) |
| Insert at Head | O(1) | O(n) |
| Insert at End | O(n) *(O(1) if tail pointer kept)* | O(1) amortized |
| Insert at Middle | O(n) | O(n) |
| Delete at Head | O(1) | O(n) |
| Delete at End | O(n) | O(1) |
| Delete at Middle | O(n) | O(n) |

---

## Linked List vs Array

| Feature | Array | Linked List |
|---|---|---|
| Memory | Contiguous | Non-contiguous |
| Access | O(1) random access | O(n) sequential access |
| Insert/Delete at start | O(n) | O(1) |
| Memory overhead | Low | Higher (extra pointer per node) |
| Size | Fixed/resizable with copy cost | Fully dynamic |
| Cache friendliness | High | Low |

---

## Advantages
- Fast insertion/deletion at the head (O(1))
- Dynamic size, no need to pre-allocate
- No wasted memory from over-allocation
- Easy to implement stacks/queues on top of it

## Disadvantages
- No random access — must traverse from head (O(n))
- Extra memory used for storing pointers
- Not cache-friendly (nodes scattered in memory)
- Reverse traversal not possible in singly linked lists (without extra pointers/recursion)

---

## Pattern Recognition

### What should I think about when I see a linked list problem?
- Traversal (O(n))
- Pointer manipulation (rewiring `next`, sometimes `prev`)
- Cycle detection
- Reversal
- Merging / splitting lists
- Finding middle / nth node from end

### Common Patterns

| Pattern | Use Case |
|---|---|
| Fast & Slow Pointers (Tortoise & Hare) | Cycle detection, finding the middle node |
| Reverse Pointers | Reversing a linked list (iterative/recursive) |
| Dummy Node | Simplifies edge cases in insert/delete at head |
| Two Pointer (offset by k) | Finding the k-th node from the end |
| Merge Technique | Merging two sorted linked lists |
| Recursion | Reversing, deleting duplicates, or traversing recursively |

---

## Common Interview Questions
- Reverse a linked list
- Detect a cycle (Floyd's Cycle Detection)
- Find the middle of a linked list
- Merge two sorted linked lists
- Remove the N-th node from the end
- Detect and remove a loop
- Check if a linked list is a palindrome
- Find the intersection point of two linked lists