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
