# Python Codility Test Prep Cheat Sheet

## I. Essential Python Libraries

| Category                          | Library        | Use Case                                         |
| --------------------------------- | -------------- | ------------------------------------------------ |
| **Math & Number Theory**          | `math`         | `gcd`, `factorial`, `sqrt`, `ceil`, `floor`      |
|                                   | `fractions`    | Rational arithmetic (rare)                       |
|                                   | `decimal`      | Precise decimal arithmetic                       |
| **Collections & Data Structures** | `collections`  | `deque`, `defaultdict`, `Counter`, `OrderedDict` |
|                                   | `heapq`        | Min-heap, priority queue                         |
| **Algorithms**                    | `bisect`       | Binary search on sorted lists                    |
|                                   | `itertools`    | Permutations, combinations, grouping             |
|                                   | `functools`    | `lru_cache`, `reduce`, memoization               |
| **Typing (for IDE & type hints)** | `typing`       | `List`, `Optional`, `Tuple`, `Dict`              |
| **Others**                        | `string`, `re` | Character sets, regex (if needed)                |

---

## II. Most Useful Built-in Functions

| Type            | Function                                     | Use Case                    |
| --------------- | -------------------------------------------- | --------------------------- |
| Math            | `abs`, `pow`, `round`, `divmod`              | Basic math                  |
| Logic           | `all`, `any`                                 | Conditions over collections |
| Iteration       | `enumerate`, `zip`, `map`, `filter`          | Smart iteration             |
| Type/Conversion | `int`, `float`, `str`, `list`, `set`, `dict` | Type ops                    |
| Sorting         | `sorted`, `reversed`, `min`, `max`           | Built-ins                   |
| Eval            | `eval`, `ord`, `chr`                         | Rare but useful             |
| Hashing         | `hash`, `id`                                 | For dict/set safety         |

---

## III. Python Data Structures

| Type            | Description            | Syntax Example     |
| --------------- | ---------------------- | ------------------ |
| **List**        | Dynamic array          | `A = [1, 2, 3]`    |
| **Tuple**       | Immutable list         | `t = (1, 2)`       |
| **Set**         | Unique unordered items | `s = {1, 2}`       |
| **Dict**        | Key-value mapping      | `d = {'a': 1}`     |
| **Deque**       | Fast queue             | `deque([1,2])`     |
| **Heap**        | Min-heap               | `heapq.heappush()` |
| **Counter**     | Frequency count        | `Counter(A)`       |
| **DefaultDict** | Auto init dict         | `defaultdict(int)` |

---

## IV. Codility-Specific Coding Patterns

| Pattern                 | Use Case                              |
| ----------------------- | ------------------------------------- |
| Prefix Sums             | Range queries                         |
| Sliding Window          | Max/min sum in window                 |
| Two Pointers            | Pairs, sorted array, distances        |
| Stack                   | Balanced parentheses, monotonic stack |
| DFS/BFS                 | Trees, graphs                         |
| Union-Find              | Connected components                  |
| Binary Search on Answer | Search in large range                 |
| Kadane’s Algorithm      | Max subarray sum                      |
| Bit Manipulation        | XOR tricks                            |
| Hash Maps / Sets        | Duplicates, lookup                    |
| Sorting & Greedy        | Interval scheduling, optimization     |

---

## V. Python Tips for Codility

* Use `enumerate()` instead of `range(len(A))`
* Use `heapq` for efficient priority queue
* Avoid `.remove()` on lists → use sets/dict for `O(1)` removals
* Cache expensive recursive calls using `@lru_cache(None)`
* Avoid `A.insert(0, x)` or `pop(0)` → use `collections.deque`
* Use `bisect.bisect_left` and `bisect.insort` for binary search insertions

---

## VI. Python Syntax Reminders (Quick Reference)

```python
# Set operations
s = set()
s.add(1)
s.remove(1)      # raises KeyError if not found
s.discard(1)     # safe remove
x = s.pop()      # removes arbitrary item
s.clear()        # empty the set

# Deque
from collections import deque
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
d.pop()
d.popleft()

# Heap
import heapq
heapq.heappush(heap, value)
heapq.heappop(heap)
```


---

```markdown
# Python Cheat Sheet for Codility Tests (Optimal Solutions)

## Essential Python Built-in Functions & Libraries

### 1. Math & Numeric Operations
- **`math` module**  
  ```python
  import math
  math.sqrt(x), math.pow(x, y), math.gcd(a, b)
  math.floor(), math.ceil(), math.isqrt()  # Python 3.8+
  ```
- **Basic Numeric Functions**  
  ```python
  abs(x), min(), max(), sum(iterable)
  divmod(a, b)  # (quotient, remainder)
  round(x, ndigits)
  ```

### 2. List & Array Manipulation
- **Sorting & Slicing**  
  ```python
  sorted(iterable, key=..., reverse=True)
  list.reverse(), list.sort()
  ```
- **Iteration Helpers**  
  ```python
  enumerate(list)  # (index, value)
  zip(*iterables)  # Combine lists
  filter(func, iterable), map(func, iterable)
  any(iterable), all(iterable)  # Check conditions
  ```

### 3. String Operations
```python
str.split(), str.join()
str.strip(), str.replace()
str.startswith(), str.endswith()
str.isdigit(), str.isalpha()
ord('a')  # → 97, chr(97)  # → 'a'
```

### 4. Data Structures
#### Built-in
- **`list`**: `append()`, `pop()`, slicing  
- **`set`**: `add()`, `remove()`, O(1) lookups  
- **`dict`**: `keys()`, `values()`, `items()`  

#### `collections` Module
```python
from collections import defaultdict, Counter, deque
defaultdict(int)  # No KeyError
Counter(A)  # Frequency map
deque()  # O(1) appendleft/popleft
```

### 5. Itertools (Advanced)
```python
from itertools import permutations, combinations, groupby
permutations('ABC', 2)  # All possible orderings
groupby(data, key=func)  # Group consecutive keys
```

### 6. Heap (Priority Queue)
```python
import heapq
heap = []
heapq.heappush(heap, 2)
heapq.heappop(heap)  # Min-heap by default
```

### 7. Binary Search (`bisect`)
```python
import bisect
bisect.bisect_left(arr, x)  # Insertion point
bisect.insort_left(arr, x)  # Insert in sorted order
```

### 8. Memoization (`lru_cache`)
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

### 9. Bit Manipulation
```python
x & y, x | y, x ^ y  # AND, OR, XOR
x << 2, x >> 2  # Bit shifts
bin(x), int('1010', 2)  # Binary conversions
```

---

## 🚀 Best Practices for Codility

### Time & Space Complexity
✅ **Use `set`/`dict` for O(1) lookups**  
✅ **Avoid O(N²) nested loops**  
✅ **Prefer `Counter` over manual frequency counting**  

### Edge Cases
- Empty inputs (`A = []`)  
- Single-element inputs (`N = 1`)  
- Large inputs (N = 100,000)  

### Pitfalls
❌ Modifying a list while iterating  
❌ Forgetting `N+1` cases (e.g., MaxCounters)  

---

## 📌 Final Tips
1. **Master `Counter`, `defaultdict`, and `heapq`** → Solves 50% of problems!  
2. **Use `bisect` for sorted arrays**  
3. **For DP, use `lru_cache`**  
4. **Practice slicing and list comprehensions**  

```

---