# author: Kimble Ke
# date: 2025.8.8

def solution(A):
	N = len(A)
	if N == 0:
		return ""
	
	def backtrack(index, sumR, sumG, sumB, coloring):
		if index == N:
			if sumR == sumG == sumB:
				return "".join(coloring)
			return None
		
		# Try R
		coloring.append('R')
		res = backtrack(index + 1, sumR + A[index], sumG, sumB, coloring)
		if res: return res
		coloring.pop()
		
		# Try G
		coloring.append('G')
		res = backtrack(index + 1, sumR, sumG + A[index], sumB, coloring)
		if res: return res
		coloring.pop()
		
		# Try B
		coloring.append('B')
		res = backtrack(index + 1, sumR, sumG, sumB + A[index], coloring)
		if res: return res
		coloring.pop()
		
		return None

	result = backtrack(0, 0, 0, 0, [])
	return result if result else "impossible"
