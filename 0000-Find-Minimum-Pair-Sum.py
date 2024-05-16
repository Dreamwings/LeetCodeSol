"""
Meta Coding Questions:

Find Minimum Pair Sum
Given two arrays A[] and B[] of size N each, the task is
to minimize A[i] + B[j] such that j ≥ i. Assume A and B
have the same length.

Examples:

Input: A[] = {34, 12, 45, 10, 86, 39, 77},
       B[] = {5, 42, 29, 63, 30, 33, 20}
Output: 30
Explanation: For minimizing the sum, take i = 3 and j = 6.

Input: A[] = {34, 17, 45, 10, 19},
       B[] = {2, 13, 7, 11, 16}
Output: 21
Explanation: For minimizing the sum, take both i and j = 3.
"""


## S1: Brute Force: Nested 2 for loops
## T: O(N^2)
## S: O(1)

## S2:
## T: O(N)
## S: O(N)

def min_pair_sum(A, B):
    n = len(A)
    C = [0] * n # C[i] is the min value in B[i:]
    C[-1] = B[-1] # last element
    res = float('inf')

    for i in reversed(range(n - 1)):
        C[i] = min(B[i], C[i+1])

    for i in range(n):
        res = min(res, A[i] + C[i])

    return res

A = [34, 12, 45, 10, 86, 39, 77]
B = [5, 42, 29, 63, 30, 33, 20]
res = min_pair_sum(A, B)
print(res)

A = [34, 17, 45, 10, 19]
B = [2, 13, 7, 11, 16]
res = min_pair_sum(A, B)
print(res)




