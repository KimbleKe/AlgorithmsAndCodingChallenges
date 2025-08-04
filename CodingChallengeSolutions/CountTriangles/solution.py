# author: Kimble Ke
# date: 2025.7.21
 
# O(N²) Time, O(1) Space
# count the number of triangles that can be built from a given set of edges
def solution(A):
	A.sort()
	n = len(A)
	count = 0

	for i in range(n - 1, 1, -1):
		left = 0
		right = i - 1
		while left < right:
			if A[left] + A[right] > A[i]:
				# All elements from left to right-1 will satisfy the condition with A[right] and A[i]
				count += right - left
				right -= 1
			else:
				left += 1

	return count
