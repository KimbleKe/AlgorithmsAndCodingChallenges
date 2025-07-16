# author: Kimble Ke
# date: 2025.7.15
 
# Time Complexity O(N)
def solution(A):
  result = 0
  for num in A:
    result ^= num  # XOR all elements
  return result

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

