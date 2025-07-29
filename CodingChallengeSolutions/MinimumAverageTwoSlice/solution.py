# author: Kimble Ke
# date: 2025.7.20
 
# O(N) Time, O(1) Space, optimal solution
def solution(A):
  """
    solution is based on math theory that slices of 4 or more numbers always 
    contain a smaller slice with lower average, hence only slices of 2 or 3
    elements need to be tested in the algorithm
  """

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

# O(N) Time, O(N) Space
# below solution use prefix sum technique, but not the optimal solution
def solution1(A):
    n = len(A)
    prefix_sum = [0]*(n+1)
    min_avg = float('inf')
    smallest_starting_pos = 0

    for i in range(n):
      prefix_sum[i+1] = prefix_sum[i] + A[i]

    for i in range(n-1):
      # Check slice of length 2
      avg = (prefix_sum[i+2] - prefix_sum[i]) / 2
      if avg < min_avg:
        min_avg = avg
        smallest_starting_pos = i

      # Check slice of length 3 (if possible)
      if i < n - 2:
        avg = (prefix_sum[i+3] - prefix_sum[i]) / 3
        if avg < min_avg:
          min_avg = avg
          smallest_starting_pos = i

    return smallest_starting_pos

