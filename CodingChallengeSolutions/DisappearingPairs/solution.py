# author: Kimble Ke
# date: 2025.7.8
 
# O(N) Time, O(N) Space solution
def solution1(S):
  stack = []
  for ch in S:
    if stack and stack[-1] == ch:
      stack.pop()  # Remove the pair
    else:
      stack.append(ch)  # Add current character
  return ''.join(stack)
