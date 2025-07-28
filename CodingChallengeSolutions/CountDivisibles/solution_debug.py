from solution import solution 

# print input and output
if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    A,B,K = eval(line) 

  print("######## input ########")
  print("A,B,K=" + str(A) + "," + str(B) + "," + str(K))

  result = solution(A,B,K)

  print("######## result ########")
  print("result is " + str(result))

