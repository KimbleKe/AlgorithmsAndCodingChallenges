# author: Kimble Ke
# date: 2025.7.28
 
# Time complexity - O((N + M) log M)

# Space complexity - O(M)
def solution1(A, B, C):
	# Helper function to check if 'n' nails can cover all planks
	def can_nail_all(n):
		sorted_nails = sorted(C[:n])  # Only consider first 'n' nails
		sorted_planks = sorted(zip(A, B), key=lambda x: x[0])  # Sort planks by start position
		nail_ptr = 0
		
		for start, end in sorted_planks:
			# Find first nail >= plank start
			while nail_ptr < len(sorted_nails) and sorted_nails[nail_ptr] < start:
				nail_ptr += 1
			# Fail if no nail in [start,end]
			if nail_ptr >= len(sorted_nails) or sorted_nails[nail_ptr] > end:
				return False
		return True

	# Binary search setup
	left = 1  # minimum 1 nail needed
	right = len(C)  # maximum all nails
	result = -1  # default: impossible
	
	# Binary search for minimal nail count
	while left <= right:
		mid = (left + right) // 2
		if can_nail_all(mid): # Check if mid nails suffice
			result = mid
			right = mid - 1  # Try fewer nails
		else:
			left = mid + 1  # Need more nails
	return result
