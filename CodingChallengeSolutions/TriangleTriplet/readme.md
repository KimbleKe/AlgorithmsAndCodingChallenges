Problem: TriangleTriplet
Task Description:
Given an array A of N integers, determine whether there exists a triplet (P, Q, R) such that 0 ≤ P < Q < R < N and the triplet satisfies the triangle inequality:
A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
Return 1 if such a triplet exists, otherwise return 0.

Examples:
A = [10, 2, 5, 1, 8, 20] → Returns 1 (triplet (10, 5, 8)).

A = [10, 50, 5, 1] → Returns 0 (no valid triplet).

Constraints:
N is an integer within [0..100,000].

Each element in A is within [−2,147,483,648..2,147,483,647].

Time: O(N log N)

Space: O(1) (if input can be modified).



<br><br><br>

> **Difficulty level**
> easy