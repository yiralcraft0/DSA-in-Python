# Arrays

An **Array** is a linear data structure that stores elements of the same data type in contiguous memory locations. Each element is accessed using its index, allowing constant-time random access.

### Why do we use it?
- Fast element access
- Easy traversal
- Low memory overhead
- Base structure for many algorithms

### Memory Layout
- Contiguous memory
- Address calculations
- Cache locality

**Example addresses (4 bytes per element):**

| Index | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Address | 1000 | 1004 | 1008 | 1012 | 1016 |

Each element occupies 4 bytes.

### Random Access — Address Formula
```
Address = Base + (Index × Size of Element)
```
This gives **O(1)** complexity.

---

## Static vs Dynamic Arrays

| Feature | Static Array | Dynamic Array |
|---|---|---|
| Size | Fixed | Resizable |
| Memory | Continuous | Continuous (reallocated when needed) |
| Insert at End | Not possible if full | Amortized O(1) |
| Memory Wastage | Less | Possible |
| Examples | C: array<br> | C++: vector<br>Java: ArrayList<br>Python: list |

### Why is Python's list called a dynamic array?
Because it automatically resizes itself when it becomes full — by copying to a larger block of memory and copying over the existing elements.

### What does "Amortized" mean?
Amortized time complexity is the **average time complexity over a sequence of operations**, even if some individual operations are slower.

---

## Operations — Time Complexity

| Operation | Complexity |
|---|---|
| Access | O(1) |
| Search | O(n) |
| Update | O(1) |
| Insert (End) | O(1) amortized |
| Insert (Middle) | O(n) |
| Delete | O(n) |

### Advantages of Arrays
- Fast access
- Cache friendly
- Constant-time indexing

### Java/C++ Vector vs Array
You can dynamically resize and access elements without traversing previous elements.

### Why "cache friendly"?
Since elements are stored next to each other in memory, CPUs can fetch multiple elements at once without accessing memory repeatedly — improving performance.

### Disadvantages of Arrays
- Insertion takes O(n) time complexity
- Deletion takes O(n) time complexity
- Memory reallocation in dynamic arrays is costly

### What does "Amortized" mean (expanded)?
Amortized time complexity is the average complexity over a sequence of operations, even if some individual operations are slower.

---

## Pattern Recognition

### What should I think about when I see arrays?
- Sequential data
- Index-based access
- Contiguous memory
- Iteration
- Searching
- Sorting

### Common Patterns

| Pattern | Use Case |
|---|---|
| Two Pointer | Sorted arrays |
| Sliding Window | Contiguous subarrays |
| Prefix Sum | Range queries |
| Hash Map | Fast lookup |
| Binary Search | Sorted arrays |
| Sorting + Two Pointer | Sum problems |