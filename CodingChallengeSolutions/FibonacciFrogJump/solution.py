# author: Kimble Ke
# date: 2025.7.24
 
# Time complexity O(N * sqrt(N))
# Space complexity O(N)
def solution(A):
	# Generate all Fibonacci numbers up to len(A) + 1
	# The frog can jump any number of steps that is a Fibonacci number
	F = [0, 1]
	while F[-1] <= len(A) + 1:
		F.append(F[-1] + F[-2])  # Generate next Fibonacci number
	F = F[2:]  # Remove the first two (0 and 1) as jumps can't be of size 0 and 1 step is duplicated

	from collections import deque

	N = len(A)  # Number of positions on the river (leaves)
	# visited[i] means whether the frog has already jumped to position i
	visited = [False] * (N + 1)
	queue = deque()
	# Start from position -1 (before the river starts), with 0 jumps
	queue.append((-1, 0))  # Each element in queue is (current_position, jump_count)

	while queue:
		pos, jumps = queue.popleft()  # Get current state
		# Try all possible Fibonacci jumps from the current position
		for f in F:
			next_pos = pos + f  # New position after a jump of size f

			if next_pos == N:
				# Reached the other side of the river (right bank)
				return jumps + 1

			# Ensure the next position is within bounds, has a leaf (A[next_pos] == 1), and not yet visited
			if 0 <= next_pos < N and A[next_pos] == 1 and not visited[next_pos]:
				visited[next_pos] = True  # Mark the position as visited
				queue.append((next_pos, jumps + 1))  # Add new position and jump count to queue

	# If queue is exhausted and we never reach the end, return -1 (impossible)
	return -1


