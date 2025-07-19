from dataclasses import dataclass
from typing import Optional
from TreeHeight_bfs_solution import solution1

@dataclass
class Tree:
    x: int = 0
    l: Optional["Tree"] = None
    r: Optional["Tree"] = None

# Construct the tree from the image
A = Tree(
    x=5,
    l=Tree(
        x=3,
        l=Tree(x=20, l=None, r=None),
        r=Tree(x=21, l=None, r=None)
    ),
    r=Tree(
      x=10,
      l=Tree(x=1, l=None, r=None),
      r=None
    )
)

# print input and output
if __name__ == "__main__":
  print("######## input ########")
  print("A=" + str(A))

  result = solution1(A)

  print("######## result ########")
  print("result is " + str(result))

