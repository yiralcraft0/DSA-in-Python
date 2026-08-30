# Hash Tables

## What is a Hash Table?
- A hash table (or hash map) is a data structure that stores information in **key-value pairs**, allowing for extremely fast data retrieval.
- A hash table stores data so that inserting, searching, and deleting are usually very fast — approximately **O(1)**.
- Python provides two built-in hash table structures:
  - `dict` → stores key-value pairs
  - `set` → stores only unique values

**Example:**
```python
table = {'name': 'Priyanshu', 'marks': 90}
```

## How It Works
A hash function converts a key into a bucket index.

```
Key → hash function → Hash value → Bucket index
```

**Example:**
```
apple → hash('apple') → bucket 3
```

When `'apple'` is requested again, the hash table calculates its bucket and searches there.

---

## Dictionary — Basic Operations

```python
table = {}   # empty dict

# Access
price = table['apple']   # Key → value

# Insert
table['apple'] = 50

# Check existence
if 'apple' in table:
    print("Found")

# Update
table['apple'] = 60

# Delete
del table['apple']

# Safe delete
table.pop('apple', None)
```

### Time Complexity

| Operation | Average | Worst |
|---|---|---|
| Access | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Update | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Traverse | O(n) | O(n) |

The worst case can occur because of many **hash collisions**.

---

## Dictionary vs Sets

### Dictionary
```python
data = {"name": "Priyanshu", "Age": 18, "Branch": "CSE"}
```
- Stores key-value pairs
- Use it for:
  - Indices
  - Frequency counting
  - Mapping one value to another
  - Caching previous results

### Sets
```python
screen = {2, 4, 7}
```
- Stores unique values only
- Use it for:
  - Checking whether a value exists
  - Finding duplicates
  - Removing duplicates
  - Tracking visited values

---

## Advantages
- Fast average lookup — O(1)
- Fast insertion and deletion on average
- Useful for frequency counting
- Excellent for duplicate detection
- Can reduce some O(n²) solutions to O(n)

## Disadvantages
- Requires extra memory
- Elements are not automatically sorted
- Collisions can occur
- Worst-case operations can become O(n)
- Mutable objects (such as a list) cannot be used as dictionary keys

## When Should You Use a Hash Table?
- Does this value exist?
- Have I seen this value before?
- How many times does each value occur?
- Where did this value previously appear?
- Is there a duplicate?
- Can I avoid repeatedly searching the array?