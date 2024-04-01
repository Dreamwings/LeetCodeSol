class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ## S1: DP
        ## T: O(N)
        ## S: O(1)
        
        res = max_p = min_p = nums[0]
        
        for x in nums[1:]:
            max_curr = max(x, x * max_p, x * min_p)
            min_curr = min(x, x * max_p, x * min_p)
            max_p, min_p = max_curr, min_curr
            res = max(res, max_p)
            
        return res