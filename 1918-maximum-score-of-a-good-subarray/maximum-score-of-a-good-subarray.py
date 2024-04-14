class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        ## S2: Monotonic Stack
        ## T: O(N)
        ## S: O(N)

        n = len(nums)
        left = [-1] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                left[stack.pop()] = i
                
            stack.append(i)
            
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                right[stack.pop()] = i
            
            stack.append(i)

        ans = 0
        for i in range(n):
            if left[i] < k and right[i] > k:
                ans = max(ans, nums[i] * (right[i] - left[i] - 1))
        
        return ans

        

        ## S1: Binary Search
        ## T: O(NlogN)
        ## S: O(N)

        def solve(nums, k):
            n = len(nums)
            left = [0] * k
            curr_min = inf
            for i in range(k - 1, -1, -1):
                curr_min = min(curr_min, nums[i])
                left[i] = curr_min

            right = []
            curr_min = inf
            for i in range(k, n):
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)

            ans = 0
            for j in range(len(right)):
                curr_min = right[j]
                i = bisect_left(left, curr_min)
                size = (k + j) - i + 1
                ans = max(ans, curr_min * size)
                
            return ans
        
        return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))