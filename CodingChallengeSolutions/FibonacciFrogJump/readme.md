1. Problem Description:


A small frog wants to get to the other side of a river. The frog can jump over the river by only landing on positions with leaves (1s) or directly to the end bank. The frog starts before the first position (-1) and can jump only distances that are Fibonacci numbers (1, 2, 3, 5, 8, 13, ...). You are given a binary array A of size N representing the river (1 is a leaf, 0 is water).

Find the minimal number of jumps the frog needs to reach the opposite bank (position N). Return -1 if it is not possible.

2. Example Input/Output Including Edge Cases:
Example 1:
Input: A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
Output: 3
Explanation: Jump from -1 → 4 → 6 → 11 (end).

Example 2:
Input: A = [1, 1, 0, 0, 0]
Output: 2
Explanation: Jump from -1 → 0 → 5 (end).

Edge Case:
Input: A = []
Output: 1  # Can jump directly if len(A) + 1 == a Fibonacci number (1)


<br><br><br>

> **Difficulty level**
> medium

---

The Fibonacci sequence is defined using the following recursive formula:

F(0) = 0 F(1) = 1 F(M) = F(M - 1) + F(M - 2) if M >= 2

A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:

A[0] = 0 A[1] = 0 A[2] = 0 A[3] = 1 A[4] = 1 A[5] = 0 A[6] = 1 A[7] = 0 A[8] = 0 A[9] = 0 A[10] = 0

The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)


that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:

A[0] = 0 A[1] = 0 A[2] = 0 A[3] = 1 A[4] = 1 A[5] = 0 A[6] = 1 A[7] = 0 A[8] = 0 A[9] = 0 A[10] = 0

the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.