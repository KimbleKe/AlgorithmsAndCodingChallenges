1. Problem Description
  Count the number of different ways of climbing to the top of a ladder.

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
> medium

---

You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

with your first step you can stand on rung 1 or 2,
if you are on rung K, you can move to rungs K + 1 or K + 2,
finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

1, 1, 1 and 1 rung,
1, 1 and 2 rungs,
1, 2 and 1 rung,
2, 1 and 1 rungs, and
2 and 2 rungs.
Given N = 5, you have eight different ways of climbing, ascending by:

1, 1, 1, 1 and 1 rung,
1, 1, 1 and 2 rungs,
1, 1, 2 and 1 rung,
1, 2, 1 and 1 rung,
1, 2 and 2 rungs,
2, 1, 1 and 1 rungs,
2, 1 and 2 rungs, and
2, 2 and 1 rung.
The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].

For example, given L = 5 and:

    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1
the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

L is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..L];
each element of array B is an integer within the range [1..30].