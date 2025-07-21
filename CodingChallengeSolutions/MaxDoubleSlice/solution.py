# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(N) Space
def solution1(A):
	n = len(A)
	if n == 3:
		return 0
	
	left_max = [0] * n
	right_max = [0] * n
	
	# compute left maximum sums ending at each position
	for i in range(1, n-1):
		left_max[i] = max(0, left_max[i-1] + A[i])

	# compute right maximum sums starting at each position
	for i in range(n-2, 0, -1):
		right_max[i] = max(0, right_max[i+1] + A[i])
	
	# find the maximum combination of left and right sums
	max_sum = 0
	for i in range(1, n-1):
		max_sum = max(max_sum, left_max[i-1] + right_max[i+1])
	
	return max_sum