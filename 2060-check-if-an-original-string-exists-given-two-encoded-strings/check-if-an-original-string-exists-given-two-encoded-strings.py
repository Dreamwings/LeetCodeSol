class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:

        ## S2: DFS + Cache

        from functools import lru_cache
    
        @lru_cache(None)
        def dfs(s1, s2, i, j, diff):
            if i == len(s1) and j == len(s2):
                return diff == 0
            if i < len(s1) and s1[i].isdigit():
                k = i
                val = 0
                while k < len(s1) and s1[k].isdigit():
                    val = val*10 + int(s1[k])
                    k += 1
                    if dfs(s1, s2, k, j, diff - val):
                        return True
            elif j < len(s2) and s2[j].isdigit():
                k = j
                val = 0
                while k < len(s2) and s2[k].isdigit():
                    val = val*10 + int(s2[k])
                    k += 1
                    if dfs(s1, s2, i, k, diff + val):
                        return True
            elif diff == 0:
                if i < len(s1) and j < len(s2) and s1[i] == s2[j] and dfs(s1, s2, i+1, j+1, diff):
                    return True
            elif diff > 0:
                if i < len(s1) and dfs(s1, s2, i+1, j, diff - 1):
                    return True
            elif diff < 0:
                if j < len(s2) and dfs(s1, s2, i, j+1, diff + 1):
                    return True
            return False
        
        return dfs(s1, s2, 0, 0, 0)
        

        """
        ## S3: DP
        ## https://algo.monster/liteproblems/2060
        ## T: O(M * N * (M + N))
        ## S: O(M * N * (M + N))

        ## S1: DP

        def gg(s): 
            # Return possible length.
            ans = {int(s)}
            for i in range(1, len(s)): 
                ans |= {x+y for x in gg(s[:i]) for y in gg(s[i:])}
            return ans
        
        @cache
        def fn(i, j, diff): 
            # Return True if s1[i:] matches s2[j:] with given differences.
            if i == len(s1) and j == len(s2): return diff == 0
            if i < len(s1) and s1[i].isdigit(): 
                ii = i
                while ii < len(s1) and s1[ii].isdigit(): ii += 1
                for x in gg(s1[i:ii]): 
                    if fn(ii, j, diff-x): return True 
            elif j < len(s2) and s2[j].isdigit(): 
                jj = j 
                while jj < len(s2) and s2[jj].isdigit(): jj += 1
                for x in gg(s2[j:jj]): 
                    if fn(i, jj, diff+x): return True 
            elif diff == 0: 
                if i < len(s1) and j < len(s2) and s1[i] == s2[j]: return fn(i+1, j+1, 0)
            elif diff > 0: 
                if i < len(s1): return fn(i+1, j, diff-1)
            else: 
                if j < len(s2): return fn(i, j+1, diff+1)
            return False 
            
        return fn(0, 0, 0)

        
        """
