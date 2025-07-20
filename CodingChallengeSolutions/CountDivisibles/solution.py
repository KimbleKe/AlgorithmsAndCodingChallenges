# author: Kimble Ke
# date: 2025.7.20
 
# O(1) Time, O(1) Space
def solution1(A, B, K):
  if K == 0:
    return 0  # Handle invalid case (though K ≥ 1 per constraints)
  
  result = (B // K) - (A // K)

  if (A % K == 0):
    result+=1

  return result
