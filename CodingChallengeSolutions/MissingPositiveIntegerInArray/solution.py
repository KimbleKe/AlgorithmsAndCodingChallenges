# author: Kimble Ke
# date: 2025.7.19
 
# O(N) Time, O(N) Space
def solution1(A):
  seen = set(A)
  for i in range(1, len(A)+2):
    if i not in seen:
      return i
    
# O(N) Time, O(1) Space
def solution2(A):
  n = len(A)
  
  # Step 1: Replace non-positives with (n+1) (irrelevant)
  for i in range(n):
    if A[i] <= 0:
      A[i] = n + 1
  
  # Step 2: Mark indices as "seen" by making A[abs(num)-1] negative
  for num in A:
    if abs(num) <= n:
      A[abs(num) - 1] = -abs(A[abs(num) - 1])
  
  # Step 3: Find the first positive index
  for i in range(n):
    if A[i] > 0:
      return i + 1
  
  # If all 1..n are present, return n+1
  return n + 1


