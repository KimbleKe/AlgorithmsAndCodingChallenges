# author: Kimble Ke
# date: 2025.7.21
 
# this problem is extended version of Dominator problem
# the core idea here is firstly finding the global leader, 
# then count the number of indices (where global leader locate) where there are equileaders
# O(N) Time, O(1) Space
def solution(A):
	if not A:
		return 0

	# Step 1: Find the leader candidate
	candidate = None
	count = 0
	for num in A:
		if count == 0:
			candidate = num
			count = 1
		else:
			count += 1 if num == candidate else -1

	# Step 2: Verify if the candidate is the actual leader
	total_leader_count = A.count(candidate)
	if total_leader_count <= len(A) // 2:
		return 0

	# Step 3: Count equi-leaders
	equi_leaders = 0
	left_leader_count = 0
	right_leader_count = 0
	for i in range(len(A)):
		if A[i] == candidate:
			left_leader_count += 1
		left_size = i + 1
		right_size = len(A) - left_size
		right_leader_count = total_leader_count - left_leader_count
		if left_leader_count > left_size // 2 and right_leader_count > right_size // 2:
			equi_leaders += 1
	return equi_leaders
