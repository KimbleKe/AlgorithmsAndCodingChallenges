# author: Kimble Ke
# date: 2025.7.6

# O(N) solution
def solution(A):
  from collections import defaultdict

  # Step 1: Count occurrences
  count = defaultdict(int)
  for num in A:
    count[num] += 1

  # Step 2: Find the first unique number
  for num in A:
    if count[num] == 1:
      return num

  return -1  # No unique number found
