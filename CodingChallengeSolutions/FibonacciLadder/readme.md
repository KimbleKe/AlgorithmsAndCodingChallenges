1. Problem Description
You are climbing a ladder. The ladder has A[i] rungs, and for each ladder, you can take steps in any Fibonacci number size (e.g., step sizes of 1, 2, 3, 5, 8, ...), but modulo 2^B[i].
You are given two arrays A and B, both of length L. Your task is to calculate how many different ways you can climb each ladder (modulo 2^B[i]), using only Fibonacci steps.
Each result corresponds to one query: result[i] = fib_ways(A[i]) % (2 ** B[i]).

2. Example Input/Output
Input:
A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]
Output: [5, 1, 8, 0, 1]

Explanation:
The number of ways to climb:
4 rungs: 5 ways → mod 8 = 5, mod 4 = 1
5 rungs: 8 ways → mod 16 = 8, mod 8 = 0
1 rung: 1 way → mod 2 = 1

Edge Case (Zero Rungs):
Input: A = [0], B = [1]
Output: [0]

Edge Case (Large Values):
Input: A = [50000], B = [30]
Output: [fib(50000) mod 2^30]


<br><br><br>

> **Difficulty level**
> hard