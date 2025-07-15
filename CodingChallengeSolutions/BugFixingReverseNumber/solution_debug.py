# author: Kimble Ke
# date: 2025.7.15

# O(N) solution
def solution(n):
  return int(str(n)[::-1])

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 BugFixingReverseNumber_debug.py input.txt")
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