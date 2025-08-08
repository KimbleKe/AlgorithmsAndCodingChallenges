Problem:

there are N points on a plane, numbered from 0 to N-1, the coordinates of the K-th point are X[K], Y[K], find any triangle with vertices at three of the given points, such that no other point lies inside this triangle (and no other points, except vertices, on the boundary of the triangle). the triangle must have a positive area. 

given 2 arrays X and Y consisting of N integers each, representing points on the plan, return an array B consisting of exactly three integers, such that the points with indices B[0], B[1], B[2] form an empty triangle

if no such triplet, return an empty array instead

given X=[1,4,3,2,3], Y=[4,3,1,1,2], there are N=5 points on the plan
the function could return [0,1,4] since points 0,1,4 form an empty triangle
[0,1,2] is incorrect, since triangle 0,1,2 contains point 4 inside
[0,1,3] is incorrect, since triangle 0,1,3 contains point 4 on the boundary
[1,3,4] is incorrect, since triangle 1,3,4 do not form a triangle with positive area
[4,2,3] is correct, since points 2,3,4 also form an empty triangle

given X=[0], Y=[0], the function should return an empty area, since having only one point, cannot build any triangle

given X=[0,1,2,4,4,5,6] and Y=[0,1,2,3,4,5,6] the function would return [2,3,4], since points (2,2), (4,3), (4,4) form an empty triangle that contains no points inside it or on its edges

given X=[0,1,3,0,0,2] and Y=[3,0,0,1,2,0] the function returns [1,3,5]


<br><br><br>

> **Difficulty level**
> hard


