# Insertion Sort
# time complexity: best case=O(N), avg case=O(N^2), worst case=O(N^2)
# space complexity = O(1)
# how it works: Insert elements into sorted portion by shifting larger elements.

def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

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

  insertionSort(arr)

  print("Sorted array: ", end="")
  printArray(arr)