# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(1) Space
def solution(A):
	if not A:
		return 0
	max_current = max_global = A[0]
	for num in A[1:]:
		max_current = max(num, max_current + num)
		if max_current > max_global:
			max_global = max_current
	return max_global
