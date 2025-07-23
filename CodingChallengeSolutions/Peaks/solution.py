# author: Kimble Ke
# date: 2025.7.23
 
# O(N * √N) Time incl. peak detection is O(N)
# O(N) Space
def solution1(A):
	n = len(A)
	peaks = [0] * n

	# step 1: find peaks
	for i in range(1, n - 1):
		if A[i - 1] < A[i] > A[i + 1]:
			peaks[i] = 1

	# step 2: compute prefix
	prefix = [0] * (n + 1)
	for i in range(n):
		prefix[i + 1] = prefix[i] + peaks[i]

	# step 3: find max blocks where each block contains at least one peak
	for block_size in range(1, n + 1):
		if n % block_size != 0:
			continue   # block_size cannot divide the array evenly, so move on to try different block size
		block = n // block_size
		each_block_contain_peak = True
		for i in range(block):
			if prefix[(i + 1) * block_size] - prefix[i * block_size] == 0:  # break if next block has no new peak
				each_block_contain_peak = False
				break
		if each_block_contain_peak:  # checked every block has its own peak(s) 
			return block
	return 0
