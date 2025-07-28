# author: Kimble Ke
# date: 2025.7.16
 
# Time complexity: O(N+M)
# Space complexity: O(N)
def solution(N, A):
  counters = [0] * N
  current_max = 0
  last_max_counter = 0
  
  for num in A:
    if 1 <= num <= N:    # scenario 1, if A[k]==X, counters[X-1]++
      # Apply lazy update if counter is stale
      if counters[num - 1] < last_max_counter:
        counters[num - 1] = last_max_counter

      counters[num - 1] += 1
      
      # Update current_max
      if counters[num - 1] > current_max:
        current_max = counters[num - 1]
        
    elif num == N + 1:    # scenario 2, if A[K]==N+1, set all counters to last max counter
      # Set all counters to current_max (lazy update)
      last_max_counter = current_max
  
  # Apply last_max_counter to any remaining stale counters
  for i in range(N):
    if counters[i] < last_max_counter:
      counters[i] = last_max_counter
  
  return counters
