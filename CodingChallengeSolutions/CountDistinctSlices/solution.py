# author: Kimble Ke
# date: 2025.7.24
 
# Time complexity O(N)
# Space complexity O(M+1)
def solution(M, A):
  seen = [False] * (M + 1)
  P = 0
  total = 0

  for Q in range(len(A)):
    while seen[A[Q]]:
      seen[A[P]] = False # remove A[P] from the sliding window, so it's no longer seen and the value can be used again later, basically move window forward
      P += 1
    seen[A[Q]] = True
    total += (Q - P + 1)  # every time we see a new Q, count new slices ending at Q and beginning at P
    
    if total >= 1_000_000_000:
      return 1_000_000_000

  return total
