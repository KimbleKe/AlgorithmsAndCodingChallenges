from solution import solution1 

# print input and output
if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    S,P,Q = eval(line) 

  print("######## input ########")
  print("S,P,Q=" + str(S) + "," + str(P) + "," + str(Q))

  result = solution1(S,P,Q)

  print("######## result ########")
  print("result is " + str(result))

