# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(N) Space
def solution(S):
  stack = []
  bracket_pairs = {')': '(', '}': '{', ']': '['}
  
  for char in S:
    if char in bracket_pairs.values():  # Opening bracket
      stack.append(char)
    elif char in bracket_pairs.keys():  # Closing bracket
      if not stack or stack.pop() != bracket_pairs[char]:
        return 0
    else:  # Invalid character (optional, if input is guaranteed clean)
      return 0
  
  return 1 if not stack else 0
