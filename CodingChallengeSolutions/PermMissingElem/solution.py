# author: Kimble Ke
# date: 2025.7.15
 
# Time Complexity O(N)
def solution(A):
  n = len(A)
  total = (n + 1) * (n + 2) // 2  # Sum of 1..(N+1)
  return total - sum(A)  # Missing element

