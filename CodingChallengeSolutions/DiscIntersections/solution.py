# author: Kimble Ke
# date: 2025.7.20
 
# O(NlogN) Time, O(N) Space
def solution(A):
  n = len(A)
  start_points = []
  end_points = []
  
  for i in range(n):
    start_points.append(i - A[i])
    end_points.append(i + A[i])
  
  start_points.sort()
  end_points.sort()
  
  intersections = 0
  active_discs = 0
  end_ptr = 0
  
  for start_ptr in range(n):
    while end_ptr < n and end_points[end_ptr] < start_points[start_ptr]:
      active_discs -= 1
      end_ptr += 1
    intersections += active_discs
    active_discs += 1
    
    if intersections > 10_000_000:
      return -1
  
  return intersections