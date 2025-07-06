# Merge Sort
# time complexity: best case=O(NlogN), avg case=O(NlogN), worst case=O(NlogN)
# space complexity = O(N)
# how it works: Divide array, recursively sort, and merge sorted halves.

def merge(arr, left, mid, right):
  n1 = mid - left + 1
  n2 = right - mid

  # Create temp arrays
  L = [0] * n1
  R = [0] * n2

  # Copy data to temp arrays L[] and R[]
  for i in range(n1):
    L[i] = arr[left + i]
  for j in range(n2):
    R[j] = arr[mid + 1 + j]

  i = 0  # Initial index of first subarray
  j = 0  # Initial index of second subarray
  k = left  # Initial index of merged subarray

  # Merge the temp arrays back
  # into arr[left..right]
  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  # Copy the remaining elements of L[],
  # if there are any
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  # Copy the remaining elements of R[], 
  # if there are any
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

def mergeSort(arr, left, right):
  if left < right:
    mid = (left + right) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)

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

  mergeSort(arr, 0, len(arr) - 1)

  print("Sorted array: ", end="")
  printArray(arr)
