# author: Kimble Ke
# date: 2025.8.4
 
# O(N * S) Time, O(S) Space
def solution(A):
	if not A:
		return 0

	A = [abs(x) for x in A]
	total = sum(A)
	max_val = max(A)

	count = [0] * (max_val + 1)
	for num in A:
		count[num] += 1

	dp = [-1] * (total + 1)
	dp[0] = 0

	for val in range(1, max_val + 1):
		if count[val] == 0:
			continue
		for i in range(total + 1):
			if dp[i] >= 0:
				dp[i] = count[val]
			elif i >= val and dp[i - val] > 0:
				dp[i] = dp[i - val] - 1

	result = total
	for i in range(total // 2 + 1):
		if dp[i] >= 0:
			result = min(result, total - 2 * i)
	return result
