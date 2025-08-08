def solution(A):
	mod = 1000000000
	N = len(A)
	if N == 0:
		return 0

	income = 0
	i = 0
	state = "sell"  # start by selling

	while i < N:
		if state == "sell":
			# Find local max
			while i + 1 < N and A[i] < A[i + 1]:
					i += 1
			income += A[i]
			income %= mod
			state = "buy"
		else:
			# Find local min
			while i + 1 < N and A[i] > A[i + 1]:
					i += 1
			income -= A[i]
			income %= mod
			state = "sell"
		i += 1

	return income % mod
