def dls(graph, current, goal, depth, path):
  if depth == 0 and current == goal:
    return path + [current]
  if depth > 0:
    for neighbor in graph.get(current, []):
      result = dls(graph, neighbor, goal, depth - 1, path + [current])
      if result:
        return result
  return None

def iddfs(graph, start, goal, max_depth):
  for depth in range(max_depth + 1):
    result = dls(graph, start, goal, depth, [])
    if result:
      return result
  return None
