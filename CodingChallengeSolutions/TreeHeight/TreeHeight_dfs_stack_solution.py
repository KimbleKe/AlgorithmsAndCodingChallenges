# author: Kimble Ke
# date: 2025.7.6

# Iterative DFS using Stack — O(N) time, O(H) space. Manual stack avoids recursion depth issues. Optimal in time and space without recursion
from dataclasses import dataclass
from typing import Optional

@dataclass
class Tree:
  x: int = 0
  l: Optional["Tree"] = None
  r: Optional["Tree"] = None

def solution1(T) -> int:
  if T is None:
    return -1  # Convention: height of empty tree is -1

  stack = [(T, 0)]  # (node, current_depth)
  max_height = 0

  while stack:
    node, depth = stack.pop()
    max_height = max(max_height, depth)

    if node.l:
      stack.append((node.l, depth + 1))
    if node.r:
      stack.append((node.r, depth + 1))

  return max_height
