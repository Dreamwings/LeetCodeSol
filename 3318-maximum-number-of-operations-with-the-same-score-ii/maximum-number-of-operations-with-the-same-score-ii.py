class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        ## S1: DFS with Memoization
        ## T: O(N^2)
        ## S: O(N^2)

        # Use lru_cache decorator to cache the results of the recursive calls
        @lru_cache(maxsize=None)
        def dfs(start: int, end: int, target_sum: int) -> int:
            # Base case: if the subarray has less than two elements, no pair can be formed
            if end - start < 1:
                return 0
            max_ops = 0
            # If the first two elements make up the target sum, explore the subproblem excluding them
            if nums[start] + nums[start + 1] == target_sum:
                max_ops = max(max_ops, 1 + dfs(start + 2, end, target_sum))
            # If the first and last elements make up the target sum, explore the subproblem excluding them
            if nums[start] + nums[end] == target_sum:
                max_ops = max(max_ops, 1 + dfs(start + 1, end - 1, target_sum))
            # If the last two elements make up the target sum, explore the subproblem excluding them
            if nums[end - 1] + nums[end] == target_sum:
                max_ops = max(max_ops, 1 + dfs(start, end - 2, target_sum))
            return max_ops

        # Calculate the total length of the array
        n = len(nums)
        # Try all possible pairs that include the first and last element
        first_two = dfs(2, n - 1, nums[0] + nums[1])
        last_two = dfs(0, n - 3, nums[-1] + nums[-2])
        first_last = dfs(1, n - 2, nums[0] + nums[-1])
        # One operation is already counted so we add 1 to the maximum of the three possibilities
        return 1 + max(first_two, last_two, first_last)        