# Heap Sort
# time complexity: best case=O(NlogN), avg case=O(NlogN), worst case=O(NlogN)
# space complexity = O(1)
# how it works: Build max-heap, extract max repeatedly and rebuild heap.

# To heapify a subtree rooted with node i
# which is an index in arr[].
def heapify(arr, n, i):
    
  # Initialize largest as root
  largest = i 
  
  #  left index = 2*i + 1
  l = 2 * i + 1 
  
  # right index = 2*i + 2
  r = 2 * i + 2  

  # If left child is larger than root
  if l < n and arr[l] > arr[largest]:
    largest = l

  # If right child is larger than largest so far
  if r < n and arr[r] > arr[largest]:
    largest = r

  # If largest is not root
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]  # Swap

    # Recursively heapify the affected sub-tree
    heapify(arr, n, largest)

# Main function to do heap sort
def heapSort(arr):
  
  n = len(arr) 

  # Build heap (rearrange array)
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  # One by one extract an element from heap
  for i in range(n - 1, 0, -1):
    
    # Move root to end
    arr[0], arr[i] = arr[i], arr[0] 

    # Call max heapify on the reduced heap
    heapify(arr, i, 0)

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

  heapSort(arr)

  print("Sorted array: ", end="")
  printArray(arr)
