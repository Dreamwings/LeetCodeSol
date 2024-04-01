class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n
        p = 1
        
        for i in range(1, n):
            p *= nums[i-1]
            res[i] = p
        
        p = 1
        
        for i in range(n-2, -1, -1):
            p *= nums[i+1]
            res[i] *= p
            
        return res
        