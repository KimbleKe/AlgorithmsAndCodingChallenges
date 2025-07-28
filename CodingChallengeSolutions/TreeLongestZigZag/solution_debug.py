from dataclasses import dataclass
from typing import Optional
from solution import solution

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
    l=Tree(
      x=20, 
      l=Tree(
        x=6, 
        l=None, 
        r=None
      ), 
      r=None
    ),
    r=None
  ),
  r=Tree(
    x=10,
    l=Tree(
      x=1, 
      l=None, 
      r=None
    ),
    r=Tree(
      x=15, 
      l=Tree(
        x=30, 
        l=None, 
        r=Tree(
          x=9, 
          l=None, 
          r=None
        )
      ), 
      r=Tree(
        x=8, 
        l=None, 
        r=None
      )
    )
  )
)

# print input and output
if __name__ == "__main__":
  print("######## input ########")
  print("A=" + str(A))

  result = solution(A)

  print("######## result ########")
  print("result is " + str(result))

