Problem: PassingCars
Task Description:
Given a non-empty array A consisting of N integers where 0 represents a car traveling east and 1 represents a car traveling west, count the number of passing cars (pairs (P, Q) where 0 ≤ P < Q < N and A[P] = 0 and A[Q] = 1). If the count exceeds 1,000,000,000, return -1.

Examples:
A = [0, 1, 0, 1, 1] → Returns 5

Pairs: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

A = [1, 1, 0] → Returns 0 (no eastbound cars before westbound).

Constraints:
N is an integer within [1..100,000].

Each element in A is either 0 or 1.

Time: O(N)

Space: O(1)