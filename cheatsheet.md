Coding challenges and solutions
=====================================

**string/numbers manipulation**
- str(), int(), float(), abs(), len(), reversed()
- modulo, //, %
- ''.join(string)

**Operators** 
- +=, -=, //=, /=, %= 
- string concatenation is O(N) in worst case

**looping**
- for i in range(A)
- for i in A
- for while else loop
- while loop

**data structure**
- array, stack, queue, list
- tuple  #immutable
- hashset  #unordered, unique elements
- dictionary  #key-value pair
- deque  #from Collection library, optimised for fast append/pop at both ends

**array, stack, queue**
- array=[], A=[]
  - A.sort()
  - sorted(A)
  - len(A)
  - A.insert(idx, 'x')
  - A.remove('x')
  - A.index(element)
  - A.count(element)
  - list(A)
  - B = A.copy()
  - A+B
  - A*10
  - A.clear()
- stack=[]
  - stack.append('x')
  - stack.pop()
  - zip(A,B)
  - sorted(zip(A, B), key=lambda x: x[0])
  - ''.join(stack)
- slice notation
  - [::1]  # creates a shallow copy of a sequence (e.g., list, string, tuple)
  - [::-1]  # reverse the sequence of array or stack
- sum(A), max(A), min(A)

**hashset**
- S=set(), set(stack)
- set.add('x')
- set.remove('x')
- set.pop() # pop a random element, unlike stack

**common algorithms**
- recursion
- prefix_sum
- GCD (greatest common divisor), LCM (least common multiple), Euclidean algorithm
- Sieve
- Greedy algorithm
- Dynamic programming
- array search algorithms 
  - linearSearch
  - binarySearch
  - jumpSearch
  - exponentialSearch
  - fibonacciSearch
  - interpolationSearch
  - blockSearch
- tree graph search algorithms 
  - depthFirstSearch DFS
  - breadthFirstSearch BFS
  - dijkstra
  - bestFirstSearch BFS
  - bidirectionalSearch,
  - uniformCostSearch UCS
  - iterativeDeepeningDFS
- sorting algorithms 
  - quickSort
  - bubbleSort
  - mergeSort
  - countingSort
  - heapSort
  - insertionSort
  - radixSort
  - selectionSort
  - timSort
  - shellSort