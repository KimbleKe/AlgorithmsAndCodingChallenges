# graph = {
#   'A': ['B', 'C'],
#   'B': ['D', 'E'],
#   'C': ['F'],
#   'D': [],
#   'E': ['F'],
#   'F': []
# }

#      A
#     / \
#    B   C
#   / \    \
#  D   E -- F

# heuristic = {
#   'A': 5,
#   'B': 4,
#   'C': 2,
#   'D': 10,
#   'E': 3,
#   'F': 0
# }

# input
# best_first_search(graph, 'A', 'F', heuristic)
# best_first_search(graph, 'B', 'F', heuristic)


# output
# ['A', 'C', 'F']
# ['B', 'E', 'F']

# Edge case
# disconnected_graph = {
#   'A': ['B'],
#   'B': [],
#   'C': ['D'],
#   'D': []
# }

# heuristic = {
#   'A': 3,
#   'B': 2,
#   'C': 5,
#   'D': 1
# }

# best_first_search(disconnected_graph, 'A', 'D', heuristic)
# None

import heapq

def best_first_search(graph, start, goal, heuristic):
  visited = set()
  heap = [(heuristic[start], start, [start])]

  while heap:
    _, current, path = heapq.heappop(heap)
    if current == goal:
      return path
    visited.add(current)
    for neighbor in graph.get(current, []):
      if neighbor not in visited:
        heapq.heappush(heap, (heuristic[neighbor], neighbor, path + [neighbor]))
  return None
