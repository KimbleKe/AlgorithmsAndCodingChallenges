# author: Kimble Ke
# date: 2025.7.15

# Time Complexity: O(N)
def missing_integer(A):
  seen = set(A)
  for i in range(1, len(A)+2):  # Worst case: N+1 is missing
    if i not in seen:
      return i
    
