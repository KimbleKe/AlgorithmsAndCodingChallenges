from dataclasses import dataclass
from solution import solution

@dataclass
class Point2D:
  x: int
  y: int

A = [
  Point2D(0, 0),
  Point2D(2, 0),
  Point2D(2, 2),
  Point2D(1, 1),  # Concave point
  Point2D(0, 2)
]

# print input and output
if __name__ == "__main__":
  print("######## input ########")
  print("A=" + str(A))

  result = solution(A)

  print("######## result ########")
  print("result is " + str(result))

