# author: Kimble Ke
# date: 2025.7.22
 
# O(N) Time, Peak detection is O(N), flag placement is O(√N) × O(N) → O(N)
# O(N) Space
def solution(A):
	N = len(A)
	if N < 3:
		return 0

	# step 1: find peaks
	peaks = [0] * N
	for i in range(1, N - 1):
		if A[i - 1] < A[i] > A[i + 1]:
			peaks[i] = 1

	# step 2: precompute next peak index
	next_peak = [-1] * N
	for i in range(N - 2, -1, -1):
		if peaks[i]:
			next_peak[i] = i
		else:
			next_peak[i] = next_peak[i + 1]

	# step 3: try to place the maximum number of flags
	import math
	max_flags = 0
	max_possible = int(math.sqrt(N)) + 1
	for k in range(1, max_possible + 1):  # assume k is the number of max possible flags 
		flags_used = 0
		pos = 0
		# position cannot exceed length of array, flags_used cannot exceed max possible flags k
		while pos < N and flags_used < k:
			pos = next_peak[pos]
			if pos == -1:
				break
			flags_used += 1
			pos += k  # any 2 peak flags should have distance at least equal to k
		max_flags = max(max_flags, flags_used)

	return max_flags
