Problem Statement:
Given an array A of integers and an integer K, perform a cyclic rotation of the array. Each rotation shifts every element to the right by one position, with the last element moving to the front.

Examples
Input: A = [3, 8, 9, 7, 6], K = 1
Output: [6, 3, 8, 9, 7]
(Explanation: 6 moves to the front, others shift right.)

Input: A = [1, 2, 3, 4], K = 4
Output: [1, 2, 3, 4]
(Explanation: After 4 rotations, the array returns to its original state.)

Edge Case: A = [], K = 5
Output: [] (Empty array remains unchanged.)