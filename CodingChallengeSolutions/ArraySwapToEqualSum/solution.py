# author: Kimble Ke
# date: 2025.7.25
 
# Time complexity - O(N + M)
# Space complexity - O(M) — due to set for fast lookup
def solution1(A, B):
	sumA = sum(A)
	sumB = sum(B)
	delta = sumB - sumA

	# If the difference is odd, it's impossible to balance with integer swaps
	if delta % 2 != 0:
		return False

	target = delta // 2
	setB = set(B)

	for a in A:
		if a + target in setB:
			return True

	return False
