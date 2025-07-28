# author: Kimble Ke
# date: 2025.7.20
 
# O(N) Time, O(1) Space
def solution(A):
  # solution is based on math theory that slices of 4 or more numbers always 
  # contain a smaller slice with lower average, hence only slices of 2 or 3
  # elements need to be tested in the algorithm

  n = len(A)
  min_avg = float('inf')
  min_pos = 0

  for i in range(n - 1):
    # Check slice of length 2
    avg = (A[i] + A[i + 1]) / 2
    if avg < min_avg:
      min_avg = avg
      min_pos = i

    # Check slice of length 3 (if possible)
    if i < n - 2:
      avg = (A[i] + A[i + 1] + A[i + 2]) / 3
      if avg < min_avg:
        min_avg = avg
        min_pos = i
  return min_pos


