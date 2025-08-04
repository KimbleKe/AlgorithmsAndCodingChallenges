1. Problem Description
  count factors of given number n.

Given a positive integer N, compute the number of its positive divisors (factors). For example, 24 has 8 divisors (1, 2, 3, 4, 6, 8, 12, 24).

2. Example Input/Output
Input: 24
Output: 8 (factors: 1, 2, 3, 4, 6, 8, 12, 24)

Edge Case 1 (Prime Number):
Input: 13
Output: 2 (1, 13)

Edge Case 2 (Square Number):
Input: 16
Output: 5 (1, 2, 4, 8, 16)

Edge Case 3 (N = 1):
Input: 1
Output: 1 (only 1)


<br><br><br>

> **Difficulty level**
> easy

---

A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

class Solution { public int solution(int N); }
content_copy

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].