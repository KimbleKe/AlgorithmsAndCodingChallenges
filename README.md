Coding challenges and solutions
=====================================

__Table of Content__ 
<br>

**1. Algorithms** 
  - Data structure
    - Sequence: list, tuple, range, str, array
    - Set: set, frozenset
    - Mapping: dict, defaultdict, OrderedDict
    - Queue/Stack: deque, queue.Queue, list
    - FrequencyMap: Counter
    - PriorityQueue: heapq
    - Other: namedtuple, bisect, custom classes
  - Algorithm basics
    - iteration, array, timeComplexity, countingElem, prefixSum, sorting, stack, leader, maxSlice, primeNumber, sieve, euclideanAlgorithm, fibonacci, binarySearch, caterpillarMethod, greedyAlgorithm, dynamicProgramming
  - Search
    - Array search: linearSearch, binarySearch, jumpSearch, exponentialSearch, fibonacciSearch, interpolationSearch, blockSearch
    - Tree graph search: bestFirstSearch, bidirectionalSearch, breadthFirstSearch, depthFirstSearch, dijkstra, iterativeDeepeningDFS, uniformCostSearch
    - Graph algorithm: DFS/BFS, dijkstra, Bellman-Ford, Floyd-Warshall, Kruskal / Prim - Minimum Spanning Tree (MST), topologicalSort, Tarjan’s / Kosaraju’s, Union-Find / Disjoint Sets, A* Search 
  - Sorting
    - bubbleSort, countingSort, heapSort, insertionSort, mergeSort, quickSort, radixSort, selectionSort, shellSort, timSort
  - Dynamic Programming(DP)
    - fibonacci / staircase, knapsack, longestCommonSubsequence, matrixChainMultiplication, editDistance, coinChange, DP on Trees / Bitmasks / States
  - Greedy algorithm
    - activitySelection, huffmanCoding, Kruskal’s Algorithm, dijkstra (with heap), EgyptianFraction
  - Backtracking
    - N-Queens, sudokuSolver, subset / Combination Generator, permutations
  - Recursion
    - factorial / fibonacci, treeTraversals, Tower of Hanoi
  - Maths algorithm
    - Euclidean Algorithm (GCD / LCM), Sieve of Eratosthenes, Modular Exponentiation, Miller-Rabin, Chinese Remainder Theorem, binaryExponentiation
  - Bit manipulation
    - countSetBits, XOR Tricks, Bitmask DP, Bitwise Operators (AND, OR, XOR, NOT, SHIFT)
  - String algorithm
    - Rabin-Karp, KMP (Knuth-Morris-Pratt), Z-Algorithm, Trie, suffixArray / Tree
  - Geometric algorithm
    - Convex Hull (Graham Scan, Jarvis March), lineIntersection, closest Pair of Points, rotatingCalipers
  - Randomized & Probabilistic algorithm
    - randomized QuickSort, Monte Carlo / Las Vegas, reservoirSampling, hashing
  - Sliding Window / Two Pointers
    - MaxSubArray, longestSubstringWithoutRepeatingChars, Two-sum / Three-sum
  - Heap and Priority Queue Based
    - Kth largest element, merge k sorted arrays, dijkstra’s
  - Union-Find / Disjoint Set
    - Find + Union, pathCompression
  - Topological algorithm
    - topologicalSort, Kahn’s Algorithm
<br>

**2. Coding challenges & solutions**
  - (refer to below "Coding challenges" section)

## Coding challenges

#### Total number of challenges
- Easy=27, Medium=20, Hard=11
- Total=58

#### Easy Problems

| # | Problem Name | Algorithm/Approach | Time Complexity | Space Complexity |
|---|-------------|--------------------|-----------------|------------------|
| 1 | BinaryGap | Bit manipulation | O(log N) | O(log N) |
| 2 | CyclicRotation | Array rotation with modulo | O(N) | O(N) |
| 3 | ArrListLen | Linked list traversal | O(N) | O(1) |
| 4 | BugFixingReverseNumber | Debugging/edge cases | O(1) | O(1) |
| 5 | CountDivisibles | Mathematical formula | O(1) | O(1) |
| 6 | DistinctValuesInArray | HashSet tracking | O(N) | O(N) |
| 7 | DoubleDigitsSum | Mathematical operations | O(1) | O(1) |
| 8 | FrogJump | Ceiling division | O(1) | O(1) |
| 9 | FrogRiverOne | HashSet tracking | O(N) | O(N) |
| 10 | IncreaseTheDigits | String manipulation | O(N) | O(N) |
| 11 | MaxProductOfThree | Sorting + greedy | O(N log N) | O(1) |
| 12 | MaxProfit | Single pass (Kadane-like) | O(N) | O(1) |
| 13 | MissingInteger | HashSet tracking | O(N) | O(N) |
| 14 | NestedBrackets | Stack validation | O(N) | O(N) |
| 15 | NestingBrackets | Balance counting | O(N) | O(1) |
| 16 | OddOccurrencesInArray | Bitwise XOR | O(N) | O(1) |
| 17 | PassingCars | Prefix sums | O(N) | O(1) |
| 18 | PermMissingElem | Mathematical formula | O(N) | O(1) |
| 19 | PermutationArrayCheck | HashSet validation | O(N) | O(N) |
| 20 | StrSymmetryPoint | String palindrome check | O(N) | O(1) |
| 21 | TapeEquilibrium | Prefix sums | O(N) | O(1) |
| 22 | TreeHeight | DFS/BFS traversal | O(N) | O(N) |
| 23 | TriangleTriplet | Sorting + greedy | O(N log N) | O(1) |
| 24 | CountFactors | Optimized Trial Division | O(√N) | O(1) |
| 25 | MinimumPerimeterRectangle | Optimized Trial Division | O(√N) | O(1) |
| 26 | AbsoluteDistinctValue | Hash Set + Absolute Value | O(N) | O(N) |
| 27 | Array Reversal | In-Place Swapping | O(N) | O(1) |

#### Medium Problems

| # | Problem Name | Algorithm/Approach | Time Complexity | Space Complexity |
|---|-------------|--------------------|-----------------|------------------|
| 1 | CountBoundedSlices | Sliding window | O(N) | O(1) |
| 2 | Dominator | Moore's voting | O(N) | O(1) |
| 3 | EquiLeader | Leader + prefix sums | O(N) | O(N) |
| 4 | FirstUnique | LinkedHashSet | O(N) | O(N) |
| 5 | Fish | Stack simulation | O(N) | O(N) |
| 6 | GenomicRangeQuery | Prefix sums | O(N+M) | O(N) |
| 7 | MaxCounters | Lazy propagation | O(N+M) | O(N) |
| 8 | MaxSliceSum | Kadane's algorithm | O(N) | O(1) |
| 9 | MinAbsSumOfTwo | Sorting + two pointers | O(N log N) | O(1) |
| 10 | MinimumAverageSlice | Prefix sums | O(N) | O(1) |
| 11 | MissingPositiveIntegerInArray | In-place hashing | O(N) | O(1) |
| 12 | StoneWall | Stack tracking | O(N) | O(N) |
| 13 | TreeLongestZigZag | DFS traversal | O(N) | O(N) |
| 14 | MaxDoubleSlice | Prefix Sums, Kadane's algorithm, DynamicProgramming | O(N) | O(N) |
| 15 | CountNonDivisible | Divisor Counting + Frequency Map | O(N log N) | O(N + max(A)) |
| 16 | ChocolatesByNumber | Math (Least Common Multiple LCM and Greatest Common Divisor GCD with Euclidean Algorithm) | O(log N) | O(1) |
| 17 | CommonPrimeDivisors | GCD with Prime Divisors Elimination | O(N * log^2(M)) | O(1) |
| 18 | MushroomPicker | Prefix Sum + Sliding Window | O(N) | O(N) |
| 19 | ArraySwapToEqualSum | Hashing + Math Equation | O(N + M) | O(M) |
| 20 | MinMaxDivision | Binary Search + Greedy Partitioning | O(N log S) | O(1) |


#### Hard Problems

| # | Problem Name | Algorithm/Approach | Time Complexity | Space Complexity |
|---|-------------|--------------------|-----------------|------------------|
| 1 | ArrayInversionCount | Modified merge sort | O(N log N) | O(N) |
| 2 | CountriesCount | DFS/BFS (flood fill) | O(N*M) | O(N*M) |
| 3 | DiscIntersections | Line sweep algorithm | O(N log N) | O(N) |
| 4 | DisappearingPairs | Stack/DFS simulation | O(N) | O(N) |
| 5 | PolygonConcavityIndex | Computational geometry | O(N) | O(1) |
| 6 | Flags | Peak Detection, Binary Search, Greedy Placement | O(N) | O(N) |
| 7 | Peaks | Prefix Sum + Divisors Check | O(N * √N) | O(N) |
| 8 | CountSemiPrimesSieveOfEratosthenes | Sieve of Eratosthenes + Prefix Sum | O(N log log N + M) | O(N) |
| 9 | FibonacciFrogJump | BFS with Fibonacci bounds | O(N * sqrt(N)) | O(N) |
| 10 | FibonacciLadder | DP (Dynamic Programming) + Fibonacci with Bitwise Modulo | O(L + N) | O(N) |
| 11 | NailingPlanks | Binary Search + Greedy Selection | O((N + M) log M) | O(M) |


