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
