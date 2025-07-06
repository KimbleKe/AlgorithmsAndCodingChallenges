from collections import deque

def bidirectional_bfs(graph, start, goal):
  if start == goal:
    return [start]
  
  front = {start}
  back = {goal}
  front_parents = {start: None}
  back_parents = {goal: None}

  while front and back:
    # Expand smaller frontier
    if len(front) > len(back):
      front, back = back, front
      front_parents, back_parents = back_parents, front_parents

    next_front = set()
    for node in front:
      for neighbor in graph.get(node, []):
        if neighbor in back_parents:
          # Reconstruct path
          path = []
          n = node
          while n:
            path.append(n)
            n = front_parents[n]
          path = path[::-1]
          n = neighbor
          while n:
            path.append(n)
            n = back_parents[n]
          return path
        if neighbor not in front_parents:
          front_parents[neighbor] = node
          next_front.add(neighbor)
    front = next_front
  return None
