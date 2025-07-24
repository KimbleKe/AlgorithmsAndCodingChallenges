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
> hard