Problem: MaxCounters
Task Description:
You are given an integer N (number of counters) and an array A of M integers. The array A represents operations:

If A[K] = X (where 1 ≤ X ≤ N), increment counter X.

If A[K] = N + 1, set all counters to the current maximum value.

Return the final state of the counters.

Constraints:

N and M are integers within [1, 100,000].

Each element in A is an integer within [1, N + 1].

Example:

N = 5, A = [3, 4, 4, 6, 1, 4, 4]

Result: [3, 2, 2, 4, 2]