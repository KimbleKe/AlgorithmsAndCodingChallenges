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

# input
# bfs(graph, 'A', 'F')
# bfs(graph, 'D', 'Z')

# output
# ['A', 'C', 'F']
# None

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
