Here’s an **extended and refined version** of the comprehensive **Search Algorithms Table**, including:

* Any **missing standard algorithms**.
* **Space complexity** for each.
* Clear grouping and sorting for clarity.

---

## 🔍 1. **Array-Based Search Algorithms**

| Algorithm                    | Structure       | Best Time | Avg Time     | Worst Time | Space | Description                                          |
| ---------------------------- | --------------- | --------- | ------------ | ---------- | ----- | ---------------------------------------------------- |
| **Linear Search**            | Unsorted Array  | O(1)      | O(N)         | O(N)       | O(1)  | Sequentially checks all elements.                    |
| **Sentinel Linear Search**   | Unsorted Array  | O(1)      | O(N)         | O(N)       | O(1)  | Adds sentinel to avoid boundary checks.              |
| **Binary Search**            | Sorted Array    | O(1)      | O(log N)     | O(log N)   | O(1)  | Repeatedly halves search range.                      |
| **Meta Binary Search**       | Sorted Array    | O(1)      | O(log N)     | O(log N)   | O(1)  | Binary search using bit manipulation.                |
| **One-Sided Binary Search**  | Monotonic Array | O(1)      | O(log N)     | O(log N)   | O(1)  | Prunes one side aggressively using problem logic.    |
| **Ubiquitous Binary Search** | Monotonic Fn    | -         | O(log N)     | O(log N)   | O(1)  | Binary search on answers (not arrays).               |
| **Jump Search**              | Sorted Array    | O(1)      | O(√N)        | O(√N)      | O(1)  | Jump ahead in blocks, then linear search.            |
| **Exponential Search**       | Sorted Array    | O(1)      | O(log i)     | O(log i)   | O(1)  | Exponentially find range, then binary search.        |
| **Fibonacci Search**         | Sorted Array    | O(1)      | O(log N)     | O(log N)   | O(1)  | Uses Fibonacci gaps to divide the array.             |
| **Ternary Search**           | Unimodal Array  | O(1)      | O(log N)     | O(log N)   | O(1)  | Divide into 3 segments. Good for unimodal f(x).      |
| **Interpolation Search**     | Uniform Sorted  | O(1)      | O(log log N) | O(N)       | O(1)  | Estimate position using interpolation (value-based). |
| **Block Search**             | Index + Block   | O(1)      | O(√N)        | O(√N)      | O(√N) | Indexing blocks + linear search within block.        |

---

## 🌳 2. **Tree & Graph-Based Search Algorithms**

| Algorithm                   | Structure      | Time                        | Space      | Description                                        |
| --------------------------- | -------------- | --------------------------- | ---------- | -------------------------------------------------- |
| **Depth-First Search**      | Graph/Tree     | O(V + E)                    | O(H)       | Recursively or via stack explore deep before wide. |
| **Breadth-First Search**    | Graph/Tree     | O(V + E)                    | O(W)       | Uses queue to explore level by level.              |
| **Iterative Deepening DFS** | Graph          | O(V + E)                    | O(H)       | Combines DFS depth-limit and BFS completeness.     |
| **Bidirectional Search**    | Graph          | O(b^(d/2))                  | O(b^(d/2)) | Searches from both ends.                           |
| **A* Search*\*              | Weighted Graph | O(E) (depends on heuristic) | O(V)       | Uses f(n) = g(n) + h(n) for optimal pathfinding.   |
| **Dijkstra’s Algorithm**    | Weighted Graph | O((V + E)log V)             | O(V)       | Shortest path with non-negative weights.           |
| **Bellman-Ford**            | Weighted Graph | O(VE)                       | O(V)       | Works with negative edges.                         |
| **Best-First Search**       | Graph          | O(E)                        | O(V)       | Uses only heuristic h(n). Greedy approach.         |
| **IDA\***                   | Tree/Graph     | O(b^d)                      | O(d)       | Memory-optimal variant of A\*.                     |
| **Uniform Cost Search**     | Weighted Graph | O((V + E)log V)             | O(V)       | Like Dijkstra but allows priority queue for cost.  |

> H = tree height; W = max width; V = vertices; E = edges; b = branching factor; d = depth

---

## 🧵 3. **String/Search Indexing Algorithms**

| Algorithm                    | Input Type        | Time         | Space    | Description                                    |
| ---------------------------- | ----------------- | ------------ | -------- | ---------------------------------------------- |
| **Trie Search**              | Strings           | O(L)         | O(N·L)   | Prefix tree. Fast lookup and autocomplete.     |
| **Aho-Corasick**             | Multi-pattern str | O(N + M + Z) | O(M)     | Multi-pattern match with trie + failure links. |
| **KMP (Knuth-Morris-Pratt)** | String            | O(N + M)     | O(M)     | Prefix table to avoid re-checking.             |
| **Rabin-Karp**               | String            | O(N + M) avg | O(1)     | Uses rolling hash to match substring.          |
| **Z-Algorithm**              | String            | O(N + M)     | O(N + M) | Fast pre-processing for pattern matching.      |

---

## ✅ Summary of Complexities (Best Case Scenarios)

| Class              | Best Time     | Best Space |
| ------------------ | ------------- | ---------- |
| Array-based Search | O(1)–O(log N) | O(1)–O(K)  |
| Graph Search       | O(V + E)      | O(H)–O(V)  |
| String Search      | O(N + M)      | O(M)–O(N)  |

---

## ✅ Additional Mentions

| Algorithm               | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| **Monte Carlo Search**  | Randomized tree sampling (e.g., game AI) |
| **Beam Search**         | Heuristic breadth-limited search         |
| **Hill Climbing**       | Greedy optimization search               |
| **Simulated Annealing** | Probabilistic hill-climbing variant      |

---

