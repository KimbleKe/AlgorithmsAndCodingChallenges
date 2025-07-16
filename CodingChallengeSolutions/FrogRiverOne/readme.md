Problem Statement
A small frog wants to get to the other side of a river. The frog is initially located at position 0 and wants to reach position X. Leaves fall from a tree onto the river at different positions. Given array A where A[K] represents the position where one leaf falls at time K, find the earliest time when the frog can jump from position 0 to position X.

Examples
X = 5, A = [1, 3, 1, 4, 2, 3, 5, 4] → Output 6 (At time 6, all positions 1-5 are covered)

X = 2, A = [2, 2, 2, 2] → Output -1 (Never reaches position 1)

X = 3, A = [1, 2, 1] → Output -1 (Never reaches position 3)