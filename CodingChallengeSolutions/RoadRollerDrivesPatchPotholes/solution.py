# author: Kimble Ke
# date: 2025.8.15

def solution(X, Y, W):
    """
      Note: the y-axis is actually irrelevant to the solution, because the road roller drives"
			upward and patches all the potholes regardless of how high or large the y-axis is located
    """

    if not X: return 0

    xs = len(X)
    SortedX = sorted(X)
    drives = 0
    i = 0

    while i < xs:
        left_of_road_roller = SortedX[i]
        right_of_road_roller = left_of_road_roller + W
        drives += 1
        i+=1
        while i < xs and SortedX[i] <= right_of_road_roller:
            i += 1
    
    return drives
