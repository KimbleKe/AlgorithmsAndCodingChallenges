# author: Kimble Ke
# date: 2025.7.23
 
# Time complexity - O(N * log M)
# Space complexity - O(N + M)
def solution(A):
	freq = {}
	for val in A:
		if val in freq:
			freq[val] += 1
		else:
			freq[val] = 1

	max_val = max(A)
	result = []

	# Precompute non-divisors count
	divisor_count = [0] * (max_val + 1)

	# For each number up to max(A), find which values divide it
	for i in range(1, max_val + 1):
		j = i
		while j <= max_val:
			if j in freq:
				divisor_count[j] += freq.get(i, 0)
			j += i

	for val in A:
		result.append(len(A) - divisor_count[val])

	return result
