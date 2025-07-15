# author: Kimble Ke
# date: 2025.7.2
 
# O(N) solution
def solution(A):
  i=0
  count=0
 
  while count<len(A):
    count+=1
    if A[i]!=-1:
      i=A[i]
    else:
      break
 
  return count

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