class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ## S2: DP
        ## Time: O(N * S)
        ## Space: O(S)
        
        s = sum(nums)
        if s & 1: return False
        s = s >> 1
        
        dp = [False] * (s + 1)
        dp[0] = True
        
        for x in nums:
            if dp[s]:
                return True
            for y in range(s, x - 1, -1):
                # y is the possible sum with x
                dp[y] = dp[y] | dp[y - x]
        
        return dp[s]
        
        """
        ## S 1:
        
        s = sum(nums)
        if s & 1: return False
        s = s >> 1
        
        d = set([0])
        
        for x in nums:
            c = d.copy()
            for y in c:
                z = x + y
                if z == s:
                    return True
                elif z < s:
                    d.add(z)
        
        return False
        """
