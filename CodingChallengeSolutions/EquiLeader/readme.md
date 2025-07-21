Problem: EquiLeader
Task Description:
Given a non-empty array A of N integers, find the number of equi-leaders. An equi-leader occurs when a value is the leader (appears more than half the time) in both the left and right parts of an index split.

Examples:
A = [4, 3, 4, 4, 4, 2] → Returns 2

Equi-leaders at indices 0 and 2 (value 4 dominates both sides).

A = [1, 2, 3, 4, 5] → Returns 0 (no leader exists).

Constraints:
N is within [1..100,000].

Each element in A is within [−1,000,000,000..1,000,000,000].

Time: O(N)

Space: O(1)