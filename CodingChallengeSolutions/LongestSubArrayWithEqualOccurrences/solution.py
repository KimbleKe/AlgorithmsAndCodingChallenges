# author: Kimble Ke
# date: 2025.8.8

# Time complexity: O(N)
# Space complexity: O(1)
def solution(X, Y, A):
  N = len(A)
  result = -1
  nX = 0
  nY = 0
  for i in range(N):
    if A[i] == X:
      nX += 1
    if A[i] == Y:
      nY += 1
    if nX == nY:
      result = i
  return result
