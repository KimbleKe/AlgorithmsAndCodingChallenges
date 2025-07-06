# author: Kimble Ke
# date: 2025.7.6

# Below solution use depth first search algorith, it has best case O(log(N)) for balanced tree and worst case O(N) for skewed tree
from dataclasses import dataclass
from typing import Optional
 
@dataclass
class Tree:
  x: int = 0
  l: Optional["Tree"] = None
  r: Optional["Tree"] = None
 
def solution(T: Tree) -> int:
  if T is None:
    return -1 # Convention: height of empty tree is -1

  max_height = 0  # Global variable to track longest zigzag
  
  def dfs(node: Optional[Tree], length: int):
    nonlocal max_height

    if not node:
      return

    max_height = max(max_height, length)

    dfs(node.l, length + 1)
    dfs(node.r, length + 1)

  dfs(T, 0)

  return max_height