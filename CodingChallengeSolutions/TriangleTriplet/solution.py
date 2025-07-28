# author: Kimble Ke
# date: 2025.7.21
 
# O(NlogN) Time, O(1) Space
def solution(A):
  A.sort()
  for i in range(len(A) - 2):
    if A[i] + A[i+1] > A[i+2]:
      return 1
  return 0
