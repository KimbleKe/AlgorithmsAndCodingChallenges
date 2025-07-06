def dfs(graph, start, goal, visited=None):
  if visited is None:
    visited = set()
  if start == goal:
    return [start]
  visited.add(start)
  for neighbor in graph.get(start, []):
    if neighbor not in visited:
      path = dfs(graph, neighbor, goal, visited)
      if path:
        return [start] + path
  return None
