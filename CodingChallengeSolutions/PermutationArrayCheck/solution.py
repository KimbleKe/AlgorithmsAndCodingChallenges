# author: Kimble Ke
# date: 2025.7.19
 
# O(N) Time, O(N) Space
def solution1(A):
  n = len(A)
  seen = set()
  for num in A:
    if num < 1 or num > n or num in seen:
      return 0
    seen.add(num)
  return 1


