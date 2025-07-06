# Selection Sort
# time complexity: best case=O(N^2), avg case=O(N^2), worst case=O(N^2)
# space complexity = O(1)
# how it works: Select smallest from unsorted and place it at correct position.

def selectionSort(arr):
  n = len(arr)
  for i in range(n - 1):

    # Assume the current position holds
    # the minimum element
    min_idx = i
    
    # Iterate through the unsorted portion
    # to find the actual minimum
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        
        # Update min_idx if a smaller element is found
        min_idx = j
  
    # Move minimum element to its
    # correct position
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

def printArray(arr):
  for val in arr:
    print(val, end=" ")
  print()

if __name__ == "__main__":
  arr = [64, 34, 25, 12, 91, 22, 11, 5, 31, 91, 52, 18, 92, 17, 70, 97, 17, 56]
  
  print("Original array: ", end="")
  printArray(arr)
  
  selectionSort(arr)
  
  print("Sorted array: ", end="")
  printArray(arr)