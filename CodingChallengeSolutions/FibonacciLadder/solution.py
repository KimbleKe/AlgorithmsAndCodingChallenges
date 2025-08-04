# author: Kimble Ke
# date: 2025.7.24
 
# Time complexity O(L + N) (Where N = max(A) + 2, for precomputing Fibonacci sequence)
# Space complexity O(N)
def solution(A, B):
	# Get the maximum number of rungs needed
	L = len(A)
	N = max(A)

	# Precompute Fibonacci numbers up to N + 2 (to be safe)
	fib = [0] * (N + 2)
	fib[0] = 1
	fib[1] = 1
	for i in range(2, N + 2):
		fib[i] = (fib[i - 1] + fib[i - 2]) & ((1 << 30) - 1)  # avoid overflow

	# Compute results using modulo 2^B[i]
	result = [0] * L
	for i in range(L):
		mod = 1 << B[i]
		result[i] = fib[A[i]] % mod

	return result
