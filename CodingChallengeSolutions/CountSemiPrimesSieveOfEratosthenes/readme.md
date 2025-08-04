1. Problem Description
  count the semiprime numbers in the given range [a..b]

Given integers N, P, and Q (where P and Q are arrays of indices), count the number of semi-primes in each range [P[i]..Q[i]]. A semi-prime is a product of exactly two prime numbers (not necessarily distinct).

2. Example Input/Output
Input:
N = 26, P = [1, 4, 16], Q = [26, 10, 20]
Output: [10, 4, 0]
Explanation:

Range 1-26 contains 10 semi-primes (4,6,9,10,14,15,21,22,25,26)

Range 4-10 contains 4 semi-primes (4,6,9,10)

Range 16-20 contains 0 semi-primes

Edge Case (N=1):
Input: N=1, P=[1], Q=[1]
Output: [0]

Edge Case (No Semi-Primes):
Input: N=5, P=[2], Q=[3]
Output: [0]


<br><br><br>

> **Difficulty level**
> medium

---

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

P[0] = 1 Q[0] = 26 P[1] = 4 Q[1] = 10 P[2] = 16 Q[2] = 20
content_copy
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

class Solution { public int[] solution(int N, int[] P, int[] Q); }
content_copy

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

P[0] = 1 Q[0] = 26 P[1] = 4 Q[1] = 10 P[2] = 16 Q[2] = 20
content_copy
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P and Q is an integer within the range [1..N];
P[i] ≤ Q[i].