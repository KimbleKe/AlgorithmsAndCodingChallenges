def solution(A):
	mod = 1_000_000_000
	N = len(A)
	if N == 0:
		return 0

	income = 0
	i = 0
	state = "sell"

	while i < N:
		if state == "sell":
			# find local max to sell
			while i + 1 < N and A[i] <= A[i + 1]:
				i += 1
			income += A[i]
			state = "buy"
		else:
			# find local min to buy
			while i + 1 < N and A[i] >= A[i + 1]:
				i += 1
			income -= A[i]
			state = "sell"
		income %= mod
		i += 1

	# if we end with a buy (incomplete cycle), undo the last buy
	if state == "buy":
		income += A[N - 1]
		income %= mod

	return income
