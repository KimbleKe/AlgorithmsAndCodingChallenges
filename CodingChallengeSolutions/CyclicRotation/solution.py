# author: Kimble Ke
# date: 2025.7.15

# O(N) solution
def cyclic_rotation1(A, K):
  if not A:
    return A
  K = K % len(A)
  return A[-K:] + A[:-K]

# O(N x K) solution
def cyclic_rotation2(A, K):
  if not A:
    return A
  for _ in range(K):
    last_element = A[-1]
    for i in range(len(A)-1, 0, -1):
      A[i] = A[i-1]
    A[0] = last_element
  return A