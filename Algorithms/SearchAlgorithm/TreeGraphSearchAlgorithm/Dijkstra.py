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
