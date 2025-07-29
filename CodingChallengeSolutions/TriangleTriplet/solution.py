# author: Kimble Ke
# date: 2025.7.21
 
# O(NlogN) Time, O(1) Space
def solution(A):
  A.sort()
  for i in range(len(A) - 2):
    if A[i] + A[i+1] > A[i+2]:
      return 1
  return 0

#####################################

# O(NlogN) Time, O(1) Space
def valid_triangle_triplet(A,P,Q,R):
  if P<Q<R and A[P]+A[Q]>A[R] and A[Q]+A[R]>A[P] and A[R]+A[P]>A[Q]:
    return True
  return False

def solution1(A):
  A.sort()
  for i in range(len(A)-2):
    if valid_triangle_triplet(A, i, i+1, i+2):
      return 1
  return 0