# author: Kimble Ke
# date: 2025.7.6

# O(N) solution
def solution(S):
  N = len(S)
  if N == 0:
    return -1
  if N == 1:
    return 0
  
  i = N // 2 # 7/2=3.5, 7//2=3, 7mod2=1
  if S[0:i] == S[i+1:][::-1]: # reverse S[i+1:] using [::-1]
    return i
  else:
    return -1