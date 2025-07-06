# Shell Sort
# time complexity: best case=O(NlogN), avg case=O(N^1.5), worst case=O(N^2)
# space complexity = O(1)
# how it works: Insertion sort with decreasing gap sizes to pre-sort elements.

def shellSort(arr):
  n = len(arr)
  gap = n // 2  # Start with a large gap and reduce it

  while gap > 0:
    # Perform a gapped insertion sort for this gap size
    for i in range(gap, n):
      temp = arr[i]
      j = i

      # Shift earlier gap-sorted elements up until the correct location is found
      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap

      arr[j] = temp

    gap //= 2  # Reduce the gap for next pass


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

  shellSort(arr)

  print("Sorted array: ", end="")
  printArray(arr)
