1. Problem Description:
  given array of integers, find the lowest absolute sum of elements.

You are given an array A of N integers. You want to divide each element by assigning a sign (+ or -) such that the absolute value of the total sum is minimized.

That is, you want to find the minimal possible value of:
|sum(S[0]*A[0] + S[1]*A[1] + ... + S[N−1]*A[N−1])|
Where each S[i] is either +1 or -1.

Constraints:

N is an integer within the range [0..20,000]

each element of array A is an integer within the range [−100..100]

2. Example Input/Output:

Example 1:

Input: A = [1, 5, 2, -2]
Output: 0

Explanation:
Choose signs: [1, -5, -2, 2] → sum = 0 → abs(0) = 0

Example 2:

Input: A = [1, 3, 3, 5]
Output: 0

Choose: [-1, 3, -3, 1] → sum = 0

Edge Cases:

[] → 0
[5] → 5
[100, -100] → 0


<br><br><br>

> **Difficulty level**
> hard