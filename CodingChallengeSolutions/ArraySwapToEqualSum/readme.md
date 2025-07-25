1. Problem Description
Also named as "SwapSum" problem. Given two arrays A and B of integers, determine if a single swap between any element of A and any element of B can make the sum of both arrays equal. Return True if possible, otherwise False.

2. Example Input/Output
Input:
A = [4, 1, 2, 1, 1, 2], B = [3, 6, 3, 3]
Output: True (Swap 4 in A with 3 in B → sums become 11 each)

Edge Case (No Swap Needed):
Input: A = [1, 2], B = [3, 0]
Output: True (Sums already equal)

Edge Case (Impossible):
Input: A = [1, 2, 3], B = [4, 5, 6]
Output: False


<br><br><br>

> **Difficulty level**
> medium