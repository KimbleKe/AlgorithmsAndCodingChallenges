# author: Kimble Ke
# date: 2025.7.15
 
# Time Complexity O(N)
def solution1(A):
  result = 0
  for num in A:
    result ^= num  # XOR all elements
  return result

