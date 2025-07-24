1. Problem Description
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