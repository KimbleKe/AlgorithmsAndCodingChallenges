# author: Kimble Ke
# date: 2025.7.15
 
# Time complexity: O(N)
# Space complexity: O(1)
def solution(A):
  total = sum(A)
  left_sum = 0
  min_diff = float('inf')
  
  for i in range(len(A)-1):
    left_sum += A[i]
    right_sum = total - left_sum
    current_diff = abs(left_sum - right_sum)
    if current_diff < min_diff:
      min_diff = current_diff
      if min_diff == 0:  # Early exit if perfect balance found
        break
  
  return min_diff
