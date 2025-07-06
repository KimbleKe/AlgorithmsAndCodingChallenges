# Bubble Sort
# time complexity: best case=O(N^2), avg case=O(N^2), worst case=O(N^2)
# space complexity = O(1)
# how it works: Repeatedly swap adjacent elements if out of order (bubble up max).

def bubbleSort(arr):
  n = len(arr)
  
  # Traverse through all array elements
  for i in range(n):
    swapped = False

    # Last i elements are already in place
    for j in range(0, n-i-1):

      # Traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if (swapped == False):
        break

# A utility function to print array of size n
def printArray(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()

# Driver code to test above
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 91, 22, 11, 5, 31, 91, 52, 18, 92, 17, 70, 97, 17, 56]

  print("Original array: ", end="")
  printArray(arr)

  bubbleSort(arr)

  print("Sorted array: ", end="")
  printArray(arr)