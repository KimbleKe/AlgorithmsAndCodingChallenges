# author: Kimble Ke
# date: 2025.7.28
 
# Time complexity: O((N + M) log M)

# Space complexity: O(M)
# Algorithms: binary search, sorting, for loop + while loop + pointer
def solution(A, B, C):
	# check if C[:n] first n nails can nail all planks, helper function is O(N+M)
	def is_nailed(A, B, C, n):
		nails = sorted(C[:n])  # Only consider first 'n' nails
		planks = sorted(zip(A, B), key=lambda x: x[0])  # Sort planks by start position
		ptr = 0
		for idx_a,idx_b in planks:
			while ptr < len(nails) and not (idx_a <= nails[ptr] <= idx_b):
				ptr += 1
			if ptr >= len(nails) or nails[ptr] > idx_b:
				return False
		return True

	# binary search over number of nails, binary search is O(logN)
	lower = 1
	upper = len(C)
	result = -1
	while lower <= upper:
		mid = (lower + upper) // 2
		if is_nailed(A, B, C, mid):
			result = mid
			upper = mid - 1
		else:
			lower = mid + 1
	return result

#################################################################

# Time complexity: O((N + M) log M)
# Space complexity: O(M)
# Algorithms: binary search, prefix sum
def solution2(A, B, C):
	# helper function is O(N+M)
	def is_nailed2(A, B, C, n):
		nail_used = [0] * (2 * max(B) + 1)
		# Mark all nails used up to n index
		for i in range(n):
			nail_used[C[i]] = 1
		# Create prefix sum array to check if a nail is available in a range
		for i in range(1, len(nail_used)):
			nail_used[i] += nail_used[i - 1]
		# Check each plank if there's a nail in its range
		for i in range(len(A)):
			start = A[i]
			end = B[i]
			if nail_used[end] - nail_used[start - 1] == 0:
				return False
		return True

	# binary search over number of nails, binary search is O(logN)
	lower = 1
	upper = len(C)
	result = -1
	while lower <= upper:
		mid = (lower + upper) // 2
		if is_nailed2(A, B, C, mid):
			result = mid
			upper = mid - 1
		else:
			lower = mid + 1
	return result

#################################################################

# Time complexity: O(N*M)
# Brute force, less efficient solution
def solution1(A, B, C):
	used_nails = set()

	for i in range(len(A)):
		nailed = False
		for j in range(len(C)):
			if A[i] <= C[j] <= B[i]:
				used_nails.add(j)
				nailed = True
				break  # plank i is nailed, check next plank
		if not nailed:
			return -1

	return max(used_nails) + 1  # +1 since nail index starts at 0
