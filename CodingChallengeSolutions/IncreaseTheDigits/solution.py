# author: Kimble Ke
# date: 2025.7.15

# O(N) solution
def solution1(n):
  result = []
  for digit in str(n):
    new_digit = (int(digit) + 1) % 10
    result.append(str(new_digit))
  return int(''.join(result))  # Removes leading zero if needed