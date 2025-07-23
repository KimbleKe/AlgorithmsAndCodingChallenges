1. Problem Description
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
> medium to hard