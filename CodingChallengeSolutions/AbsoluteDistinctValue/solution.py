# author: Kimble Ke
# date: 2025.7.24
 
# Time complexity O(N)
# Space complexity O(N)
def solution(A):
	# Use a set to store unique absolute values
	abs_set = set()
	for num in A:
		abs_set.add(abs(num)) 
	return len(abs_set)