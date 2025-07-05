# author: Kimble Ke
# date: 2025.7.2

# O(N) solution
from collections import deque
 
def solution(K, A):
    N = len(A)
    left = 0
    count = 0
    maxDeque = deque() # indices of potential max values
    minDeque = deque() # indices of potential min values
 
    for right in range(N):
        # update maxDeque: remove all smaller values from the end
        while maxDeque and A[maxDeque[-1]] < A[right]:
            maxDeque.pop()
        maxDeque.append(right)
 
        # update minDeque: remove all larger values from the end
        while minDeque and A[minDeque[-1]] > A[right]:
            minDeque.pop()
        minDeque.append(right)
 
        # if current window is invalid, move left forward
        while A[maxDeque[0]] - A[minDeque[0]] > K:
            left += 1
            # remove indices outside the window
            if maxDeque[0] < left:
                maxDeque.popleft()
            if minDeque[0] < left:
                minDeque.popleft()
 
        # all slices [left..right], [left+1..right], ..., [right..right] are valid
        count += (right - left + 1)
        if count > 1_000_000_000:
            return 1_000_000_000
 
    return count

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        # example input file contains (2, [3, 5, 7, 6, 3]) where K = 2 and A = [3, 5, 7, 6, 3]
        print("Usage: python3 codingSolutions/CountBoundedSlices.py codingSolutions/input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        line = f.read().strip()
        K, A = eval(line) 

    result = solution(K, A)
    print(result)