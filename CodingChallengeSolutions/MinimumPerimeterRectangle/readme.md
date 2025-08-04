1. Problem Description
  find the minimal perimeter of any rectangle whose area equals N.

Given an integer N, representing the area of a rectangle, find the minimal perimeter of any rectangle whose area is exactly N with integer side lengths.

2. Example Input/Output
Example 1:
Input: N = 30
Output: 22 (Sides: 5 × 6 → Perimeter = 2×(5+6) = 22)

Example 2 (Square Case):
Input: N = 16
Output: 16 (Sides: 4 × 4 → Perimeter = 2×(4+4) = 16)

Edge Case (Prime Number):
Input: N = 13
Output: 28 (Sides: 1 × 13 → Perimeter = 2×(1+13) = 28)

Edge Case (N = 1):
Input: N = 1
Output: 4 (Sides: 1 × 1 → Perimeter = 4)


<br><br><br>

> **Difficulty level**
> easy

---

An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

class Solution { public int solution(int N); }
content_copy

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].