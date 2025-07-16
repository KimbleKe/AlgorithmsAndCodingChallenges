# author: Kimble Ke
# date: 2025.7.15

# O(N) solution
def solution(n):
  result = []
  for digit in str(n):
    new_digit = (int(digit) + 1) % 10
    result.append(str(new_digit))
  return int(''.join(result))  # Removes leading zero if needed

###############################################################################
# print input and output
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 IncreaseTheDigits_debug.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        line = f.read().strip()
        n = eval(line) 

    result = solution(n)

    print("######## input ########")
    print("input  is " + str(n))
    print("######## result ########")
    print("result is " + str(result))