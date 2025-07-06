# Quick Sort
# time complexity: best case=O(NlogN), avg case=O(NlogN), worst case=O(N^2)
# space complexity = O(log(N))
# how it works: Choose pivot, partition array, and recursively sort partitions.

# Partition function
def partition(arr, low, high):
  
  # Choose the pivot
  pivot = arr[high]
  
  # Index of smaller element and indicates 
  # the right position of pivot found so far
  i = low - 1
  
  # Traverse arr[low..high] and move all smaller
  # elements to the left side. Elements from low to 
  # i are smaller after every iteration
  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      swap(arr, i, j)
  
  # Move pivot after smaller elements and
  # return its position
  swap(arr, i + 1, high)
  return i + 1

# Swap function
def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

# The QuickSort function implementation
def quickSort(arr, low, high):
  if low < high:
      
    # pi is the partition return index of pivot
    pi = partition(arr, low, high)
    
    # Recursion calls for smaller elements
    # and greater or equals elements
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)

# A utility function to print array of size n
def printArray(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()

# Driver method
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 91, 22, 11, 5, 31, 91, 52, 18, 92, 17, 70, 97, 17, 56]
  
  print("Original array: ", end="")
  printArray(arr)

  quickSort(arr, 0, len(arr) - 1)

  print("Sorted array: ", end="")
  printArray(arr)

