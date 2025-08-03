# author: Kimble Ke
# date: 2025.7.15

# Time complexity: O(N)
# Space complexity: O(N)
def solution(n):
  result = []
  string = str(n)
  for digit in string:
    new_digit = (int(digit) + 1) % 10
    result.append(str(new_digit))
  return int(''.join(result))  # Removes leading zero if needed
