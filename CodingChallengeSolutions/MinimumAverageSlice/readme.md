Problem: MinimumAverageSlice
Task Description:
Given a non-empty array A of N integers, find the starting position of the slice (contiguous subarray) with the minimal average. If multiple slices have the same minimal average, return the smallest starting position.

Examples:
A = [4, 2, 2, 5, 1, 5, 8] → Returns 1

Minimal average is (2 + 2) / 2 = 2 starting at index 1.

A = [1, 2, 3] → Returns 0

Minimal average is 1 / 1 = 1 starting at index 0.

Constraints:
N is an integer within [2..100,000].

Each element in A is within [−10,000..10,000].

Time: O(N)

Space: O(1)