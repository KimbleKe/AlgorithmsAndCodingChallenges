Problem:

An array A consisting of N integers. A tricoloring of this array is a string consisting of N characters such that each character is either ‘R’ (meaning red), ‘G’ (meaning green), ‘B’, (meaning blue). The K-th character of the string (where 0 <= K < N ) denotes the color of the K-th element of the array. A tricoloring is stable if the sum of red elements is equal to the sum of green elements and to the sum of blue elements. A tricoloring does not necessarily use all three colours. The sum of elements of a color that is not used is assumed to be 0

e.g. consider array A=[3,7,2,5,4]
The string “RRGGB” is an example tricoloring of this array. It is not stable, because A[0]+A[1]=10,A[2]+A[3]=7,A[4]=4 and 10 not equal to 7 not equal to 4. on the other hand, tricoloring “RGBBR” is table, because A[0] + A[4] = 7, A[1]=7 and A[2]+A[3]=7

def solution(A) that, given an array A consisting of N integers, returns any stable tricoloring of this array. the function should return the string “impossible” if no stable tricoloring exists.

e.g. given array A=[3,7,2,5,4], the function may return “RGBBR”
given array A=[3,6,9], the function should return “impossible”

N is an integer within range [0..18]
each element of A is an integer within the range [-100000000…100000000]


<br><br><br>

> **Difficulty level**
> hard


