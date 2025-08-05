1. Problem Description: CountDistinctSlices
  count the number of distinct slices (containing only unique numbers).

You are given integers M and a zero-indexed array A of N integers. Every element of A is an integer within the range [0..M].

A slice is a contiguous subsequence of A defined by a pair of integers (P, Q) such that 0 ≤ P ≤ Q < N.

A slice (P, Q) is called distinct if all elements in the sequence A[P], A[P+1], ..., A[Q] are distinct.

Your task is to count the number of distinct slices. If the number of distinct slices is greater than 1,000,000,000, return 1,000,000,000.

2. Example Input/Output:
Example 1:

M = 6  
A = [3, 4, 5, 5, 2]

Output: 9
Explanation:
The valid distinct slices are:
  (0,0), (0,1), (0,2)
  (1,1), (1,2)
  (2,2)
  (3,3)
  (4,4), (3,4)

Edge Cases:

If A = [] → output = 0

If all elements are the same → each (i, i) slice is distinct

If all elements are unique → number of slices = N * (N + 1) // 2


<br><br><br>

> **Difficulty level**
> easy

---

An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

A[0] = 3 A[1] = 4 A[2] = 5 A[3] = 5 A[4] = 2

There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

class Solution { public int solution(int M, int[] A); }


that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

A[0] = 3 A[1] = 4 A[2] = 5 A[3] = 5 A[4] = 2

the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].