# author: Kimble Ke
# date: 2025.7.21
 
# O(N) Time, O(N) Space
def solution(H):
	stack = [] # memory to store heights seen 
	blocks = 0
	for height in H:
		while stack and stack[-1] > height:
			stack.pop()  # remove the height seen before
		if not stack or stack[-1] < height:
			stack.append(height)
			blocks += 1  # increment blocks needed when height increase 
	return blocks