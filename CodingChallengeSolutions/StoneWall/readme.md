Problem: StoneWall
Task Description:
Given an array H of N positive integers representing the heights of a stone wall's sections, compute the minimum number of rectangular blocks needed to build the wall. Adjacent blocks must have different heights unless they are part of the same block.

Examples:
H = [8, 8, 5, 7, 9, 8, 7, 4, 8] → Returns 7

Blocks: [8], [5,7,9], [8], [7], [4], [8]

H = [1, 2, 3, 4, 5] → Returns 5 (each height needs a separate block)

Constraints:
N is within [1..100,000].

Each element in H is within [1..1,000,000,000].

Time: O(N)

Space: O(N)



<br><br><br>

> **Difficulty level**
> medium