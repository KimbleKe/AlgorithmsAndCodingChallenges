# author: Kimble Ke
# date: 2025.7.20
 
# O(NlogN) Time, O(1) Space, preferred solution
def solution(A):
  A.sort()
  return max(
    A[-1] * A[-2] * A[-3],    # Case 1: All positive/largest
    A[0] * A[1] * A[-1]       # Case 2: Two negatives + largest positive
  )

# O(N) Time, O(1) Space
def solution2(A):
  min1 = min2 = float('inf')
  max1 = max2 = max3 = -float('inf')
  
  for num in A:
    # Update max values
    if num > max1:
      max3, max2, max1 = max2, max1, num
    elif num > max2:
      max3, max2 = max2, num
    elif num > max3:
      max3 = num
    
    # Update min values
    if num < min1:
      min2, min1 = min1, num
    elif num < min2:
      min2 = num
  
  return max(
    max1 * max2 * max3,
    min1 * min2 * max1
  )