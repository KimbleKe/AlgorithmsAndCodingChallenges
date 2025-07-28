# author: Kimble Ke
# date: 2025.7.28

# Time complexity: O(N)
# Space complexity: O(1)
def solution(A):
  N = len(A)
  for i in range(N // 2):
    k = N - i - 1
    A[i], A[k] = A[k], A[i]
  return A
