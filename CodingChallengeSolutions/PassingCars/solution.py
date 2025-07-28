# author: Kimble Ke
# date: 2025.7.20
 
# O(N) Time, O(1) Space
def solution(A):
  east_count = 0
  passing_pairs = 0
  
  for car in A:
    if car == 0:
      east_count += 1
    else:
      passing_pairs += east_count
      if passing_pairs > 1_000_000_000:
        return -1
  return passing_pairs


