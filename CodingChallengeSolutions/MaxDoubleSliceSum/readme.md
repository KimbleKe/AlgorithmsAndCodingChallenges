1. Problem Description
  find the maximal sum of any double slice.

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
> medium

--- 

A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

A[0] = 3 A[1] = 2 A[2] = 6 A[3] = -1 A[4] = 4 A[5] = 5 A[6] = -1 A[7] = 2
content_copy
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)
content_copy

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

A[0] = 3 A[1] = 2 A[2] = 6 A[3] = -1 A[4] = 4 A[5] = 5 A[6] = -1 A[7] = 2
content_copy
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].