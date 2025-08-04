1. Problem: 
  tie adjacent ropes to achieve the maximum number of ropes of length >= K.

You are given N ropes of various lengths. You are also given an integer K. You need to tie the ropes together (in any order), but only keep the ones whose length is greater than or equal to K.
Two ropes can be tied together by summing their lengths. Your task is to find the maximum number of ropes you can tie such that each has a length ≥ K

2. Example Input/Output Including Edge Cases
Example 1:

Input:
A = [1, 2, 3, 4, 1, 1, 3], K = 4
Output:
3
Explanation:
  Tie rope 0 and 1 → 1+2 = 3 (not enough)
  Tie rope 2 and 3 → 3+4 = 7 → valid
  Rope 4, 5, 6 → 1+1+3 = 5 → valid
  So you can form 3 ropes ≥ 4.

Edge Case 1:
A = [5, 5, 5], K = 10
Output: 1

Explanation: Tie all three ropes: 5+5+5 = 15 → only one valid rope.

Edge Case 2:

A = [1, 1, 1], K = 10
Output: 0

Explanation: No combination can reach 10.


<br><br><br>

> **Difficulty level**
> easy

---

There are N ropes numbered from 0 to N − 1, whose lengths are given in an array A, lying on the floor in a line. For each I (0 ≤ I < N), the length of rope I on the line is A[I].

We say that two ropes I and I + 1 are adjacent. Two adjacent ropes can be tied together with a knot, and the length of the tied rope is the sum of lengths of both ropes. The resulting new rope can then be tied again.

For a given integer K, the goal is to tie the ropes in such a way that the number of ropes whose length is greater than or equal to K is maximal.

For example, consider K = 4 and array A such that:

A[0] = 1 A[1] = 2 A[2] = 3 A[3] = 4 A[4] = 1 A[5] = 1 A[6] = 3
content_copy
The ropes are shown in the figure below.
![img1](./img1.png)


We can tie:

rope 1 with rope 2 to produce a rope of length A[1] + A[2] = 5;
rope 4 with rope 5 with rope 6 to produce a rope of length A[4] + A[5] + A[6] = 5.
After that, there will be three ropes whose lengths are greater than or equal to K = 4. It is not possible to produce four such ropes.

Write a function:

class Solution { public int solution(int K, int[] A); }
content_copy

that, given an integer K and a non-empty array A of N integers, returns the maximum number of ropes of length greater than or equal to K that can be created.

For example, given K = 4 and array A such that:

A[0] = 1 A[1] = 2 A[2] = 3 A[3] = 4 A[4] = 1 A[5] = 1 A[6] = 3
content_copy
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
K is an integer within the range [1..1,000,000,000];
each element of array A is an integer within the range [1..1,000,000,000].