# author: Kimble Ke
# date: 2025.7.20
 
# O(1) Time, O(1) Space
def solution(A, B, K):
  if K == 0:
    return 0  # Handle invalid case (though K ≥ 1 per constraints)
  
  # Calculate prefix sums up to B and A
  prefix_B = B // K  # The count of numbers ≤ B divisible by K is B // K
  prefix_A = A // K  # The count of numbers ≤ A divisible by K is A // K
  result = prefix_B - prefix_A

  if A % K == 0:  # Check if A itself is divisible
    result+=1  # Include A in the count

  return result
