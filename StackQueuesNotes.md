# Stacks & Queues

---

# Stacks

## What is a Stack?
A **Stack** is a linear data structure that follows **LIFO** — **Last In, First Out**. The last element added is the first one removed.

Think of it like a stack of plates — you add and remove from the top only.

```
push -> [3]
        [2]
        [1]
pop  <- removes 3 first
```

---

## Basic Operations

| Operation | Description |
|---|---|
| `push(x)` | Add element `x` to the top |
| `pop()` | Remove and return the top element |
| `peek()` / `top()` | View the top element without removing it |
| `isEmpty()` | Check if the stack is empty |

### Python Implementation (using a list)
```python
stack = []

# Push
stack.append(10)
stack.append(20)

# Pop
stack.pop()      # removes 20

# Peek
top = stack[-1]

# isEmpty
is_empty = len(stack) == 0
```

---

## Time Complexity

| Operation | Complexity |
|---|---|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |

---

## Why Use It?
- Tracks state that needs to be undone/reversed (undo functionality, back button)
- Naturally models nested/recursive structures (parentheses, function calls)
- Backtracking algorithms use a stack (explicitly or via recursion's call stack)

## Advantages
- Simple and fast O(1) operations at the top
- Great for reversing order / tracking "most recent" item

## Disadvantages
- No random access to middle elements
- Only top element accessible — not suited for search-heavy tasks

---

## Common Use Cases / Patterns
- **Balanced Parentheses / Valid Brackets** — push opening brackets, pop on matching closing bracket
- **Undo/Redo** functionality
- **Function Call Stack** — recursion tracking
- **Monotonic Stack** — maintaining increasing/decreasing order for problems like "Next Greater Element"
- **Expression Evaluation** — infix to postfix, postfix evaluation
- **DFS (Depth-First Search)** — iterative implementation using an explicit stack
- **Browser History (back button)**

---

# Queues

## What is a Queue?
A **Queue** is a linear data structure that follows **FIFO** — **First In, First Out**. The first element added is the first one removed.

Think of it like a line at a ticket counter — first person in line gets served first.

```
enqueue -> [1][2][3] <- dequeue removes 1 first
```

---

## Basic Operations

| Operation | Description |
|---|---|
| `enqueue(x)` | Add element `x` to the back |
| `dequeue()` | Remove and return the front element |
| `front()` / `peek()` | View the front element without removing it |
| `isEmpty()` | Check if the queue is empty |

### Python Implementation (using `collections.deque`)
```python
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
queue.popleft()   # removes 10

# Peek
front = queue[0]

# isEmpty
is_empty = len(queue) == 0
```

> Note: A plain Python `list` can simulate a queue, but `pop(0)` is O(n) — always prefer `collections.deque` for O(1) operations.

---

## Time Complexity

| Operation | Complexity (deque) | Complexity (list) |
|---|---|---|
| Enqueue | O(1) | O(1) |
| Dequeue | O(1) | O(n) |
| Peek | O(1) | O(1) |
| Search | O(n) | O(n) |

---

## Types of Queues

| Type | Description |
|---|---|
| Simple Queue | Standard FIFO |
| Circular Queue | Last position connects back to the first (efficient fixed-size buffer) |
| Priority Queue | Elements dequeued by priority, not insertion order (usually backed by a heap) |
| Deque (Double-Ended Queue) | Insertion/removal allowed from both ends |

---

## Why Use It?
- Models real-world "waiting line" scenarios (task scheduling, print queues)
- Core building block for **BFS (Breadth-First Search)**
- Handles data processed in the order it arrives

## Advantages
- Fair ordering — first come, first served
- O(1) enqueue/dequeue with the right implementation (deque)

## Disadvantages
- No random access to middle elements
- Plain array-based queues can waste space unless implemented circularly

---

## Common Use Cases / Patterns
- **BFS (Breadth-First Search)** — level-order traversal of trees/graphs
- **Task Scheduling** — CPU scheduling, print queue, request handling
- **Sliding Window Maximum** — using a monotonic deque
- **Level Order Traversal** of a tree
- **Rate Limiting / Buffering** systems

---

## Stack vs Queue

| Feature | Stack | Queue |
|---|---|---|
| Order | LIFO | FIFO |
| Insertion | Top | Back |
| Removal | Top | Front |
| Typical Use | Undo, DFS, recursion, parsing | BFS, scheduling, buffering |
| Python Implementation | `list` (`append`/`pop`) | `collections.deque` |