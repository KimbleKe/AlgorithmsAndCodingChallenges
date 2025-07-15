# author: Kimble Ke
# date: 2025.7.15
 
# Time Complexity O(1)
def solution(X, D):
  if D == 0:
    return 0  # Edge case: no movement
  jumps = X // D
  if X % D != 0:
    jumps += 1
  return jumps

# print input and output
if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    X,D = eval(line) 

  result = solution(X,D)

  print("######## input ########")
  print("X=" + str(X) + ", D=" + str(D))
  print("######## result ########")
  print("result is " + str(result))

