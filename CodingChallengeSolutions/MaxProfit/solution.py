# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(1) Space
def solution(A):
	if len(A) < 2:
		return 0
	min_price = A[0]
	max_profit = 0
	for price in A[1:]:
		min_price = min(min_price, price)
		max_profit = max(max_profit, price - min_price)
	return max_profit
