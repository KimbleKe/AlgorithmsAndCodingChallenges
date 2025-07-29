Problem: GenomicRangeQuery 基因组范围查询
  find the minimal nucleotide from a range of sequence DNA.

Task Description:
Given a DNA sequence S (consisting of characters 'A', 'C', 'G', 'T') and two arrays P and Q (each of length M), where each pair (P[k], Q[k]) represents a query for the minimal nucleotide impact factor 核苷酸影响因子 in S[P[k]..Q[k]]. The impact factors are: A=1, C=2, G=3, T=4. Return an array of answers for all queries.

Examples:
S = "CAGCCTA", P = [2, 5, 0], Q = [4, 5, 6] → Returns [2, 4, 1]

Query 1: S[2..4] = "GCC" → min(3, 2, 2) = 2

Query 2: S[5..5] = "T" → 4

Query 3: S[0..6] = "CAGCCTA" → min(2, 1, 3, 2, 2, 4, 1) = 1

Constraints:
N (length of S) and M (length of queries) up to 100,000.

Time: O(N + M)

Space: O(N)



<br><br><br>

> **Difficulty level**
> medium