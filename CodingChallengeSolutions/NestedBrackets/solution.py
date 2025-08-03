# author: Kimble Ke
# date: 2025.7.21
 
# Time complexity - O(N)
# Space complexity - O(N) 
def solution(S):
  stack = []
  bracket_pairs = {'(': ')', '{': '}', '[': ']'}
  
  for char in S:
    if char in bracket_pairs.keys():  # opening bracket
      stack.append(char)
    elif char in bracket_pairs.values():  # closing bracket
      if not stack or bracket_pairs[stack.pop()] != char:
        return 0
    else:  # invalid character (optional, if input is guaranteed clean)
      return 0
  
  return 1 if not stack else 0
