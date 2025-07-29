# author: Kimble Ke
# date: 2025.7.20
 
# O(N+M) Time, O(N) Space
# optimised solution using prefix sum technique
def solution(S, P, Q):
	# Initialize prefix sums for each nucleotide (A, C, G, T)
	# Each prefix array has length (n+1) to store cumulative counts
	n = len(S)
	prefix = {
		'A': [0] * (n + 1),
		'C': [0] * (n + 1),
		'G': [0] * (n + 1),
		'T': [0] * (n + 1)
	}

	# Build prefix sums: O(N) time
	for i, char in enumerate(S):
		for key in prefix:
			# Increment count if current character matches the nucleotide
			prefix[key][i+1] = prefix[key][i] + (1 if key == char else 0)
	
	result = []
	# Process each query: O(M) time (M = number of queries)
	for i in range(len(P)):
		start, end = P[i], Q[i] + 1  # Convert to 1-based indexing for prefix sums
		
		# Check nucleotides in order of priority (A=1, C=2, G=3, T=4)
		if prefix['A'][end] - prefix['A'][start] > 0:
			result.append(1)  # At least one 'A' in the range
		elif prefix['C'][end] - prefix['C'][start] > 0:
			result.append(2)  # No 'A's, but at least one 'C'
		elif prefix['G'][end] - prefix['G'][start] > 0:
			result.append(3)  # No 'A's or 'C's, but at least one 'G'
		elif prefix['T'][end] - prefix['T'][start] > 0:
			result.append(4)  # Only 'T's in the range
		else:
			pass

	return result


#######################################################

# O(N+M) Time, O(N) Space
def solution1(S, P, Q):
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

# Time complexity: O(N * M)
# Space complexity: O(N + M)
# algorithm: direct min-slicing; this solution is to help understand but might not meet efficiency requirement
def solution2(S, P, Q):
  m = len(P)
  impact_factor = {'A':1,'C':2,'G':3,'T':4}  # impact factor of nucleotide type 核苷酸影响因子
  S_impact = []
  result = []

  for char in S:
    S_impact.append(impact_factor[char]) # O(N) time, O(N) space

  for i in range(m):
    result.append(min(S_impact[P[i]:Q[i]+1])) # O(M*N) time in worst case, O(N + M) space

  return result

# Note for the solution
# S = CAGCCTA, S_impact = [2,1,3,2,2,4,1]
# P = [2,5,0], Q = [4,5,6]
# min{idx 2.. idx 4} = min{3,2,2} = 2
# min{idx 5 .. 5} = min{4} = 4
# min{idx 0 .. 6} = min{2,1,3,2,2,4,1} = 1
# result = [2,4,1]