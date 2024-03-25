class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        from collections import defaultdict

        ## S1:
        ## T: O(N)
        ## S: O(N)
        
        d = defaultdict(int)
        d[0] = 1  # IMPORTANT, it means an subarray starting from nums[0] has a sum of k
        s, res = 0, 0
        
        for x in nums:
            s += x  # s is the current prefix sum
            pre_s = s - k
            if pre_s in d:
                res += d[pre_s]
            d[s] += 1
        
        return res
        
        """

        ## S2: Brute Force
        ## Time Limit Exceeded

        s=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1]) == k:
                    s += 1 
        return s 

        """
