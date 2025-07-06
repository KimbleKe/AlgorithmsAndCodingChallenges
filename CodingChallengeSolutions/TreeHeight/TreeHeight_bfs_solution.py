# author: Kimble Ke
# date: 2025.7.6

# Below solution use breadth first search algorith, it has O(N) time complexity, and space complexity as O(W) in best case and O(N) in worst case
from dataclasses import dataclass
from typing import Optional
from collections import deque

@dataclass
class Tree:
  x: int = 0
  l: Optional["Tree"] = None
  r: Optional["Tree"] = None

def solution(T: Optional[Tree]) -> int:
  if T is None:
    return -1  # Empty tree has height -1 (by convention)

  queue = deque([T])
  height = -1

  while queue:
    level_size = len(queue)
    for _ in range(level_size):
      node = queue.popleft()
      if node.l:
        queue.append(node.l)
      if node.r:
        queue.append(node.r)
    height += 1

  return height
