# author: Kimble Ke
# date: 2025.7.15

# Time Complexity: O(NlogN)
def solution(A):
  A.sort()  # Sort the array in ascending order
  n = len(A)
  left, right = 0, n - 1
  min_abs = float('inf')
  
  while left <= right:
    current_sum = A[left] + A[right]
    current_abs = abs(current_sum)
    min_abs = min(min_abs, current_abs)
    
    # Move pointers to try to get a smaller sum
    if current_sum < 0:
      left += 1  # Need a larger sum (move left pointer right)
    else:
      right -= 1  # Need a smaller sum (move right pointer left)
  
  return min_abs

