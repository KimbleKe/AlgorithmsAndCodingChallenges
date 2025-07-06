Here are Python implementations for common **search algorithms**, covering both basic and advanced methods. Each works on **sorted or unsorted arrays**, depending on the algorithm.

---

## 🔍 1. **Linear Search (O(N))**

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

---

## 🔍 2. **Binary Search (O(log N))**

> Requires sorted array

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 🔍 3. **Jump Search (O(√N))**

> Requires sorted array

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Find the block
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1
```

---

## 🔍 4. **Exponential Search (O(log i))**

> Requires sorted array

```python
def binary_search_expo(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2
    return binary_search_expo(arr, target, index // 2, min(index, len(arr) - 1))
```

---

## 🔍 5. **Fibonacci Search (O(log N))**

> Requires sorted array

```python
def fibonacci_search(arr, target):
    n = len(arr)
    fibMMm2 = 0  # (m-2)'th Fibonacci number
    fibMMm1 = 1  # (m-1)'th Fibonacci number
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    while fibM < n:
        fibMMm2, fibMMm1 = fibMMm1, fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1

    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)

        if arr[i] < target:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > target:
            fibM = fibMMm2
            fibMMm1 -= fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i

    if fibMMm1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1
```

---

## 🔍 6. **Interpolation Search (O(log log N))**

> Works well when data is uniformly distributed

```python
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Estimate the position
        if arr[high] == arr[low]:
            pos = low
        else:
            pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if pos >= len(arr):
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
```

---

## 🔍 7. **Block Search (aka Indexed Search)**

> Split into blocks and do linear search in correct block

```python
def block_search(arr, target, block_size):
    blocks = [(i, min(i + block_size, len(arr))) for i in range(0, len(arr), block_size)]

    # Create block max index
    for start, end in blocks:
        if arr[end - 1] >= target:
            for i in range(start, end):
                if arr[i] == target:
                    return i
            return -1
    return -1
```

---

### ✅ Summary Table

| Algorithm            | Time Complexity | Requirement     | Best Use Case                          |
| -------------------- | --------------- | --------------- | -------------------------------------- |
| Linear Search        | O(N)            | Unsorted        | Small lists                            |
| Binary Search        | O(log N)        | Sorted          | General-purpose fast search            |
| Jump Search          | O(√N)           | Sorted          | Better than linear for large arrays    |
| Exponential Search   | O(log i)        | Sorted          | Fast search in unknown/unbounded lists |
| Fibonacci Search     | O(log N)        | Sorted          | Theoretically optimal log-time search  |
| Interpolation Search | O(log log N)    | Sorted, Uniform | Uniformly distributed data             |
| Block Search         | O(√N)           | Sorted          | Sparse indexes on sorted data          |

---
