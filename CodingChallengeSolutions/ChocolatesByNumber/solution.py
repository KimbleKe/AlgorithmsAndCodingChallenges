# author: Kimble Ke
# date: 2025.7.23
 
# Time complexity O(log N)
# Space complexity O(1)
def solution(N, M):
	# helper function to compute Greatest Common Divisor GCD using Euclidean Algorithm
	def gcd(n, m):
		if n % m == 0:
			return m
		else:
			return gcd(m, n % m)

	# compute Least Common Multiple (LCM), LCM = N*M/GCD
	# number of chocolates eaten is equal to LCM / M, which is equivalent to N divided by gcd of N and M
	return N // gcd(N, M)
