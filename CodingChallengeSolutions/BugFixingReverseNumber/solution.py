# author: Kimble Ke
# date: 2025.7.15

# Time complexity - O(N)
# Space complexity - O(N)
def solution(n):
  return int(str(n)[::-1])

# Note: (this is cleanest solution, best balance of speed and readability)
# Syntax Breakdown:
  # sequence[start:stop:step]
    # start: Index to begin (default: 0).
    # stop: Index to end (default: end of sequence).
    # step: Interval between elements (default: 1).
  # Negative step (e.g., -1): Reverses the sequence.
# Also, Slicing ([::-1]) is slightly faster in practice due to Python’s optimizations

############################################################

# Time complexity - O(N)
# Space complexity - O(N)
def solution1(n):
  string = str(n)
  return int(''.join(reversed(string)))

############################################################

# Time complexity - O(N)
# Space complexity - O(N)
def solution2(n):
  string = str(n)
  length = len(string)
  stack = ['0']*length
  i = 0
  while i<length//2:
    stack[i]=str(string[length-1-i])
    stack[length-1-i]=str(string[i])
    i+=1
  return int(''.join(stack))
