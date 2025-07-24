# graph = {
# 	'A': [('B', 2), ('C', 5)],
# 	'B': [('D', 4), ('E', 1)],
# 	'C': [('F', 2)],
# 	'D': [],
# 	'E': [('F', 3)],
# 	'F': []
# }

# start = 'A'
# goal = 'F'

# print(uniform_cost_search(graph, start, goal))
# ['A', 'B', 'E', 'F']

# Edge case
# start = 'A'
# goal = 'Z'  # 'Z' not in graph

# print(uniform_cost_search(graph, start, goal))
# None



import heapq

def uniform_cost_search(graph, start, goal):
  heap = [(0, start, [start])]
  visited = set()

  while heap:
    cost, node, path = heapq.heappop(heap)
    if node == goal:
      return path
    if node in visited:
      continue
    visited.add(node)
    for neighbor, weight in graph.get(node, []):
      if neighbor not in visited:
        heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
  return None
