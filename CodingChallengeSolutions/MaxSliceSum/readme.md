1. Problem Description
MaxSliceSum
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

> **Difficulty level**
> medium