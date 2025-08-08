Problem:
Given a string made with N letter, count the different letters appear in both uppercase and lowercase where all lowercase occurrences of the given letter appear before any upper occurrency.
e.g.
letters = aaAbcCABBc, result=2
letters = xyzXYZabcABC, result=6
letters = ABCabcAefG, result=0

key observation: 
- for any letter, the dictionary will only record its index when it appears for the first time, any re-occurence won't be counted, for example, aaAbcCABBc, the last letter c, appears again, but it appears before at index 4, so its position in dictionary is still at index 4. This is important, as recounting can result in wrong answer

<br><br><br>

> **Difficulty level**
> medium


