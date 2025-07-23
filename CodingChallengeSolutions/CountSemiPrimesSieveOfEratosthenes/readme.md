1. Problem Description
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
> medium to hard