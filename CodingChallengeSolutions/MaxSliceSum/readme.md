1. Problem Description, MaxSliceSum, a.k.a. MaxSubArray
  find a maximum sum of a compact subsequence of array elements.

Given an array of integers, find the maximum sum of any contiguous subarray (also known as a "slice"). The slice can be of any length, including the entire array. The sum of an empty slice is defined as 0, but since the array contains only integers, the maximum slice sum cannot be less than the maximum single element in the array (if all numbers are negative).

2. Example Input/Output (Including Edge Cases)
Example 1:
Input: [3, 2, -6, 4, 0]
Output: 5
Explanation: The maximum sum is achieved by the subarray [3, 2] or [4, 0] or [3, 2, -6, 4, 0] (sum = 5).

Example 2:
Input: [-10]
Output: -10
Explanation: The only possible slice is [-10].

Example 3 (All Negative Numbers):
Input: [-2, -3, -1, -5]
Output: -1
Explanation: The maximum sum is the single element -1.

Example 4 (All Positive Numbers):
Input: [1, 2, 3, 4]
Output: 10
Explanation: The maximum sum is the entire array.


<br><br><br>

> **Difficulty level**
> easy

--- 

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)


that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3 A[1] = 2 A[2] = -6 A[3] = 4 A[4] = 0

the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].