# author: Kimble Ke
# date: 2025.8.4
 
# O(N) Time, O(N) Space
def solution(A):
	dp = [0] * len(A)
	dp[0] = A[0]
	for i in range(1, len(A)):
		dp[i] = A[i] + max(dp[max(0, i - 6):i])
	return dp[-1]

# Algorithm Used
# Dynamic Programming (DP)
# Track the maximum score to reach each position using a recurrence relation:
#   dp[i] = A[i] + max(dp[i-1], dp[i-2], ..., dp[i-6])