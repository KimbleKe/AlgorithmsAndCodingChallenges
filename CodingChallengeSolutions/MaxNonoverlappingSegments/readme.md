Problem: 
  find a maximal set of non-overlapping segments.

You are given two arrays A and B, both of length N, representing N segments. Segment K starts at A[K] and ends at B[K]. Segments are sorted by their end points (B[K] <= B[K+1]).

Your goal is to select the maximum number of non-overlapping segments. Two segments [A[K], B[K]] and [A[L], B[L]] are non-overlapping if B[K] < A[L] or B[L] < A[K].

Return the maximum number of non-overlapping segments that can be chosen.

2. Example Input/Output including Edge Cases

Example 1:
Input:
A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]

Output:
3

Explanation:
Pick segments (1,5), (7,8), (9,10)


Edge Case 1: Empty input
Input: A = [], B = []
Output: 0


Edge Case 2: Fully overlapping segments
Input: A = [1, 1, 1], B = [5, 5, 5]
Output: 1


<br><br><br>

> **Difficulty level**
> easy

---

Located on a line are N segments, numbered from 0 to N − 1, whose positions are given in arrays A and B. For each I (0 ≤ I < N) the position of segment I is from A[I] to B[I] (inclusive). The segments are sorted by their ends, which means that B[K] ≤ B[K + 1] for K such that 0 ≤ K < N − 1.

Two segments I and J, such that I ≠ J, are overlapping if they share at least one common point. In other words, A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J].

We say that the set of segments is non-overlapping if it contains no two overlapping segments. The goal is to find the size of a non-overlapping set containing the maximal number of segments.

For example, consider arrays A, B such that:

A[0] = 1 B[0] = 5 A[1] = 3 B[1] = 6 A[2] = 7 B[2] = 8 A[3] = 9 B[3] = 9 A[4] = 9 B[4] = 10

The segments are shown in the figure below.
![img1](./img1.png)


The size of a non-overlapping set containing a maximal number of segments is 3. For example, possible sets are {0, 2, 3}, {0, 2, 4}, {1, 2, 3} or {1, 2, 4}. There is no non-overlapping set with four segments.

Write a function:

class Solution { public int solution(int[] A, int[] B); }


that, given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.

For example, given arrays A, B shown above, the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..30,000];
each element of arrays A and B is an integer within the range [0..1,000,000,000];
A[I] ≤ B[I], for each I (0 ≤ I < N);
B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1).