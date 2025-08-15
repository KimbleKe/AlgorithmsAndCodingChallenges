# author: Kimble Ke
# date: 2025.8.15

def solution(A, B):
  pass
  
  def solution(X, Y, W):
    """
    Return the minimum number of road-roller drives to patch all potholes.

    X: list[int] - x-coordinates of potholes
    Y: list[int] - y-coordinates (unused)
    W: int       - roller width
    """
    if not X:
        return 0

    xs = sorted(X)           # O(N log N)
    drives = 0
    i, n = 0, len(xs)

    while i < n:
        start = xs[i]
        end = start + W      # inclusive coverage [start, start+W]
        drives += 1

        # skip all potholes covered by this drive
        i += 1
        while i < n and xs[i] <= end:
            i += 1

    return drives