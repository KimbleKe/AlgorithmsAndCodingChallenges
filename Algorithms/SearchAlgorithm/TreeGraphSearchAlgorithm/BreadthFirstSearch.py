from collections import deque

def bfs(graph, start, goal):
  visited = set()
  queue = deque([(start, [start])])

  while queue:
    current, path = queue.popleft()
    if current == goal:
      return path
    visited.add(current)
    for neighbor in graph.get(current, []):
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, path + [neighbor]))
  return None
