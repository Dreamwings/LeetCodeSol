class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        ## S1: Hash Map
        ## T: O(N)
        ## S: O(N)
        
        counts = collections.defaultdict(int)
        res = 0
        
        for num in nums:
            res += counts[num]
            counts[num] += 1
        
        return res