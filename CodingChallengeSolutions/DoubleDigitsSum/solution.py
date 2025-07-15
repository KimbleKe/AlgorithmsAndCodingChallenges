# author: Kimble Ke
# date: 2025.7.15

# O(N) solution
def solution(n):
  total = 0
  for digit in str(n):
    total += 2 * int(digit)
  return total