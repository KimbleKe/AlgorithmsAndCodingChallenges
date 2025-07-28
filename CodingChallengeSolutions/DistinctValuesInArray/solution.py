# author: Kimble Ke
# date: 2025.7.20
 
# O(N) Time, O(N) Space (this is the preferred solution)
def solution(A):
  return len(set(A))

# O(NlogN) Time, O(1) Space
def solution2(A):
  if not A:
    return 0
  A.sort()
  distinct = 1
  for i in range(1, len(A)):
    if A[i] != A[i - 1]:
      distinct += 1
  return distinct