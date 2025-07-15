# author: Kimble Ke
# date: 2025.7.15

# Time Complexity: O(N). Worst case: N+1 is missing
def missing_integer(A):
  seen = set(A)    # store all positive numbers in a set for O(1) lookup
  for i in range(1, len(A)+2): 
    if i not in seen:
      return i
    
