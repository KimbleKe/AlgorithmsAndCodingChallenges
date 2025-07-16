# author: Kimble Ke
# date: 2025.7.15
 
# Time Complexity O(N)
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

###############################################################################
# print input and output
if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    A = eval(line) 

  result = solution(A)

  print("######## input ########")
  print("A=" + str(A))
  print("######## result ########")
  print("result is " + str(result))

