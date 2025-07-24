# graph = {
#   'A': ['B', 'C'],
#   'B': ['D', 'E'],
#   'C': ['F'],
#   'D': [],
#   'E': ['G'],
#   'F': [],
#   'G': []
# }

#        A
#      /   \
#     B     C
#    / \     \
#   D   E     F
#        \
#         G

# input
# iddfs(graph, 'A', 'G', 4)

# output
# ['A', 'B', 'E', 'G']

# Edge case
# iddfs(graph, 'A', 'Z', 5)
# None


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
