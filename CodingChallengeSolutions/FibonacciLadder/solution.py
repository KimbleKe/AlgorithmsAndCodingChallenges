# author: Kimble Ke
# date: 2025.7.24
 
# Time complexity O(L + N) (Where N = max(A) + 2, for precomputing Fibonacci sequence)
# Space complexity O(N)
def solution(A, B):
	L = len(A)

	# ladder has no rung, no way to climb
	if L == 0:
		return []

	# find max rung and max modulo exponent
	max_rung = max(A)
	max_mod_exponent = max(B)

	# Final Step Options:
	#     If your last step is 1 rung, there are fib(n-1) ways to reach the (n-1)-th rung.
	#     If your last step is 2 rungs, there are fib(n-2) ways to reach the (n-2)-th rung.
	# Base Cases:
	#     fib(0) = 0 (no ladder, no way to climb)
	#     fib(1) = 1 (only one way: [1])
	#     fib(2) = 2 (two ways: [1+1] or [2]) 
	# Thus, the recurrence is:
	#     fib(n) = fib(n-1) + fib(n-2)
	#     which is the Fibonacci sequence shifted by 1 position
	# number of rungs [0,1,2,3,4,5,6...] have corresponding fib ways of [0,1,2,3,5,8,13...] to climb the ladder

	# precompute Fibonacci numbers up to max_rung using modulo 2^max_mod_exponent
	# << is bitwise operator, 3 has binary 00000011, shift bits left by 2 gives 00001100, e.g. 3<<2=3x(2^2)=12
	# If it's 1<<max_mod_exponent, it's 2 to the power of max_mod_exponent
	mod = 1 << max_mod_exponent  # Global mod to prevent integer overflow. 
	fib = [0] * (max_rung + 2)
	fib[1] = 1
	fib[2] = 2
	for i in range(3, max_rung + 1):
		# Paths ending with 1: fib(n-1) ways; Paths ending with 2: fib(n-2) ways; Total: fib(n) = fib(n-1) + fib(n-2)
		fib[i] = (fib[i - 1] + fib[i - 2]) % mod  

	# answer each query with modulus 2^B[i]
	result = []
	for i in range(L):
		mod_val = 1 << B[i] # 2 to the power of B[i]
		result.append(fib[A[i]] % mod_val)

	return result



