# author: Kimble Ke
# date: 2025.7.20
 
# O(N) Time, O(1) Space
def solution(A):
  east_count = 0
  passing_pairs = 0
  
  for car in A:
    if car == 0:
      east_count += 1
    else:
      passing_pairs += east_count
      if passing_pairs > 1_000_000_000:
        return -1
  return passing_pairs

# O(N) Time, O(N) Space
def solution1(A):
  n = len(A)
  prefix = [0]*(n+1)
  count = 0

  # compute prefix sums (count of west passing cars)
  for i in range(1, n+1):
    prefix[i] = prefix[i-1] + A[i-1]

  # compute passing pairs, for each east passing car, add the number of west passing cars after it
  for i in range(n):
    if A[i] == 0: # east passing car
      count += prefix[-1] - prefix[i+1]
      if count > 1_000_000_000:
        return -1
      
  return count

