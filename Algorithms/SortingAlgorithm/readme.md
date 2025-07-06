Here’s a succinct summary of common sorting algorithms, including how they work and their **time and space complexities**:

---

| Algorithm          | Best Time  | Avg Time   | Worst Time | Space    | How It Works                                                        |
| ------------------ | ---------- | ---------- | ---------- | -------- | ------------------------------------------------------------------- |
| **Bubble Sort**    | O(N²)      | O(N²)      | O(N²)      | O(1)     | Repeatedly swap adjacent elements if out of order (bubble up max).  |
| **Selection Sort** | O(N²)      | O(N²)      | O(N²)      | O(1)     | Select smallest from unsorted and place it at correct position.     |
| **Insertion Sort** | O(N)       | O(N²)      | O(N²)      | O(1)     | Insert elements into sorted portion by shifting larger elements.    |
| **Merge Sort**     | O(N log N) | O(N log N) | O(N log N) | O(N)     | Divide array, recursively sort, and merge sorted halves.            |
| **Quick Sort**     | O(N log N) | O(N log N) | O(N²)      | O(log N) | Choose pivot, partition array, and recursively sort partitions.     |
| **Heap Sort**      | O(N log N) | O(N log N) | O(N log N) | O(1)     | Build max-heap, extract max repeatedly and rebuild heap.            |
| **Counting Sort**  | O(N + K)   | O(N + K)   | O(N + K)   | O(K)     | Count occurrences and reconstruct sorted array (for integers).      |
| **Shell Sort**     | O(N log N) | O(N^1.5)   | O(N²)      | O(1)     | Insertion sort with decreasing gap sizes to pre-sort elements.      |
| **Tim Sort**       | O(N)       | O(N log N) | O(N log N) | O(N)     | Hybrid of merge and insertion sort (used in Python, Java).          |
| **Radix Sort**     | O(N·k)     | O(N·k)     | O(N·k)     | O(N + k) | Sort by each digit (or byte), using stable sort like counting sort. |

---

## ✅ Key Takeaways

* **Best General-Purpose Sorts:** `Merge Sort`, `Quick Sort`, `Tim Sort`
* **Best for Small Arrays:** `Insertion Sort`, `Tim Sort` (hybrid)
* **Best for Integers in Known Range:** `Counting Sort`, `Radix Sort`
* **In-place & Stable?**

  * ✅ In-place: Quick, Heap, Insertion, Selection
  * ✅ Stable: Merge, Insertion, Counting, Tim, Radix

Let me know if you want a decision tree for which to use when.


Resources:
- https://www.geeksforgeeks.org/dsa/sorting-algorithms/
- https://www.youtube.com/watch?v=rbbTd-gkajw 