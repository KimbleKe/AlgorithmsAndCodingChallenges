# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(N) Space
def solution1(A):
	n = len(A)
	if n == 3:
		return 0
	
	left_max = [0] * n
	right_max = [0] * n
	
	# compute left maximum sums ending at each position in array {A[X+1]...A[Y-1]}
	# using Kadane's algorithm 
	for i in range(1, n-1):
		left_max[i] = max(0, left_max[i-1] + A[i])

	# compute right maximum sums starting at each position in array {A[Y+1]...A[Z-1]}
	# using Kadane's algorithm in opposite direction to last iteration
	for i in range(n-2, 0, -1):
		right_max[i] = max(0, right_max[i+1] + A[i])
	
	# recall we want to find max sum of A[X+1] + A[X+2] + ... + A[Y-1] + A[Y+1] + ... + A[Z-1]
	# we need to find the maximum combination of left and right sums
	# skip y index element as it's the index to move from left to right
	# left_max[i-1] is the max sum from left side of y
	# right_max[i+1] is the max sum from right side of y
	max_sum = 0
	for y in range(1, n-1):
		max_sum = max(max_sum, left_max[y-1] + right_max[y+1]) 
	
	return max_sum