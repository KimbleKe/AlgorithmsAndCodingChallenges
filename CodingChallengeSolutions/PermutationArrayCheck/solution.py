# author: Kimble Ke
# date: 2025.7.20
 
# Time complexity: O(N)
# Space complexity: O(N)
def solution(A):
  n = len(A)
  seen = set()
  for num in A:
    if num < 1 or num > n or num in seen:
      return 0
    seen.add(num)
  return 1
