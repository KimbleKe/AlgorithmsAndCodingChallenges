# author: Kimble Ke
# date: 2025.7.15
 
# Time Complexity: O(N)
# Space Complexity: O(1)
def solution(A):
  """
  Property of XOR:
    a ^ a = 0 (Any number XOR itself cancels out)
    a ^ 0 = a (XOR with 0 returns the original number)
    XOR is commutative and associative (a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b)
  """
  result = 0
  for num in A:
    result ^= num  # bitwise XOR operation between two integers across all elements
  return result
