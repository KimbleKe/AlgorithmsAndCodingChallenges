# author: Kimble Ke
# date: 2025.7.15

# Time Complexity: O(N). Worst case: N+1 is missing
def missing_integer(A):
  seen = set(A) # store all positive numbers in a set for O(1) lookup
  for i in range(1, len(A)+2): 
    if i not in seen:
      return i

###############################################################################
# print input and output    
if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    # example input file contains (2, [3, 5, 7, 6, 3]) where K = 2 and A = [3, 5, 7, 6, 3]
    print("Usage: python3 MissingInteger_debug.py input.txt")
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    A = eval(line) 

  result = missing_integer(A)

  print("######## input ########")
  print("A=" + str(A))
  print("######## result ########")
  print("result is " + str(result))