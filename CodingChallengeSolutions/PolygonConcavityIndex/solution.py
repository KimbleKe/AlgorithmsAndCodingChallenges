# author: Kimble Ke
# date: 2025.7.8
 
# O(N) Time, O(N) Space solution
from dataclasses import dataclass
from typing import List, Set

@dataclass
class Point2D:
  x: int
  y: int

def cross(o, a, b):
  return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def convex_hull(points: List[Point2D]) -> List[Point2D]:
  # Sort points by x, then by y
  points = sorted(points, key=lambda p: (p.x, p.y))
  n = len(points)
  if n <= 1:
    return points

  lower = []
  for p in points:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
      lower.pop()
    lower.append(p)

  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
      upper.pop()
    upper.append(p)

  # Concatenate and remove last point of each to avoid duplication
  full_hull = lower[:-1] + upper[:-1]
  return full_hull

def solution1(A) -> int:
  n = len(A)
  if n < 3:
    return -1

  # Compute convex hull
  hull = convex_hull(A)

  # Build a set of convex hull points for quick lookup
  hull_set: Set[tuple] = set((p.x, p.y) for p in hull)

  # Find a point in A that is not on the convex hull
  for i, pt in enumerate(A):
    if (pt.x, pt.y) not in hull_set:
      return i

  return -1
