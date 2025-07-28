# author: Kimble Ke
# date: 2025.7.16
 
# Time complexity: O(N)
# Space complexity: O(X)
def solution(X, A):
  covered = set()
  for time, position in enumerate(A):
    if position <= X:
      covered.add(position)
      if len(covered) == X:
        return time
  return -1
