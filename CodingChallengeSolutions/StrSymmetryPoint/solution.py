# author: Kimble Ke
# date: 2025.7.6

# O(N) solution#1
def solution1(S):
  N = len(S)
  if N == 0:
    return -1
  if N == 1:
    return 0

  for i in range(N):
    l, r = i - 1, i + 1
    match = True
    while l >= 0 and r < N:
      if S[l] != S[r]:
        match = False
        break
      l -= 1
      r += 1
    if match and l == -1 and r == N:
      return i
    elif match and (l < 0 or r >= N):
      return i
  return -1

# O(N) solution#2
def solution2(S):
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