# author: Kimble Ke
# date: 2025.7.22
 
# O(√N) Time, O(1) Space
def solution1(N):
	min_perimeter = float('inf')
	i = 1
	while i * i <= N:
		if N % i == 0:
			side = N // i
			perimeter = 2 * (i + side)
			if perimeter < min_perimeter:
				min_perimeter = perimeter
		i += 1
	return min_perimeter