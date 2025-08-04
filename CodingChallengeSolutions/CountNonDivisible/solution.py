# author: Kimble Ke
# date: 2025.7.23
 
# Time complexity O(N log N)
# Space complexity O(N + max(A))
def solution(A):
	n = len(A)

	# compute prefix array "count" which count frequency of each number in A
	max_val = max(A)
	count = [0] * (max_val + 1)
	for num in A:
		count[num] += 1

	# compute number of divisible and non-divisible
	result = []
	for num in A:
		total = 0
		i = 1
		while i * i <= num:
			if num % i == 0:  # check if i is divisible
				total += count[i]  # add frequency of number i in count to total
				if i != num // i: 
					total += count[num // i]  # use count array to reduce computation, e.g. 3 // 1 = 3, count[3] gives freq of 3 in array A
			i += 1
		result.append(n - total)  # non-divisible = total number of elem in A - total number of divisible
	
	# return number of non-divisible for each elem in A 
	return result
