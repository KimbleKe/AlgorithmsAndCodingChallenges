# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(1) Space
def solution(A):
	candidate = None
	count = 0
	# find dominating number 
	for num in A:
		if count == 0:
			candidate = num
			count = 1
		else:
			count += 1 if num == candidate else -1
	# verify dominator and return dominator index
	if A.count(candidate) > len(A) // 2:
		return A.index(candidate)
	return -1

###############################################

# O(N) Time, O(N) Space
def solution2(A):
	if len(A) == 0:
		return -1
	if len(A) == 1:
		return 0
	B = A.copy()
	B.sort()
	c = 1
	for i in range(1,len(B)):
		if B[i] != B[i-1]:
			c = 1
		else:
			c += 1
		if c > int(len(B)/2):
			return A.index(B[i])
	return -1
