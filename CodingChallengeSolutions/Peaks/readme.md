1. Problem Description
Given a non-empty array A of N integers representing mountain heights, divide the array into the maximum number of blocks (of equal length) where each block contains at least one peak (an element larger than its neighbors).

2. Example Input/Output
Input: [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
Output: 3 (can be divided into 3 blocks: [1,2,3,4], [3,4,1,2], [3,4,6,2])

Edge Case 1 (No Peaks):
Input: [1, 2, 3, 4, 5]
Output: 0

Edge Case 2 (Single Peak):
Input: [1, 3, 2]
Output: 1

Edge Case 3 (All Equal):
Input: [5, 5, 5, 5]
Output: 0


<br><br><br>

> **Difficulty level**
> hard