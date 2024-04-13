class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        ## S2: DP + DFS
        ## T: O(2^N)
        ## S: O(N)
        
        arr = list(range(1, maxChoosableInteger + 1))

        if sum(arr) < desiredTotal:
            return False
        
        @cache
        def dp(arr, remain_tot):
            if arr[-1] >= remain_tot:
                return True
            
            for i in range(len(arr)):
                new_arr = arr[:i] + arr[i+1:]
                if not dp(new_arr, remain_tot - arr[i]):
                    return True

            return False

        return dp(tuple(arr), desiredTotal)  # Note convert arr to tuple(arr) for cache purpose

        """

        ## S1: DFS + Memorization  (TLE)
        ## Time: O(2^N)
        ## Space: O(N)
        
        
        max_num, t = maxChoosableInteger, desiredTotal
        
        if t <= max_num: return True
        if t > (1 + max_num) * max_num // 2: return False
        
        # @cache
        def dfs(mask, cur_sum):
            for i in range(1, max_num + 1):
                curr = 1 << i
                if mask & curr: # mask contains 1 at the position of curr, it means i is used
                    continue
                if cur_sum + i >= t or not dfs(curr | mask, cur_sum + i):
                    return True
                
            return False
        
        # dfs.cache_clear()
        
        return dfs(0, 0)
        
        """