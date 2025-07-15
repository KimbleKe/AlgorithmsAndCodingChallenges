# author: Kimble Ke
# date: 2025.7.15

# O(N) solution, this is the preferred solution
def cyclic_rotation1(K, A):
  if not A:
    return A
  K = K % len(A)
  return A[-K:] + A[:-K]

# O(N x K) solution
def cyclic_rotation2(K, A):
  if not A:
    return A
  for _ in range(K):
    last_element = A[-1]
    for i in range(len(A)-1, 0, -1):
      A[i] = A[i-1]
    A[0] = last_element
  return A

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 CyclicRotation_debug.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        line = f.read().strip()
        K, A = eval(line) 

    result = cyclic_rotation1(K, A) # use either cyclic_rotation1 or cyclic_rotation2

    print("######## input ########")
    print("K=" + str(K) + ", A=" + str(A))
    print("######## result ########")
    print("result is " + str(result))