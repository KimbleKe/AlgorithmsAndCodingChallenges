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

#######################################

# Time complexity O(N)
# Space complexity O(1)
def solution1(A):
	counter = 1
	maxnum = max(abs(A[0]), abs(A[-1]))
	idx1 = 0
	idx2 = len(A)-1
	while idx1 <= idx2:
		head = abs(A[idx1])
		if head == maxnum:
			idx1 += 1
			continue
		tail = abs(A[idx2])
		if tail == maxnum:
			idx2 -= 1
			continue
		if head >= tail:
			maxnum = head
			idx1 += 1
		else:
			maxnum = tail
			idx2 -= 1
		counter += 1
	return counter