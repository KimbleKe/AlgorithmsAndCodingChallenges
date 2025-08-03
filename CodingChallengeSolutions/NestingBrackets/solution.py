# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(1) Space
def solution(S):
  balance = 0
  for char in S:
    if char == '(':
      balance += 1
    else:
      balance -= 1
      if balance < 0:
        return 0
  return 1 if balance == 0 else 0

##########################################

# Time complexity - O(N)
# Space complexity - O(N) 
def solution1(S):
  stack = []
  bracket_pairs = {'(': ')'}
  
  for char in S:
    if char in bracket_pairs.keys():  # opening bracket
      stack.append(char)
    elif char in bracket_pairs.values():  # closing bracket
      if not stack or bracket_pairs[stack.pop()] != char:
        return 0
    else:  # invalid character (optional, if input is guaranteed clean)
      return 0
  
  return 1 if not stack else 0