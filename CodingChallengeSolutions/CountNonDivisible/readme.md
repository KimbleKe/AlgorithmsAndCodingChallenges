1. Problem Description
  calculate the number of elements of an array that are not divisors of each element.

Given an array A of N integers, for each element A[i] count the number of elements in the array that are not divisors of A[i].

2. Example Input/Output
Input: [3, 1, 2, 3, 6]
Output: [2, 4, 3, 2, 0]
Explanation:

For 3: 1 and 2 are not divisors → 2

For 1: all other numbers are not divisors → 4

For 2: 3, 3, 6 are not divisors → 3

For 6: no numbers are not divisors → 0

Edge Case (All Same):
Input: [2, 2, 2]
Output: [0, 0, 0]

Edge Case (Prime Numbers):
Input: [7, 11, 13]
Output: [2, 2, 2]


<br><br><br>

> **Difficulty level**
> medium

---

You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

A[0] = 3 A[1] = 1 A[2] = 2 A[3] = 3 A[4] = 6
content_copy
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)
content_copy

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

A[0] = 3 A[1] = 1 A[2] = 2 A[3] = 3 A[4] = 6
content_copy
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N
content_copy
].