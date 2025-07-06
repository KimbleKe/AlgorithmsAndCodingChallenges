Assume the graph/tree has below data

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

---

### ✅ Summary Table:

| Search Algorithm     | Uses Heuristic? | Weighted Graph? | Complete? | Optimal? | Time Complexity |
| -------------------- | --------------- | --------------- | --------- | -------- | --------------- |
| DFS                  | ❌               | ❌               | ❌         | ❌        | O(V + E)        |
| BFS                  | ❌               | ❌               | ✅         | ✅        | O(V + E)        |
| IDDFS                | ❌               | ❌               | ✅         | ✅        | O(b^d)          |
| Best-First (Greedy)  | ✅               | ✅               | ❌         | ❌        | O(E log V)      |
| Dijkstra             | ❌               | ✅               | ✅         | ✅        | O(E log V)      |
| Uniform Cost Search  | ❌               | ✅               | ✅         | ✅        | O(E log V)      |
| Bidirectional Search | ❌               | ❌               | ✅         | ✅        | O(b^(d/2))      |

---
