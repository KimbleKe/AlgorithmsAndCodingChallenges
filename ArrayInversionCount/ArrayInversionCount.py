# author: Kimble Ke
# date: 2025.7.6
 
# O(NlogN) solution
def solution(A):
  def merge_sort(arr):
    if len(arr) <= 1:
      return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)

    total_inv = inv_left + inv_right + inv_merge
    return merged, total_inv

  def merge(left, right):
    merged = []
    i = j = inv_count = 0
    L = len(left)

    while i < L and j < len(right):
      if left[i] <= right[j]:
        merged.append(left[i])
        i += 1
      else:
        merged.append(right[j])
        inv_count += L - i  # All remaining in left are greater
        j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count

  _, total_inversions = merge_sort(A)
  return total_inversions if total_inversions <= 1_000_000_000 else -1
