1. Problem: 

1. Problem Description:
Count the number of triangular triplets in a given array of integers.
A triangular triplet consists of three elements (P, Q, R) such that:

0 ≤ P < Q < R < N

A[P] + A[Q] > A[R]

A[Q] + A[R] > A[P]

A[R] + A[P] > A[Q]

In practice, when the array is sorted in non-decreasing order, it’s sufficient to check only:

A[P] + A[Q] > A[R], because A[R] ≥ A[Q] ≥ A[P]


2. Example Input/Output:
Example 1:

Input: [10, 2, 5, 1, 8, 12]
Output: 4
Explanation: There are 4 triangular triplets.

Edge Case 1:
Input: [1, 1, 1]
Output: 1

Edge Case 2:
Input: [1, 2, 3]
Output: 0


<br><br><br>

> **Difficulty level**
> easy

---

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

A[0] = 10 A[1] = 2 A[2] = 5 A[3] = 1 A[4] = 8 A[5] = 12

There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)


that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:

A[0] = 10 A[1] = 2 A[2] = 5 A[3] = 1 A[4] = 8 A[5] = 12

the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000];
each element of array A is an integer within the range [1..1,000,000,000].