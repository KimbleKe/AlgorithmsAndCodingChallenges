# author: Kimble Ke
# date: 2025.8.8

def solution(X, Y):
  lenX = len(X)
  lenY = len(Y)
  N = lenX

  if not X or not Y or lenX != lenY or lenX <= 2 or lenY <= 2:
    return []

  # 2 * Area with positive or negative sign
  def double_area_with_sign(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)

  # All areas should have same sign and none should be zero, so it's strictly inside
  def is_point_in_triangle(x1, y1, x2, y2, x3, y3, pointX, pointY):
    areaA = double_area_with_sign(x1, y1, x2, y2, pointX, pointY)
    areaB = double_area_with_sign(x2, y2, x3, y3, pointX, pointY)
    areaC = double_area_with_sign(x3, y3, x1, y1, pointX, pointY)
    return (areaA >= 0 and areaB >= 0 and areaC >= 0) or (areaA <= 0 and areaB <= 0 and areaC <= 0)

  for i in range(N):
    for j in range(i + 1, N):
      for k in range(j + 1, N):
        # Check if area is not zero (not collinear)
        triangleArea = double_area_with_sign(X[i], Y[i], X[j], Y[j], X[k], Y[k])
        if triangleArea == 0:
          continue
        # Check if any point is in the triangle
        isValidTriangle = True
        for point in range(N):
          if point == i or point == j or point == k:
            continue
          if is_point_in_triangle(X[i], Y[i], X[j], Y[j], X[k], Y[k], X[point], Y[point]):
            isValidTriangle = False
            break
        if isValidTriangle:
          return [i, j, k]
        
  return []
