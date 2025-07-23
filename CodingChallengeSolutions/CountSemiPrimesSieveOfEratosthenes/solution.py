# author: Kimble Ke
# date: 2025.7.23
 
# Time complexity O(N log log N + M)
# Space complexity O(N)
def solution1(N, P, Q):
	# Step 1: Sieve Of Eratosthenes algorithm used to find prime numbers up to N
	is_prime = [True] * (N + 1)
	is_prime[0] = is_prime[1] = False
	for i in range(2, int(N**0.5) + 1):
		if is_prime[i]:
			for j in range(i * i, N + 1, i):
				is_prime[j] = False

	# Step 2: Generate all semiprimes up to N
	semiprime = [0] * (N + 1)
	for i in range(2, N + 1):
		if is_prime[i]:
			for j in range(i, N // i + 1):
				if is_prime[j]:
					if i * j <= N:
						semiprime[i * j] = 1

	# Step 3: Compute prefix sum of semiprimes
	prefix = [0] * (N + 1)
	for i in range(1, N + 1):
		prefix[i] = prefix[i - 1] + semiprime[i]

	# Step 4: Answer each query using prefix sums
	result = []
	for i in range(len(P)):
		result.append(prefix[Q[i]] - prefix[P[i] - 1])

	return result


