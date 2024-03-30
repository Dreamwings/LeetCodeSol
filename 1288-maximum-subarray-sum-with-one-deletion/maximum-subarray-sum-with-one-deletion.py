class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        ## S2: DP
        ## T: O(N)
        ## S: O(1)

        res = zero = one = -inf
        for x in arr:
            one = max(zero, x + one)
            zero = max(x, x + zero)
            res = max(res, one, zero)
        return res

        """
        ## S1: DP
        ## T: O(N)
        ## S: O(N)

        n = len(arr)
        max_ending_here = n * [arr[0]]
        for i in range(1, n):
            max_ending_here[i] = max(max_ending_here[i-1] + arr[i], arr[i])
        return max(max_ending_here)
        """