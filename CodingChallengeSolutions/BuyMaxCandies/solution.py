# author: Kimble Ke
# date: 2025.8.15

def solution(A, B):
	n = len(A)
	mid = n // 2
	shopA_unique_candy_type = set(A)
	shopB_unique_candy_type = set(B)

	candy_bought_from_A = min(len(shopA_unique_candy_type), mid)
	uniqueB = shopB_unique_candy_type - shopA_unique_candy_type
	candy_bought_from_B = min(len(uniqueB), mid)
	total_types = candy_bought_from_A + candy_bought_from_B

	if candy_bought_from_B < mid:
		overlap = shopB_unique_candy_type & shopA_unique_candy_type
		extra_from_overlap = min(mid - candy_bought_from_B, len(overlap))
		total_types = candy_bought_from_A + candy_bought_from_B + extra_from_overlap

	return min(total_types, len(shopA_unique_candy_type | shopB_unique_candy_type))
