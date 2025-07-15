# author: Kimble Ke
# date: 2025.7.15

# Time Complexity: O(NlogN)
def min_abs_sum_of_two(A):
  A.sort()  # Sort the array in ascending order
  n = len(A)
  left, right = 0, n - 1
  min_abs = float('inf')
  
  while left <= right:
    current_sum = A[left] + A[right]
    current_abs = abs(current_sum)
    min_abs = min(min_abs, current_abs)
    
    # Move pointers to try to get a smaller sum
    if current_sum < 0:
      left += 1  # Need a larger sum (move left pointer right)
    else:
      right -= 1  # Need a smaller sum (move right pointer left)
  
  return min_abs

if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, 'r') as f:
    line = f.read().strip()
    A = eval(line) 

  result = min_abs_sum_of_two(A)

  print("######## input ########")
  print("input  is " + str(A))
  print("######## result ########")
  print("result is " + str(result))