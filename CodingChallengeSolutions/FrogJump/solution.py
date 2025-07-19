# author: Kimble Ke
# date: 2025.7.15
 
# Time Complexity O(1)
def solution1(X, D):
  if D == 0:
    return 0  # Edge case: no movement
  jumps = X // D
  if X % D != 0:
    jumps += 1
  return jumps

