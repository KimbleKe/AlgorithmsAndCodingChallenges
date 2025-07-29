# author: Kimble Ke
# date: 2025.7.20
 
# O(NlogN) Time, O(1) Space, preferred solution
def solution(A):
  A.sort()
  return max(
    A[-1] * A[-2] * A[-3],    # Case 1: All positive/largest
    A[0] * A[1] * A[-1]       # Case 2: Two negatives + largest positive
  )
