from solution import solution 

# print input and output
if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    K,A = eval(line) 

  print("######## input ########")
  print("A=" + str(A) + ",K=" + str(K))

  result = solution(K,A)

  print("######## result ########")
  print("result is " + str(result))

