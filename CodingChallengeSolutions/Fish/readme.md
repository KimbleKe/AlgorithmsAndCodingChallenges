Problem: Fish
Task Description:
Given two arrays A (fish sizes) and B (fish directions, 0 for upstream and 1 for downstream), compute the number of fish that will survive. Fish moving downstream will eat smaller upstream fish they encounter, and vice versa.

Examples:
A = [4, 3, 2, 1, 5], B = [0, 1, 0, 0, 0] → Returns 2

Fish 4 (up) and fish 5 (up) survive.

A = [3, 4, 2, 1, 5], B = [1, 0, 0, 0, 0] → Returns 4


Constraints:
N (number of fish) is within [1..100,000].

Each element in A is within [0..1,000,000,000].

Time: O(N)

Space: O(N)