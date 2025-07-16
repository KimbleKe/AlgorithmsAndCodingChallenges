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
        print("-------- iterator " + str(right) + " --------")

        # update maxDeque: remove all smaller values from the end
        while maxDeque and A[maxDeque[-1]] < A[right]:
            print("A[maxDeque[-1]]=" + str(A[maxDeque[-1]]) + " < A[right]=" + str(A[right]))
            print("maxDeque pop " + str(maxDeque[-1]))
            maxDeque.pop()
        maxDeque.append(right)
        print("maxDeque append " + str(right))
 
        # update minDeque: remove all larger values from the end
        while minDeque and A[minDeque[-1]] > A[right]:
            print("A[minDeque[-1]]=" + str(A[minDeque[-1]]) + " > A[right]=" + str(A[right]))
            print("minDeque pop " + str(minDeque[-1]))
            minDeque.pop()
        minDeque.append(right)
        print("minDeque append " + str(right))
 
        # if current window is invalid, move left forward
        while A[maxDeque[0]] - A[minDeque[0]] > K:
            left += 1
            print("if current window is invalid, move left forward, left=" + str(left) + "; A[maxDeque[0]]=" + str(A[maxDeque[0]]) + " - A[minDeque[0]]=" + str(A[minDeque[0]]) + " > K=" + str(K))

            # remove indices outside the window
            if maxDeque[0] < left:
                print("maxDeque[0]=" + str(maxDeque[0]) + " < left=" + str(left) + "; maxDeque will pop " + str(maxDeque[0]))
                maxDeque.popleft()
            if minDeque[0] < left:
                print("minDeque[0]=" + str(minDeque[0]) + " < left=" + str(left) + "; minDeque will pop " + str(minDeque[0]))
                minDeque.popleft()
 
        # all slices [left..right], [left+1..right], ..., [right..right] are valid
        print("right=" + str(right) + ", left=" + str(left))
        count += (right - left + 1)
        print("count=" + str(count))

        if count > 1_000_000_000:
            return 1_000_000_000
 
    return count

###############################################################################
# print input and output
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        # example input file contains (2, [3, 5, 7, 6, 3]) where K = 2 and A = [3, 5, 7, 6, 3]
        print("Usage: python3 CountBoundedSlices_debug.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        line = f.read().strip()
        K, A = eval(line) 

    result = solution(K, A)

    print("######## input ########")
    print("K=" + str(K) + ", A=" + str(A))
    print("######## result ########")
    print("result is " + str(result))