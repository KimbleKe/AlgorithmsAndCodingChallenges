Problem: 
  in a given array, find the subset of maximal sum in which the distance between consecutive elements is at most 6.

1. Problem Description
You are given a list A of N integers. Imagine a game where a pebble starts at position 0 and can move forward by 1 to 6 steps at a time (like a dice roll). At each step, the value at the position the pebble lands on is added to the score.

Return the maximum score the pebble can collect to reach the last index (N-1).


2. Example Input/Output
Example 1:
Input: A = [1, -2, 0, 9, -1, -2]
Output: 8

Explanation:
Path: 1 → -2 → 9 → -2 → total = 8


Edge Cases:
A = [5] → Output: 5 (Only one square, max score is the value itself)
A = [-1000, -1000, -1000, -1000, -1000, -1000] → Output: -600 (Only one path exists)


<br><br><br>

> **Difficulty level**
> medium