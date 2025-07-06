# Tim Sort
# time complexity: best case=O(N), avg case=O(NlogN), worst case=O(NlogN)
# space complexity = O(N)
# how it works: Hybrid of merge and insertion sort (used in Python, Java).

MIN_RUN = 32

def insertionSort(arr, left, right):
  for i in range(left + 1, right + 1):
    key = arr[i]
    j = i - 1
    while j >= left and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

def merge(arr, left, mid, right):
  left_part = arr[left:mid + 1]
  right_part = arr[mid + 1:right + 1]

  i = j = 0
  k = left

  while i < len(left_part) and j < len(right_part):
    if left_part[i] <= right_part[j]:
      arr[k] = left_part[i]
      i += 1
    else:
      arr[k] = right_part[j]
      j += 1
    k += 1

  while i < len(left_part):
    arr[k] = left_part[i]
    i += 1
    k += 1

  while j < len(right_part):
    arr[k] = right_part[j]
    j += 1
    k += 1

def timSort(arr):
  n = len(arr)

  # Step 1: Sort small runs with insertion sort
  for start in range(0, n, MIN_RUN):
    end = min(start + MIN_RUN - 1, n - 1)
    insertionSort(arr, start, end)

  # Step 2: Merge sorted runs
  size = MIN_RUN
  while size < n:
    for left in range(0, n, 2 * size):
      mid = min(n - 1, left + size - 1)
      right = min((left + 2 * size - 1), n - 1)
      if mid < right:
        merge(arr, left, mid, right)
    size *= 2

# A utility function to print array of size n
def printArray(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()

# Driver code
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 91, 22, 11, 5, 31, 91, 52, 18, 92, 17, 70, 97, 17, 56]
  
  print("Original array: ", end="")
  printArray(arr)

  timSort(arr)

  print("Sorted array: ", end="")
  printArray(arr)
