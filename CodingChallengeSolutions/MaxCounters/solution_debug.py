# author: Kimble Ke
# date: 2025.7.16
 
# Time Complexity O(N)
def solution(X, A):
  covered = set()
  for time, position in enumerate(A):
    if position <= X:
      covered.add(position)
      if len(covered) == X:
        return time
  return -1

###############################################################################
# print input and output
if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    X,A = eval(line) 

  result = solution(X,A)

  print("######## input ########")
  print("X=" + str(X) + ", A=" + str(A))
  print("######## result ########")
  print("result is " + str(result))

