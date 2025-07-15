# author: Kimble Ke
# date: 2025.7.15
 
# O(logN) solution
def solution(N):
  max_gap = 0
  current_gap = 0
  found_one = False
  
  while N > 0:
    if N & 1:  # Check if the last bit is 1
      if found_one:
        max_gap = max(max_gap, current_gap)
      else:
        found_one = True
      current_gap = 0
    else:  # Last bit is 0
      if found_one:
        current_gap += 1
    N = N // 2  # Right shift, equivalent to N >>= 1
  
  return max_gap

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

