Problem: EquiLeader
  find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.

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



<br><br><br>

> **Difficulty level**
> easy

---

A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

A[0] = 4 A[1] = 3 A[2] = 4 A[3] = 4 A[4] = 4 A[5] = 2
content_copy
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

class Solution { public int solution(int[] A); }
content_copy

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

A[0] = 4 A[1] = 3 A[2] = 4 A[3] = 4 A[4] = 4 A[5] = 2
content_copy
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].