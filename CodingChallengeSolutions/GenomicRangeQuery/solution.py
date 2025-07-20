# author: Kimble Ke
# date: 2025.7.20
 
# O(N+M) Time, O(N) Space
def solution1(S, P, Q):
  n = len(S)
  m = len(P)
  # Initialize prefix sums for A, C, G (T is implied)
  prefix_A = [0] * (n + 1)
  prefix_C = [0] * (n + 1)
  prefix_G = [0] * (n + 1)
  
  for i in range(1, n + 1):
    prefix_A[i] = prefix_A[i - 1] + (1 if S[i - 1] == 'A' else 0)
    prefix_C[i] = prefix_C[i - 1] + (1 if S[i - 1] == 'C' else 0)
    prefix_G[i] = prefix_G[i - 1] + (1 if S[i - 1] == 'G' else 0)
  
  result = []
  for k in range(m):
    start = P[k]
    end = Q[k] + 1  # Convert to 1-based index
    
    # Check for A, C, G in order (T is default)
    if prefix_A[end] - prefix_A[start] > 0:
      result.append(1)
    elif prefix_C[end] - prefix_C[start] > 0:
      result.append(2)
    elif prefix_G[end] - prefix_G[start] > 0:
      result.append(3)
    else:
      result.append(4)
  return result
