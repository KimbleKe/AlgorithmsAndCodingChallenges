# author: Kimble Ke
# date: 2025.7.24
 
# Time complexity O(N)
# Space complexity O(M+1)
def solution(M, A):
	N = len(A)
	seen = [False] * (M + 1)
	front = 0
	total = 0

	for back in range(N):
		while front < N and not seen[A[front]]:
			seen[A[front]] = True
			total += front - back + 1
			if total > 1000000000:
				return 1000000000
			front += 1
		seen[A[back]] = False
	return total
