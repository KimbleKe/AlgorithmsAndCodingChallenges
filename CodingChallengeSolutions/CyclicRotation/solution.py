# author: Kimble Ke
# date: 2025.7.15

# Time complexity: O(N)
# Space complexity: O(N)
def solution1(A, K):
  if not A:
    return A
  K = K % len(A)
  return A[-K:] + A[:-K]
