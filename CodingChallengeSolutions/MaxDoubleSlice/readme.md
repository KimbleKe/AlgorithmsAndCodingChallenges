1. Problem Description
A non-empty array A consisting of N integers is given. A double slice is any triplet (X, Y, Z) such that 0 ≤ X < Y < Z < N. The sum of the double slice is the total of A[X+1] + A[X+2] + ... + A[Y-1] + A[Y+1] + ... + A[Z-1]. Find the maximum sum of any double slice.

2. Example Input/Output
Input: [3, 2, 6, -1, 4, 5, -1, 2]
Output: 17 (from double slice (0, 3, 6))

Edge Case 1 (Minimum Length):
Input: [5, 17, 0, 3]
Output: 17 (from (0, 1, 3))

Edge Case 2 (All Negative):
Input: [-5, -2, -3, -1]
Output: 0 (best to exclude all elements)

Edge Case 3 (Three Elements):
Input: [1, 2, 3]
Output: 0 (no elements between X and Z)


<br><br><br>

> **Difficulty level**
> medium to hard