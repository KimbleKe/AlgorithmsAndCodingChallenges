# author: Kimble Ke
# date: 2025.7.16
 
# Time Complexity O(N+M)
def solution(N, A):
  counters = [0] * N
  current_max = 0
  last_update = 0
  
  for num in A:
    if 1 <= num <= N:
      # Apply lazy update if counter is stale
      if counters[num - 1] < last_update:
        counters[num - 1] = last_update
      counters[num - 1] += 1
      # Update current_max
      if counters[num - 1] > current_max:
        current_max = counters[num - 1]
    elif num == N + 1:
      # Set all counters to current_max (lazy update)
      last_update = current_max
  
  # Apply last_update to any remaining stale counters
  for i in range(N):
    if counters[i] < last_update:
      counters[i] = last_update
  
  return counters

###############################################################################
# print input and output
if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    N,A = eval(line) 

  result = solution(N,A)

  print("######## input ########")
  print("N=" + str(N) + ", A=" + str(A))
  print("######## result ########")
  print("result is " + str(result))

