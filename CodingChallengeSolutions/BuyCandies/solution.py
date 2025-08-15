# author: Kimble Ke
# date: 2025.8.15

def solution(A, B):
	pass
	
	def solution(A, B):
    n = len(A)
    half = n // 2
    
    # Unique types in each shop
    setA = set(A)
    setB = set(B)
    
    # Step 1: Buy from shop A
    fromA = min(len(setA), half)  # We can only take half coins worth
    
    # Step 2: Remaining coins for shop B
    remaining_types_needed = half - fromA
    
    # Step 3: Buy from shop B
    # We prefer types not already bought in A
    uniqueB = setB - setA
    fromB_new = min(len(uniqueB), half)
    
    # Step 4: Handle overlap — if we still have coins, we might take overlapping ones
    total_types = fromA + fromB_new
    if fromB_new < half:
        overlapB = setB & setA
        extra_from_overlap = min(half - fromB_new, len(overlapB))
        total_types = fromA + fromB_new + extra_from_overlap
    
    return min(total_types, len(setA | setB))  # Can't exceed total unique types