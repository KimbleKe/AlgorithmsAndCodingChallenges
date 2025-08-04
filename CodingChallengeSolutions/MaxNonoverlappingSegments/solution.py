# author: Kimble Ke
# date: 2025.8.4
 
# O(N) Time, O(1) Space
def solution(A, B):
	if not A:
		return 0

	count = 1
	last_end = B[0]

	for i in range(1, len(A)):
		if A[i] > last_end:
			count += 1
			last_end = B[i]

	return count
