Problem: NestedBrackets (Extended Version)
Task Description:
Given a string S consisting of the characters '(', ')', '{', '}', '[', and ']', determine if it is properly nested (i.e., every opening bracket has a corresponding closing bracket of the same type in the correct order).

Examples:
S = "{[()()]}" → Returns 1 (properly nested).

S = "([)()]" → Returns 0 (invalid nesting).

Constraints:
N (length of S) is within [0..1,000,000].

Time: O(N)

Space: O(N) (worst-case, but could be optimized to O(1) if only one bracket type exists).