# Insertion Sort
# time complexity: best case=O(N+K), avg case=O(N+K), worst case=O(N+K)
# space complexity = O(K)
# how it works: Count occurrences and reconstruct sorted array (for integers).

def countingSort(input_array):
  # Finding the maximum element of input_array.
  M = max(input_array)

  # Initializing count_array with 0
  count_array = [0] * (M + 1)

  # Mapping each element of input_array as an index of count_array
  for num in input_array:
    count_array[num] += 1

  # Calculating prefix sum at every index of count_array
  for i in range(1, M + 1):
    count_array[i] += count_array[i - 1]

  # Creating output_array from count_array
  output_array = [0] * len(input_array)

  for i in range(len(input_array) - 1, -1, -1):
    output_array[count_array[input_array[i]] - 1] = input_array[i]
    count_array[input_array[i]] -= 1

  return output_array

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

  arr=countingSort(arr)

  print("Sorted array: ", end="")
  printArray(arr)