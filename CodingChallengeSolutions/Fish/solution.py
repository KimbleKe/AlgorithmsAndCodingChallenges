# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(N) Space
def solution(A, B):
  stack = []
  survivors = 0
  
  for i in range(len(A)):
    if B[i] == 1:  # Downstream fish
      stack.append(A[i])
    else:  # Upstream fish
      while stack:
        if stack[-1] < A[i]:  # Downstream fish eaten
          stack.pop()
        else:  # Upstream fish eaten
          break
      else:  # All downstream fish eaten
        survivors += 1
  
  return survivors + len(stack)