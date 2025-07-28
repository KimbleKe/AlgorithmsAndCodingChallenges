1. Problem Description
You are given an array A of N integers and an integer K. Divide the array into K or fewer non-empty contiguous blocks so that the largest sum of any block is minimized. Return this minimal possible largest block sum.

2. Example Input/Output
Input:
A = [2, 1, 5, 1, 2, 2, 2], K = 3
Output: 6 (Optimal division: [2,1,5], [1,2,2], [2] → sums 8,5,2 → max=8 is not minimal. Better: [2,1,5,1], [2,2], [2] → sums 9,4,2 → max=9 is worse. Actually, minimal max is 6: [2,1,5], [1,2,2], [2] → sums 8,5,2 → max=8 is not minimal. Correct answer is 6 with division: [2,1], [5,1], [2,2,2] → sums 3,6,6 → max=6)

Edge Case (K = 1):
Input: A = [1, 2, 3], K = 1
Output: 6 (Single block sum)

Edge Case (K >= len(A)):
Input: A = [1, 2, 3], K = 4
Output: 3 (Each element in its own block)


<br><br><br>

> **Difficulty level**
> medium to hard