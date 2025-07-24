# graph = {
#   'A': ['B', 'C'],
#   'B': ['A', 'D', 'E'],
#   'C': ['A', 'F'],
#   'D': ['B'],
#   'E': ['B', 'F'],
#   'F': ['C', 'E']
# }
#
#      A
#     / \
#    B   C
#   / \   \
#  D   E - F
#
# input
# dfs(graph, 'A', 'F')
# dfs(graph, 'D', 'Z')
#
# output
# ['A', 'B', 'E', 'F']
# None

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
