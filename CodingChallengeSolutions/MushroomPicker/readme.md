1. Problem Description
You are given a non-empty array A of N integers representing mushrooms placed on a line, and an integer K representing the starting position of the picker. You have M moves, and each move lets you go left or right by one index. Your goal is to collect as many mushrooms as possible in these M moves by moving and picking mushrooms from the cells you pass or stop at.

Write a function:
  def solution(A, K, M):
that returns the maximum number of mushrooms that can be collected in M moves.

2. Example Input/Output
Input:
A = [2, 3, 7, 5, 1, 3, 9]
K = 4
M = 6

Output:
25

Explanation:
One optimal strategy: Move left 3 steps to index 1 and then right 3 steps to index 4. The mushrooms collected will be:
A[1] + A[2] + A[3] + A[4] = 3 + 7 + 5 + 1 = 16.

Another better path is: move right to index 6, collecting A[4] + A[5] + A[6] = 1 + 3 + 9 = 13, then go back to index 2 in left direction, collecting A[2] + A[3] = 7 + 5 = 12. Total = 25.


<br><br><br>

> **Difficulty level**
> medium