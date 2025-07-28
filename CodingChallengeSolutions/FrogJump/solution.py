# author: Kimble Ke
# date: 2025.7.15
 
# Time complexity: O(1)
# Space complexity: O(1)
def solution(X,Y,D):
  if D == 0:
    return 0  # Edge case: no movement
  jumps = (Y-X) // D
  if (Y-X) % D != 0:
    jumps += 1
  return jumps
