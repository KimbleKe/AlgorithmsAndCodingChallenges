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
- Easy=33, Medium=23, Hard=5
- Total=61

#### Easy Problems

| # | Problem Name | Algorithm/Approach | Time Complexity | Space Complexity |
|---|-------------|--------------------|-----------------|------------------|
| 1 | BinaryGap | Bit manipulation | O(log N) | O(log N) |
| 2 | CyclicRotation | Array rotation with modulo | O(N) | O(N) |
| 3 | OddOccurrencesInArray | Bitwise XOR | O(N) | O(1) |
| 4 | FrogJump | Ceiling division | O(1) | O(1) |
| 5 | PermutationMissingElem | Mathematical formula | O(N) | O(1) |
| 6 | TapeEquilibrium | Prefix sums | O(N) | O(1) |
| 7 | FrogRiverOne | HashSet tracking | O(N) | O(N) |
| 8 | PermutationCheck | HashSet validation | O(N) | O(N) |
| 9 | PassingCars | Prefix sums | O(N) | O(1) |
| 10 | MissingInteger | HashSet tracking | O(N) | O(N) |
| 11 | DistinctValuesInArray | HashSet tracking | O(N) | O(N) |
| 12 | MaxProductOfThree | Sorting + greedy | O(N log N) | O(1) |
| 13 | TriangleTriplet | Sorting + greedy | O(N log N) | O(1) |
| 14 | NestedBrackets | Stack validation | O(N) | O(N) |
| 15 | NestingBrackets | Stack validation, Balance counting | O(N) | O(1) |
| 16 | Fish | Stack simulation | O(N) | O(N) |
| 17 | StoneWall | Stack tracking | O(N) | O(N) |
| 18 | Dominator | Leader, Moore's voting | O(N) | O(1) |
| 19 | EquiLeader | Leader + prefix sums | O(N) | O(N) |
| 20 | MaxProfit | MaxSlice, Single pass (Kadane-like) | O(N) | O(1) |
| 21 | MaxSliceSum | MaxSlice, Kadane's algorithm | O(N) | O(1) |
| 22 | CountFactors | Prime and composite numbers, Optimized Trial Division | O(√N) | O(1) |
| 23 | MinimumPerimeterRectangle | Prime and composite numbers, Optimized Trial Division | O(√N) | O(1) |
| 24 | ChocolatesByNumber | Math (Least Common Multiple LCM and Greatest Common Divisor GCD with Euclidean Algorithm) | O(log N) | O(1) |
| 25 | AbsoluteDistinctValue | Hash Set + Absolute Value | O(N) | O(N) |
| 26 | MaxNonoverlappingSegments | Greedy Selection Based on End Time | O(N) | O(1) |
--
| 27 | DoubleDigitsSum | Mathematical operations | O(1) | O(1) |
| 28 | BugFixingReverseNumber | Debugging/edge cases | O(1) | O(1) |
| 29 | IncreaseTheDigits | String manipulation | O(N) | O(N) |
| 30 | ArrListLen | Linked list traversal | O(N) | O(1) |
| 31 | StrSymmetryPoint | String palindrome check | O(N) | O(1) |
| 32 | TreeHeight | DFS/BFS traversal | O(N) | O(N) |
| 33 | Array Reversal | In-Place Swapping | O(N) | O(1) |


#### Medium Problems

| # | Problem Name | Algorithm/Approach | Time Complexity | Space Complexity |
|---|-------------|--------------------|-----------------|------------------|
| 1 | MaxCounters | Lazy propagation | O(N+M) | O(N) |
| 2 | CountDivisibles | Prefix sums | O(1) | O(1) |
| 3 | GenomicRangeQuery | Prefix sums | O(N+M) | O(N) |
| 4 | MinimumAverageSlice | Prefix sums | O(N) | O(1) |
| 5 | DiscIntersections | Soring, Line sweep algorithm | O(N log N) | O(N) |
| 6 | MaxDoubleSlice | MaxSlice, Prefix Sums, Kadane's algorithm, DynamicProgramming | O(N) | O(N) |
| 7 | MissingPositiveIntegerInArray | In-place hashing | O(N) | O(1) |
| 8 | Flags | Prime and composite numbers, Peak Detection, Binary Search, Greedy Placement | O(N) | O(N) |
| 9 | Peaks | Prime and composite numbers, Prefix Sum + Divisors Check | O(N * √N) | O(N) |
| 10 | CountNonDivisible | Sieve of Eratosthenes, Divisor Counting, Frequency Map | O(N log N) | O(N + max(A)) |
| 11 | CountSemiPrimesSieveOfEratosthenes | Sieve of Eratosthenes, Prefix Sum | O(N log log N + M) | O(N) |
| 12 | CommonPrimeDivisors | GCD with Prime Divisors Elimination | O(N * log^2(M)) | O(1) |
| 13 | FibonacciFrogJump | Fibonacci numbers, BFS with Fibonacci bounds | O(N * sqrt(N)) | O(N) |
| 14 | FibonacciLadder | Fibonacci numbers, DP (Dynamic Programming) + Fibonacci with Bitwise Modulo | O(L + N) | O(N) |
| 15 | MinMaxDivision | Binary Search + Greedy Partitioning | O(N log S) | O(1) |
| 16 | NailingPlanks | Binary Search + Greedy Selection | O((N + M) log M) | O(M) |
| 17 | MinAbsSumOfTwo | Caterpillar, Sorting + two pointers | O(N log N) | O(1) |
| 18 | NumberSolitaire | Dynamic Programming | O(N) | O(N) |
--
| 19 | CountBoundedSlices | Sliding window | O(N) | O(1) |
| 20 | FirstUnique | LinkedHashSet | O(N) | O(N) |
| 21 | TreeLongestZigZag | DFS traversal | O(N) | O(N) |
| 22 | MushroomPicker | Prefix Sum + Sliding Window | O(N) | O(N) |
| 23 | ArraySwapToEqualSum | Hashing + Math Equation | O(N + M) | O(M) |


#### Hard Problems

| # | Problem Name | Algorithm/Approach | Time Complexity | Space Complexity |
|---|-------------|--------------------|-----------------|------------------|
| 1 | MinAbsSum | DP with Knapsack Variant | O(N * S) | O(S) |
--
| 2 | ArrayInversionCount | Modified merge sort | O(N log N) | O(N) |
| 3 | CountriesCount | DFS/BFS (flood fill) | O(N*M) | O(N*M) |
| 4 | DisappearingPairs | Stack/DFS simulation | O(N) | O(N) |
| 5 | PolygonConcavityIndex | Computational geometry | O(N) | O(1) |



