# author: Kimble Ke
# date: 2025.7.6
 
# O(N*M) solution
from collections import deque
from typing import List

def solution(A: List[List[int]]) -> int:
  if not A or not A[0]:
    return 0

  rows, cols = len(A), len(A[0])
  visited = [[False] * cols for _ in range(rows)]
  countries = 0

  # Directions: up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  for r in range(rows):
    for c in range(cols):
      if not visited[r][c]:
        countries += 1
        color = A[r][c]
        queue = deque([(r, c)])
        visited[r][c] = True

        while queue:
          cr, cc = queue.popleft()
          for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < rows and 0 <= nc < cols:
              if not visited[nr][nc] and A[nr][nc] == color:
                visited[nr][nc] = True
                queue.append((nr, nc))
                            
  return countries
