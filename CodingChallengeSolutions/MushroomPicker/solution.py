# author: Kimble Ke
# date: 2025.7.25
 
# Time complexity: O(N)
# Space complexity: O(N)
def solution1(A, K, M):
	N = len(A)
	# Prefix sums to allow O(1) range sum queries
	prefix_sum = [0] * (N + 1)
	for i in range(1, N + 1):
		prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

	def get_range_sum(p, q):
		# Sum from index p to q inclusive
		return prefix_sum[q + 1] - prefix_sum[p]

	result = 0

	# Try going left first, then right
	for p in range(min(M, K) + 1):
		left = K - p
		right = min(N - 1, (K - p) + (M - p))
		result = max(result, get_range_sum(left, right))

	# Try going right first, then left
	for p in range(min(M, N - 1 - K) + 1):
		right = K + p
		left = max(0, (K + p) - (M - p))
		result = max(result, get_range_sum(left, right))

	return result
