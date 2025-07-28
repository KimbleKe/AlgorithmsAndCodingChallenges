# author: Kimble Ke
# date: 2025.7.15
 
# Time complexity: O(N)
# Space complexity: O(1)
def solution(A):
  n = len(A)
  total = (n + 1) * (n + 2) // 2  # Sum of 1..(N+1)
  return total - sum(A)  # Missing element

# Time complexity: O(NlogN)
# Space complexity: O(1)
def solution1(A):
  if not A:
    return 1
  A.sort()
  if A[0] != 1:
    return 1
  for i in range(len(A)-1):
    if A[i] + 1 != A[i+1]:
      return A[i] + 1
  return A[-1] + 1