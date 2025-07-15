# author: Kimble Ke
# date: 2025.7.15

# O(N) solution
def solution(n):
  total = 0
  for digit in str(n):
    total += 2 * int(digit)
  return total

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 DoubleDigitsSum_debug.py input.txt")
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