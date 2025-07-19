# author: Kimble Ke
# date: 2025.7.16
 
# Time Complexity O(N)
def solution1(X, A):
  covered = set()
  for time, position in enumerate(A):
    if position <= X:
      covered.add(position)
      if len(covered) == X:
        return time
  return -1

