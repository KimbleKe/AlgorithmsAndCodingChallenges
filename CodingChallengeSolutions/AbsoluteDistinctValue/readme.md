1. Problem Description
  compute number of distinct absolute values of sorted array elements.

You are given an array A of N integers. Your task is to compute the number of distinct absolute values in the array.
For example:
A = [-5, -3, -1, 0, 3, 6] → Absolute values are [5, 3, 1, 0, 3, 6] → Distinct ones: [0, 1, 3, 5, 6] → Return 5.

2. Example Input/Output
Input: [-5, -3, -1, 0, 3, 6]
Output: 5 (Absolute values: 0, 1, 3, 5, 6)

Edge Case (All Duplicates):
Input: [2, 2, 2, 2]
Output: 1

Edge Case (Empty Array):
Input: []
Output: 0

Edge Case (Mixed Signs):
Input: [-2, -1, 0, 1, 1, 2]
Output: 3


<br><br><br>

> **Difficulty level**
> easy

---

A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

A[0] = -5 A[1] = -3 A[2] = -1 A[3] = 0 A[4] = 3 A[5] = 6
content_copy
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)
content_copy

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

A[0] = -5 A[1] = -3 A[2] = -1 A[3] = 0 A[4] = 3 A[5] = 6
content_copy
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.