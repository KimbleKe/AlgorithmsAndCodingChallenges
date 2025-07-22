1. Problem Description
Given a non-empty array A consisting of N integers representing mountain heights, a peak is an array element that is larger than its neighbors. Flags can only be placed on peaks, with the condition that the distance between any two flags is at least equal to the number of flags. Find the maximum number of flags that can be placed on the mountain peaks.

2. Example Input / Output
Example 1
Input:
A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
Output:
3
Explanation: Peaks at positions 1, 3, 5, 10 — you can place 3 flags with at least 3 distance apart.

Example 2
Input:
A = [1, 2, 3, 4, 5]
Output:
0
Explanation: No peaks exist.

Edge Case 1
Input:
A = []
Output:
0

Edge Case 2
Input:
A = [1]
Output:
0

Edge Case 3
Input:
A = [1, 3, 2]
Output:
1
Explanation: Only one peak at index 1, so max 1 flag.


<br><br><br>

> **Difficulty level**
> hard