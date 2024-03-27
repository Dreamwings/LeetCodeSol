class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        
        ## S2: Stack
        ## T: O(N)
        ## S: O(N)

        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)
        ans = 0
        for i in range(n -1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                ans = max(ans, i - stack[-1] + 1)
                stack.pop(-1)
        return ans
        
        """
        ## S1: Hash Table + Sorting
        ## T: O(NlogN)
        ## S: O(N)

        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        ans, k = 0, inf
        for x in sorted(d, reverse=True):
            ans = max(ans, d[x][-1] - k + 1)
            k = min(k, d[x][0])
        return ans
        """