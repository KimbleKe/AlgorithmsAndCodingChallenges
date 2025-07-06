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
