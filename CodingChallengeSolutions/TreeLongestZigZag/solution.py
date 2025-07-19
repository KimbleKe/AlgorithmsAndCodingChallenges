# author: Kimble Ke
# date: 2025.7.3

# O(N) solution
from dataclasses import dataclass
from typing import Optional
 
@dataclass
class Tree:
  x: int = 0
  l: Optional["Tree"] = None
  r: Optional["Tree"] = None
 
def solution1(T) -> int:
  max_zigzag = 0  # Global variable to track longest zigzag
  
  def dfs(node: Optional[Tree], from_left: bool, turns: int):
    nonlocal max_zigzag

    if not node:
      return

    max_zigzag = max(max_zigzag, turns)

    if from_left:
      dfs(node.r, False, turns + 1) # Go from left to right, 1 turn, hence turns+1
      dfs(node.l, True, turns) # Go left again, no turn, turns remain the same
    else:
      dfs(node.l, True, turns + 1) # Go from right to left, 1 turn, hence turns+1
      dfs(node.r, False, turns) # Go right again, no turn, turns remain the same

  def traverse(node: Optional[Tree]):
    if not node:
      return

    # Start from root, try both directions
    dfs(node.l, True, 0) # start going left
    dfs(node.r, False, 0) # start going right

  traverse(T)

  return max_zigzag