# author: Kimble Ke
# date: 2025.7.15
 
# Time complexity: O(log N)
# Space complexity: O(log N)
def solution1(N):
	binary = bin(N)[2:]  # Get binary string without '0b' prefix
	max_gap = current_gap = 0
	found_one = False

	for bit in binary:
		if bit == '1':
			if found_one:
				max_gap = max(max_gap, current_gap)
			found_one = True
			current_gap = 0
		else:
			if found_one:
				current_gap += 1

	return max_gap