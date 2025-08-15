Problem:

Road roller drives required to patch potholes

Interpretation:
there are N potholes on a straight road parallel to the y-axis, the positions of the potholes are described by two arrays of integers, X and Y, The K-th pothole (for K within the range [0..N-1]) is located at coordinates X[K], Y[K]

in order to fix the potholes, a road roller of width W will be used, the road roller can only drive along the street, parallel to y-axis, it can start driving from an y x coordinates at the beginning of the road (a point whose y coordinate is equal to 0). During one drive, for a chosen starting point (x,0) of the road roller's left end, the road roller drives upwards and patches all potholes on its way that fall within the width of the road roller, W, and are tot he right of its starting position, x. In other words, it patches all the potholes whose first coordinate is between x and x+W inclusive. 

What's the minimum number of road roller drives required to patch all the potholes

e.g. 
X=[2,4,2,6,7,1], Y=[0,5,3,2,1,5], W=2, Ans=3
X=[4,8,2,2,1,4], Y=[1,2,3,1,2,3], W=3, Ans=2
X=[0,3,6,5], Y=[0,3,2,4], W=1, Ans=3


<br><br><br>

> **Difficulty level**
> medium


