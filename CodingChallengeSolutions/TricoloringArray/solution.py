# author: Kimble Ke
# date: 2025.8.8



def solution(A):
	N = len(A)
	if N == 0 or not A:
		return "impossible"
	
	def backtrack(idx, sumR, sumG, sumB, stableTricoloring):
		if idx == N:
			if sumR == sumG == sumB:
				return "".join(stableTricoloring)
			return None
		
    # Try B
		stableTricoloring.append('B')
		r = backtrack(idx + 1, sumR, sumG, sumB + A[idx], stableTricoloring)
		if r: return r
		stableTricoloring.pop()
		
    # Try G
		stableTricoloring.append('G')
		r = backtrack(idx + 1, sumR, sumG + A[idx], sumB, stableTricoloring)
		if r: return r
		stableTricoloring.pop()
		
		# Try R
		stableTricoloring.append('R')
		r = backtrack(idx + 1, sumR + A[idx], sumG, sumB, stableTricoloring)
		if r: return r
		stableTricoloring.pop()
		
		return None

	stableTricoloringOutput = backtrack(0, 0, 0, 0, [])
	
	return stableTricoloringOutput if stableTricoloringOutput else "impossible"
