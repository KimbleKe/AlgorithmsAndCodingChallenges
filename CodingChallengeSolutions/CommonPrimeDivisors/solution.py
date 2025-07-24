# author: Kimble Ke
# date: 2025.7.23
 
# Time complexity O(N * log(max(A[i], B[i]))²)
# Space complexity O(1) (excluding input/output arrays)
def solution1(A, B):
	# Euclidean algorithm for GCD
	def gcd(a, b):
		while b:
			a, b = b, a % b
		return a
	
	# helper function checks whether any extra prime factors exist in a or b that are not in common_gcd
	def remove_common_prime_divisors(x, common_gcd):
		while True:
			gcd_val = gcd(x, common_gcd)
			if gcd_val == 1:
				break
			x //= gcd_val
		return x

	count = 0
	for a, b in zip(A, B):
		# mathematically, common GCD is the product of all a and b's common prime divisors
		common_gcd = gcd(a, b)

		# remove all prime divisors from a that are in common_gcd
		# if function returns number other than 1, it means there are other prime divisor that a contains and b does not contain
		if remove_common_prime_divisors(a, common_gcd) != 1:
			continue

		# remove all prime divisors from b that are in common_gcd
		# if function returns number other than 1, it means there are other prime divisor that b contains and a does not contain
		if remove_common_prime_divisors(b, common_gcd) != 1:
			continue

		# both a and b share the same common prime divisors, count++; if not, continue command will skip count increment
		count += 1

	# return number of pair(s) that share the exact same common prime divisors
	return count

