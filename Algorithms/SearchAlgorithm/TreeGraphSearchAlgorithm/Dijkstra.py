# graph = {
#   'A': [('B', 1), ('C', 4)],
#   'B': [('C', 2), ('D', 5)],
#   'C': [('D', 1)],
#   'D': []
# }

# A --1--> B --2--> C --1--> D
#  \       \
#   \       \--5--> D
#    \
#     \--4--> C

# input
# dijkstra(graph, 'A')

# output
# {
#   'A': 0,     # Distance to self
#   'B': 1,     # A -> B
#   'C': 3,     # A -> B -> C (1 + 2)
#   'D': 4      # A -> B -> C -> D (1 + 2 + 1)
# }


import heapq

def dijkstra(graph, start):
  heap = [(0, start)]
  distances = {start: 0}
  while heap:
    cost, node = heapq.heappop(heap)
    for neighbor, weight in graph.get(node, []):
      new_cost = cost + weight
      if neighbor not in distances or new_cost < distances[neighbor]:
        distances[neighbor] = new_cost
        heapq.heappush(heap, (new_cost, neighbor))
  return distances
