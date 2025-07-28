# author: Kimble Ke
# date: 2025.7.20
 
# O(N+M) Time, O(N) Space
def solution(S, P, Q):
  n = len(S)
  m = len(P)
  a=c=g=t=0
  result = []

  A = [0] * n
  C = [0] * n
  G = [0] * n
  T = [0] * n
  
  # break S string into 4 nucleotide arrays - A,C,G,T arrays
  for i in range(0, n):
    a+=1 if S[i] == 'A' else 0
    A[i] = a

    c+=1 if S[i] == 'C' else 0
    C[i] = c

    g+=1 if S[i] == 'G' else 0
    G[i] = g

    t+=1 if S[i] == 'T' else 0
    T[i] = t

  # if nucleotide appear between Q[k] and P[k], then append min nucleotide into result array
  for k in range(m):
    start = P[k]
    end = Q[k]  
    
    # order is important as nucleotide impact is ranked with A < C < G < T 
    if A[end] > A[start] or S[start] == 'A':
      result.append(1)
    elif C[end] > C[start] or S[start] == 'C':
      result.append(2)
    elif G[end] > G[start] or S[start] == 'G':
      result.append(3)
    elif T[end] > T[start] or S[start] == 'T':
      result.append(4)

  return result
