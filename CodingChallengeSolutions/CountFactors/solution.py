# author: Kimble Ke
# date: 2025.7.22
 
# O(√N) Time, O(1) Space
def solution1(N):
	if N == 1:
		return 1
	factors = 0
	i = 1
	while i * i < N:
		if N % i == 0:
			factors += 2  # add 2 because e.g. 1*16=16, 2*8=16, there're 2 factors
		i += 1
	if i * i == N:
		factors += 1  # add 1 because e.g. 4*4=16, but 4 cannot be counted twice
	return factors