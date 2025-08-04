# author: Kimble Ke
# date: 2025.8.4
 
# O(N) Time, O(1) Space
def solution(K, A):
	count = 0
	length = 0
	for rope in A:
		length += rope
		if length >= K:
			count += 1
			length = 0  # reset for next rope
	return count
