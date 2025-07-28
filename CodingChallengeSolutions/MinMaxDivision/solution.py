# author: Kimble Ke
# date: 2025.7.28
 
# Time complexity - O(N log S)
# Space complexity - O(1)
def solution1(K, A):
	# Helper function to check whether the array A
	# can be divided into at most K blocks
	# such that no block has a sum greater than max_block_sum
	def is_valid(max_block_sum):
		blocks = 1            # Start with one block
		current_sum = 0       # Running sum of current block

		for num in A:
			# If adding this number exceeds the allowed max block sum
			if current_sum + num > max_block_sum:
				# We need to start a new block
				blocks += 1
				current_sum = num

				# If we've used more than K blocks, it's invalid
				if blocks > K:
					return False
			else:
				current_sum += num

		# If we finished with <= K blocks, it's valid
		return True

	# Binary search bounds:
	# - min possible max block sum is the max element (cannot split further)
	# - max possible is sum of all elements (1 block only)
	low = max(A)
	high = sum(A)
	result = high  # Start with the worst case (1 block)

	while low <= high:
		mid = (low + high) // 2  # Candidate max block sum

		# If it's possible to divide A into K blocks with max block sum `mid`
		if is_valid(mid):
			result = mid         # Try to minimize result
			high = mid - 1       # Try a smaller candidate
		else:
			low = mid + 1        # Try a larger candidate

	# Final answer is the smallest maximum block sum possible
	return result

