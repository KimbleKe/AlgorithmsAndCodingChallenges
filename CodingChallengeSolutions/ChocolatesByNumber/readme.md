1. Problem Description
  there are N chocolates in a circle. Count the number of chocolates you will eat.

Given two positive integers N (number of chocolates arranged in a circle) and M (step size), determine how many chocolates you will eat before encountering an empty wrapper. You start at position 0 and eat every M-th chocolate in a circular arrangement.

2. Example Input/Output
Input: N = 10, M = 4
Output: 5 (Sequence: 0, 4, 8, 2, 6)

Edge Case (M=1):
Input: N = 5, M = 1
Output: 5

Edge Case (N=M):
Input: N = 7, M = 7
Output: 1

Edge Case (Coprime):
Input: N = 9, M = 5
Output: 9


<br><br><br>

> **Difficulty level**
> easy

---

Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

class Solution { public int solution(int N, int M); }
content_copy

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000,000,000].